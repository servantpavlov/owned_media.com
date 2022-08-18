from socket import fromshare
from django import forms
from .models import BookArticle

class UploadForm(forms.ModelForm):
    class Meta:
        model = BookArticle
        fields = "__all__"