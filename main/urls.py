from django.urls import path

from main.views import show_main, show_experience, show_skills, create_experience, get_experience_json, delete_experience, create_skill, get_skill_json, delete_skill

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('skills/', show_skills, name='show_skills'),
    
    path("experiences/add/", create_experience, name="create_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<int:experience_id>/delete/", delete_experience, name="delete_experience"),
    
    path("skills/add/", create_skill, name="create_skill"),
    path("api/skill/", get_skill_json, name="get_skill_json"),
    path("skills/<int:skill_id>/delete/", delete_skill, name="delete_skill"),
]