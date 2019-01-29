#from django import forms
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    ## configuracion de propiedades del tag en html
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Your full name"
            }
            )
    )

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class":"form-control",
            "placeholder":"Your full name"
            }
            )
    )
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',"placeholder":"Juan Jose B"
            }
        )
    )

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if not "gmail.com" in email:
    #         raise forms.ValidationError("Email has to be gmail.com")
    #     return email



