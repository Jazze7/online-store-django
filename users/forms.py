from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password']
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"})
        }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")

        if User.objects.filter(username=username).exists():
            self.add_error("username", "Username already exists")
