from django.shortcuts import render

from main.models import Experience
from .models import Mahasiswa
from .models import Skill


def show_main(request):
    context = {
        "name": "Kaysan Navid Musyaffa",
        "npm": "2506625470",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A competitive programming enjoyer who loves problem solving. "
            "Currently studying Computer Science at Universitas Indonesia, "
            "focusing on algorithm optimization and writing efficient code. "
            "Spending my days turning complex algorithmic challenges into clean, optimized solutions."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Kaysan Navid Musyaffa",
        "experience_list": Experience.objects.all(),
        "list_mahasiswa": Mahasiswa.objects.all(),
    }
    return render(request, "experience.html", context)

def show_skills(request):
    skills_data = Skill.objects.all()
    context = {
        'skills': skills_data,
    }
    return render(request, 'skills.html', context)