from django.urls import path
from main import api_views

app_name = "api"
urlpatterns = [
    path("experiences/", api_views.experience_list, name="experience-list"),
    path("experiences/<int:experience_id>/", api_views.experience_detail, name="experience-detail"),
    path("experiences/<int:experience_id>/star/", api_views.experience_star, name="experience-star"),
]
