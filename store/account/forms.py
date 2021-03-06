from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label=_('نام کاربری'), max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=_('کلمه عبور'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'email', 'password')
        labels = {'username': _('نام کاربری'), 'email': _('ایمیل'), 'password': _('کلمه عبور'),
                  'password2': _('تکرار کلمه عبور'), 'first_name': _('نام'), 'last_name': _('نام خانوادگی'), }
        widget = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                  'email': forms.EmailInput(attrs={'class': 'form-control'}),
                  'password': forms.PasswordInput(attrs={'class': 'form-control'}),
                  'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
                  'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                  'last_name': forms.TextInput(attrs={'class': 'form-control'}), }
        help_text = {'email': _('A valid email for reset your password'), }
