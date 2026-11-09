from django.contrib.auth.models import Group, Permission, User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


from main.models import Experience, Skill


class ExperienceAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner", password="test-password", email="owner@example.com",
        )
        self.visitor = User.objects.create_user(username="visitor", password="test-password")
        self.experience = Experience.objects.create(
            title="Asisten Dosen", description="Membantu praktikum", company="UI",
            date_range="2026 - Sekarang", is_active=True,
        )
        self.list_url = reverse("api:experience-list")
        self.detail_url = reverse("api:experience-detail", args=[self.experience.id])
        self.star_url = reverse("api:experience-star", args=[self.experience.id])
        self.payload = {
            "title": "Pengalaman baru", "description": "Mengembangkan aplikasi", "company": "ABC",
            "date_range": "2025 - 2026", "is_active": False,
        }

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], self.experience.id)
        self.assertFalse(response.data[0]["is_starred"])
        self.assertNotIn("fields", response.data[0])
        self.assertEqual(self.client.get(self.detail_url).status_code, status.HTTP_200_OK)

    def test_search_and_empty_results(self):
        response = self.client.get(self.list_url, {"title": "ASISTEN"})
        self.assertEqual(len(response.data), 1)
        response = self.client.get(self.list_url, {"title": "not-found"})
        self.assertEqual(response.data, [])

    def test_missing_experience(self):
        missing_id = self.experience.id + 1
        url = reverse("api:experience-detail", args=[missing_id])
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)

    def test_guest_and_visitor_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)
            self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.patch(self.detail_url, {"title": "Changed"}, format="json").status_code, 403)
            self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertEqual(Experience.objects.count(), 1)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Asisten Dosen")

    def test_owner_can_create(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Experience.objects.filter(pk=response.data["id"]).exists())

    def test_validation(self):
        self.client.force_authenticate(user=self.owner)
        for changes, field in [
            ({"title": "   "}, "title"),
            ({"title": '<img src="x" onerror="alert(1)">'}, "title"),
            ({"title": "A" * 101}, "title"),
            ({"is_active": "not-a-boolean"}, "is_active"),
        ]:
            response = self.client.post(self.list_url, {**self.payload, **changes}, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn(field, response.data)
        self.assertEqual(Experience.objects.count(), 1)

    def test_patch_put_and_delete(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(self.detail_url, {"title": "Changed"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.description, "Membantu praktikum")
        response = self.client.put(self.detail_url, {"title": "Incomplete"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.put(self.detail_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")
        self.assertFalse(Experience.objects.filter(pk=self.experience.id).exists())

    def test_star_requires_login_and_toggles(self):
        self.assertEqual(self.client.post(self.star_url).status_code, status.HTTP_403_FORBIDDEN)
        self.client.force_authenticate(user=self.visitor)
        response = self.client.post(self.star_url)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)
        response = self.client.post(self.star_url)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 0)

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {
            **self.payload, "star_count": 99, "is_starred": True,
            "starred_by_names": "forged", "starred_by": [self.visitor.id],
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])

    def test_editor_can_update_but_cannot_create_or_delete(self):
        self.visitor.groups.add(Group.objects.create(name="Editor"))
        self.client.force_authenticate(user=self.visitor)

        response = self.client.patch(self.detail_url, {"title": "Changed"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Changed")

        response = self.client.put(self.detail_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        count_before = Experience.objects.count()  
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Experience.objects.count(), count_before)  

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Experience.objects.filter(pk=self.experience.id).exists())

    def test_wrong_method(self):
        self.client.force_authenticate(user=self.owner)
        self.assertEqual(self.client.delete(self.list_url).status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner", password="test-password"))
        response = client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Experience.objects.count(), 1)

    def test_session_write_with_csrf_succeeds(self):
        client = APIClient(enforce_csrf_checks=True)
        client.login(username="owner", password="test-password")
        # The Browsable API form renders a real CSRF token into the response.
        page = client.get(self.list_url, HTTP_ACCEPT="text/html")
        self.assertEqual(page.status_code, status.HTTP_200_OK)
        token = client.cookies["csrftoken"].value
        response = client.post(
            self.list_url, self.payload, format="json", HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_old_edit_page_access(self):
        url = reverse("main:edit_experience", args=[self.experience.id])

        response = self.client.get(url)
        self.assertRedirects(response, f"/login/?next={url}")

        self.client.force_login(self.visitor)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.visitor.groups.add(Group.objects.create(name="Editor"))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, "edit_experience.html")

        self.client.force_login(self.owner)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_old_edit_page_cannot_save_with_post(self):
        self.visitor.groups.add(Group.objects.create(name="Editor"))
        url = reverse("main:edit_experience", args=[self.experience.id])
        original_data = Experience.objects.values().get(pk=self.experience.id)

        for user in (self.visitor, self.owner):
            self.client.force_login(user)
            response = self.client.post(url, self.payload)
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
            self.assertEqual(
                Experience.objects.values().get(pk=self.experience.id),
                original_data,
            )

    def test_old_create_and_delete_views_require_superuser(self):
        self.visitor.user_permissions.add(
            *Permission.objects.filter(
                content_type__app_label="main",
                codename__in=["add_experience", "delete_experience"],
            )
        )
        create_url = reverse("main:create_experience")
        ajax_url = reverse("main:create_experience_ajax")
        delete_url = reverse("main:delete_experience", args=[self.experience.id])
        count_before = Experience.objects.count()
        original_data = Experience.objects.values().get(pk=self.experience.id)
        editor_group = Group.objects.create(name="Editor")

        for is_editor in (False, True):
            if is_editor:
                self.visitor.groups.add(editor_group)
            self.client.force_login(self.visitor)

            for url in (create_url, ajax_url, delete_url):
                with self.subTest(is_editor=is_editor, url=url):
                    response = self.client.post(url, self.payload)
                    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
                    self.assertEqual(Experience.objects.count(), count_before)
                    self.assertEqual(
                        Experience.objects.values().get(pk=self.experience.id),
                        original_data,
                    )

    def test_experience_page_edit_permission_context(self):
        url = reverse("main:show_experience")

        response = self.client.get(url)
        self.assertFalse(response.context["can_edit_experience"])

        self.client.force_login(self.visitor)
        response = self.client.get(url)
        self.assertFalse(response.context["can_edit_experience"])

        self.visitor.groups.add(Group.objects.create(name="Editor"))
        response = self.client.get(url)
        self.assertTrue(response.context["can_edit_experience"])

        self.client.force_login(self.owner)
        response = self.client.get(url)
        self.assertTrue(response.context["can_edit_experience"])
        
class SkillAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner", password="test-password", email="owner@example.com",
        )
        self.visitor = User.objects.create_user(username="visitor", password="test-password")
        self.editor = User.objects.create_user(username="editor", password="test-password")
        self.editor.groups.add(Group.objects.create(name="Editor"))
        self.skill = Skill.objects.create(name="Python", image_url="https://example.com/python.png")
        self.list_url = reverse("api:skill-list")
        self.detail_url = reverse("api:skill-detail", args=[self.skill.id])
        self.star_url = reverse("api:skill-star", args=[self.skill.id])
        self.payload = {
            "name": "Django", "image_url": "https://example.com/django.png",
        }

    def test_public_read_search_and_missing_skill(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["id"], self.skill.id)
        self.assertEqual(response.data[0]["name"], "Python")
        self.assertNotIn("fields", response.data[0])
        self.assertNotIn("starred_by", response.data[0])
        self.assertEqual(self.client.get(self.detail_url).status_code, 200)
        self.assertEqual(len(self.client.get(self.list_url, {"title": "PYTH"}).data), 1)
        self.assertEqual(self.client.get(self.list_url, {"title": "missing"}).data, [])
        url = reverse("api:skill-detail", args=[self.skill.id + 1])
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_guest_and_visitor_cannot_write(self):
        original_data = Skill.objects.values().get(pk=self.skill.id)
        count_before = Skill.objects.count()
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)
            self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.patch(self.detail_url, {"name": "Changed"}, format="json").status_code, 403)
            self.assertEqual(self.client.put(self.detail_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
            self.assertEqual(Skill.objects.count(), count_before)
            self.assertEqual(Skill.objects.values().get(pk=self.skill.id), original_data)

    def test_editor_can_update_but_cannot_create_or_delete(self):
        self.client.force_authenticate(user=self.editor)
        response = self.client.patch(self.detail_url, {"name": "Changed"}, format="json")
        self.assertEqual(response.status_code, 200)
        self.skill.refresh_from_db()
        self.assertEqual(self.skill.name, "Changed")
        self.assertEqual(self.skill.image_url, "https://example.com/python.png")
        self.assertEqual(self.client.put(self.detail_url, self.payload, format="json").status_code, 200)

        count_before = Skill.objects.count()
        original_data = Skill.objects.values().get(pk=self.skill.id)
        self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertEqual(Skill.objects.count(), count_before)
        self.assertEqual(Skill.objects.values().get(pk=self.skill.id), original_data)

    def test_owner_can_create_update_and_delete(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, 201)
        created = Skill.objects.get(pk=response.data["id"])
        self.assertEqual(created.name, "Django")
        self.assertEqual(self.client.patch(self.detail_url, {"name": "Updated"}, format="json").status_code, 200)
        self.skill.refresh_from_db()
        self.assertEqual(self.skill.name, "Updated")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.content, b"")
        self.assertFalse(Skill.objects.filter(pk=self.skill.id).exists())

    def test_validation_and_cleaning(self):
        self.client.force_authenticate(user=self.owner)
        count_before = Skill.objects.count()
        for changes, field in [
            ({"name": "   "}, "name"),
            ({"name": "<b></b>"}, "name"),
            ({"name": "A" * 101}, "name"),
            ({"image_url": "javascript:alert(1)"}, "image_url"),
        ]:
            response = self.client.post(self.list_url, {**self.payload, **changes}, format="json")
            self.assertEqual(response.status_code, 400)
            self.assertIn(field, response.data)
            self.assertEqual(Skill.objects.count(), count_before)
        response = self.client.post(self.list_url, {"name": " <b>Django</b> ", "image_url": ""}, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Skill.objects.get(pk=response.data["id"]).name, "Django")

    def test_star_requires_login_and_uses_current_account(self):
        self.assertEqual(self.client.post(self.star_url).status_code, 403)
        self.assertEqual(self.skill.starred_by.count(), 0)
        self.client.force_authenticate(user=self.visitor)
        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)
        self.assertTrue(self.skill.starred_by.filter(pk=self.visitor.id).exists())
        self.client.force_authenticate(user=self.editor)
        self.assertFalse(self.client.get(self.detail_url).data["is_starred"])
        self.client.force_authenticate(user=self.visitor)
        response = self.client.post(self.star_url)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(self.skill.starred_by.count(), 0)

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {
            **self.payload, "star_count": 99, "is_starred": True,
            "starred_by_names": "forged", "starred_by": [self.visitor.id],
        }, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["starred_by_names"], "")
        self.assertEqual(Skill.objects.get(pk=response.data["id"]).starred_by.count(), 0)

    def test_session_write_requires_csrf(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner", password="test-password"))
        count_before = Skill.objects.count()
        self.assertEqual(client.post(self.list_url, self.payload, format="json").status_code, 403)
        self.assertEqual(Skill.objects.count(), count_before)
        client.get(self.list_url, HTTP_ACCEPT="text/html")
        token = client.cookies["csrftoken"].value
        response = client.post(
            self.list_url, self.payload, format="json", HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Skill.objects.filter(pk=response.data["id"]).exists())

    def test_old_skill_json_endpoint(self):
        url = reverse("main:get_skill_json")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["fields"]["name"], "Python")
        self.assertEqual(len(self.client.get(url, {"title": "PYTH"}).json()), 1)
        self.assertEqual(self.client.get(url, {"title": "missing"}).json(), [])

    def test_old_ajax_create_success_and_invalid_input(self):
        self.client.force_login(self.owner)
        url = reverse("main:create_skill_ajax")
        response = self.client.post(url, self.payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Skill.objects.get(pk=response.json()["pk"]).name, "Django")
        count_before = Skill.objects.count()
        response = self.client.post(url, {"name": "", "image_url": ""})
        self.assertEqual(response.status_code, 400)
        self.assertIn("name", response.json()["errors"])
        self.assertEqual(Skill.objects.count(), count_before)

    def test_old_ajax_create_rejects_guest_visitor_and_editor(self):
        url = reverse("main:create_skill_ajax")
        count_before = Skill.objects.count()
        for user in (None, self.visitor, self.editor):
            self.client.logout()
            if user is not None:
                self.client.force_login(user)
            response = self.client.post(url, self.payload)
            self.assertEqual(response.status_code, 403)
            self.assertEqual(Skill.objects.count(), count_before)