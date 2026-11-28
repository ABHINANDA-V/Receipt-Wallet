
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ReceiptUserCreationForm(UserCreationForm):

    username = forms.EmailField(
        label="Email Address"
    )

    first_name = forms.CharField(
        label="Full Name",
        max_length=150
    )

    class Meta(UserCreationForm.Meta):

        model = User

        fields = (
            "first_name",
            "username",
        )

    # Add Bootstrap classes and placeholders
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs.update({
                "class": "form-control py-3"
            })

        self.fields["first_name"].widget.attrs.update({
            "placeholder": "Enter your full name",
            "id": "full_name"
        })

        self.fields["username"].widget.attrs.update({
            "placeholder": "Enter your email address",
            "id": "email"
        })

        self.fields["password1"].widget.attrs.update({
            "placeholder": "Create a password",
            "id": "password"
        })

        self.fields["password2"].widget.attrs.update({
            "placeholder": "Confirm your password",
            "id": "confirm_password"
        })

    # Save user and email
    def save(self, commit=True):

        user = super().save(commit=False)

        user.email = user.username

        if commit:
            user.save()

        return user
