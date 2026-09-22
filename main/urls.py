from django.urls import path

from main.views import (
    show_main, show_experience, show_skills, 
    create_experience, get_experience_json, delete_experience, edit_experience,
    create_skill, get_skill_json, delete_skill, edit_skill,
    register, login_user, logout_user,
    toggle_star_experience, toggle_star_skill
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('skills/', show_skills, name='show_skills'),
    
    path("experiences/add/", create_experience, name="create_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<int:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("experience/<int:experience_id>/edit/", edit_experience, name="edit_experience"),
    
    path("skills/add/", create_skill, name="create_skill"),
    path("api/skill/", get_skill_json, name="get_skill_json"),
    path("skills/<int:skill_id>/delete/", delete_skill, name="delete_skill"),
    path("skills/<int:skill_id>/edit/", edit_skill, name="edit_skill"),
    
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    
    path("experience/<int:experience_id>/star/", toggle_star_experience, name="toggle_star_experience"),
    path("skill/<int:skill_id>/star/", toggle_star_skill, name="toggle_star_skill"),
]