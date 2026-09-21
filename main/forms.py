from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, URLInput
from main.models import Experience, Skill

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "company",
            "date_range",
            "description",
            "is_active",
        ]

        labels = {
            "title": "Posisi / Jabatan",
            "company": "Nama Perusahaan / Organisasi",
            "date_range": "Rentang Waktu",
            "description": "Deskripsi Pekerjaan",
            "is_active": "Masih Berlangsung?",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Asisten Dosen PBP",
                }
            ),
            "company": TextInput(
                attrs={
                    "placeholder": "Contoh: Universitas Indonesia",
                }
            ),
            "date_range": TextInput(
                attrs={
                    "placeholder": "Contoh: Feb 2024 - Present",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan tanggung jawab atau pencapaianmu...",
                    "rows": 4,
                }
            ),
            "is_active": CheckboxInput(), 
        }

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            "name",
            "image_url",
        ]

        labels = {
            "name": "Nama Skill",
            "image_url": "URL Gambar Logo",
        }

        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "Contoh: Python, C++, atau Django",
                }
            ),
            "image_url": URLInput(
                attrs={
                    "placeholder": "Contoh: https://link-ke-gambar-logo.com/logo.png",
                }
            ),
        }