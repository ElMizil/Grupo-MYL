from django import forms
from .models import DieselLog

class DieselLogForm(forms.ModelForm):
    class Meta:
        model = DieselLog
        fields = ["ubicacion", "unidad", "litros", "operador", "precio_por_litro"]
        widgets = {
            "unidad": forms.TextInput(attrs={"placeholder": "Unidad"}),
            "litros": forms.NumberInput(attrs={"placeholder": "Litros", "step": "0.01", "min": "0"}),
            "operador": forms.TextInput(attrs={"placeholder": "Operador"}),
            "precio_por_litro": forms.NumberInput(attrs={"placeholder": "Precio por litro", "step": "0.0001", "min": "0"}),
        }
