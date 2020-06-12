from django import forms
from django.template.defaulttags import widthratio

from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholer":"Your title"}))
    content = forms.CharField(max_length=100,
                              required=False,
                            widget=forms.Textarea(
                                attrs={
                                    "placeholer": "Your content"
                                }
                            )
                            )
    email = forms.CharField(max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    "class": "email"
                                }
                            )
                            )

    class Meta:
        model = Post
        fields ={'title', 'content'}

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        return title


    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data['title']
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid title")
        return email

class SendEmail(forms.Form):
    email = forms.CharField(max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    "class": "email"
                                }
                            )
                            )
    name = forms.CharField(max_length=100)
    cc = forms.BooleanField(required=False)
    content = forms.CharField(max_length=100)