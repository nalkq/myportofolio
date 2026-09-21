from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience
from .models import Skill
from main.forms import ExperienceForm, SkillForm


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
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Kaysan Navid Musyaffa",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def show_skills(request):
    title_query = request.GET.get("title", "").strip()
    
    skills_data = Skill.objects.all()

    if title_query:
        skills_data = skills_data.filter(name__icontains=title_query)

    context = {
        "name": "Kaysan Navid Musyaffa",
        "skills": skills_data,
        "title_query": title_query, 
    }
    return render(request, 'skills.html', context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        
        return redirect("main:show_experience")

    context = {
        "name": "Kaysan Navid Musyaffa", 
        "form": form,
    }
    
    return render(request, "experience_form.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def create_skill(request):
    form = SkillForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill baru berhasil ditambahkan!")
        return redirect("main:show_skills")

    context = {
        "name": "Kaysan Navid Musyaffa", 
        "form": form,
    }
    
    return render(request, "skill_form.html", context)

def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill berhasil dihapus!")
        return redirect("main:show_skills")

    return redirect("main:show_skills")

def get_skill_json(request):
    title_query = request.GET.get("title", "").strip()
    skills = Skill.objects.all()

    if title_query:
        skills = skills.filter(title__icontains=title_query)

    skills_json = serializers.serialize("json", skills)
    return HttpResponse(skills_json, content_type="application/json")