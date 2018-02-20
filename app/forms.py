from app.models import Enterprise
from django import forms


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'id': 'id_name', 'required': True,
                       'placeholder': 'Название предприятия',
                       'class': 'form-control', 'type': 'text', }),
        }
