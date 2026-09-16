from django.forms import ModelForm, TextInput, Textarea, CheckboxInput
from main.models import Experience

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