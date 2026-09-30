from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Skill


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            company="Universitas Indonesia",
            date_range="Feb 2024 - Present",
            description="Membantu mahasiswa memahami pengembangan web Django.",
            is_active=True
        )
        
        self.skill = Skill.objects.create(
            name="C++",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP - Universitas Indonesia")
        self.assertEqual(self.experience.date_range, "Feb 2024 - Present")
        self.assertTrue(self.experience.is_active)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
  
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.company)
        self.assertContains(response, self.experience.description)

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada data experience yang ditambahkan pada halaman ini.")
    
    def test_inactive_experience(self):
        self.experience.is_active = False
        self.experience.save()
        
        response = self.client.get(reverse("main:show_experience"))
        
        self.assertFalse(self.experience.is_active)
        
    def test_skill_model(self):
        self.assertEqual(str(self.skill), "C++")
        self.assertEqual(self.skill.name, "C++")
        
    def test_skill_page(self):
        response = self.client.get(reverse("main:show_skills"))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skills.html") 
        
        self.assertContains(response, self.skill.name)
        
    def test_empty_skill_page(self):
        Skill.objects.all().delete()
        
        response = self.client.get(reverse("main:show_skills"))
        
        self.assertContains(response, "Belum ada skill yang ditambahkan pada halaman ini.")