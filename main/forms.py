from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, URLInput
from main.models import Experience, Skill
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

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
        
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Posisi/Jabatan tidak boleh hanya berisi tag HTML.")
        return title

    def clean_company(self):
        return strip_tags(self.cleaned_data["company"]).strip()

    def clean_date_range(self):
        return strip_tags(self.cleaned_data["date_range"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

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

    def clean_name(self):
        name = strip_tags(self.cleaned_data["name"]).strip()
        if not name:
            raise ValidationError("Nama skill tidak boleh hanya berisi tag HTML.")
        return name

    def clean_url(self):
        return strip_tags(self.cleaned_data.get("image_url", "")).strip()