from django import forms

class SignUpForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    #email = forms.EmailField()
    username=forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)