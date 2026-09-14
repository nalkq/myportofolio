from django.contrib import admin
from .models import Mahasiswa
from .models import Skill

@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'npm')
    
admin.site.register(Skill)