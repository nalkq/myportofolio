from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Kaysan Navid Musyaffa",
        "npm": "2506625470",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Kaysan Navid Musyaffa",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)