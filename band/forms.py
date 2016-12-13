from django import forms
from models import BandInfo

class SignupForm(forms.ModelForm):
    class Meta:
        model = BandInfo
        fields = "__all__"
        widgets = {
            'est_date': forms.TextInput(attrs={'placeholder': 'dd/mm/yy'})
        }
        exclude = ["pub_date"]
