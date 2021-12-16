from django.forms import (
    ModelForm,
    CharField,
    PasswordInput,
)
from Utils.models import User


class RegistrationForm(ModelForm):
    confirm_password = CharField(widget=PasswordInput())

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password',]