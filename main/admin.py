from django.contrib import admin
from .models import Mahasiswa
from .models import Skill
from .models import Experience

@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('nama', 'npm')
    
admin.site.register(Skill)
admin.site.register(Experience)