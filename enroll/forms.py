from django import forms
from .models import User

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("id","name","email","password","Profile_Images")
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","placeholder":"Username","aria-label":"Username"}),
            'email': forms.EmailInput(attrs={"class":"form-control","placeholder":"user@gmail.com","aria-label":"user@gmail.com"}),
            'password': forms.PasswordInput(render_value=True ,attrs={"class":"form-control","placeholder":"********","aria-label":"********"}),
        }
