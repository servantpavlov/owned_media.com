from socket import fromshare
from django import forms
from .models import BookImage

class UploadForm(forms.ModelForm):
    class Meta:
        model = BookImage
        fields = ["image"]