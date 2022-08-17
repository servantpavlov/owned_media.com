from django.shortcuts import render
from .forms import UploadForm
from .models import BookImage
from django.views import generic

def top(request):
    title = 'Owned_Media'
    name = 'pavlov'
    ctx = {'title': title,
        'name': name,
        'book_image_list': BookImage.objects.all(),
    }
    return render(request, 'library/top.html', ctx)

def upload(request):
    ctx = {
        'title': 'Owned_Media : 画像のアップロード',
        'upload_form': UploadForm(),
        'id': None,
    }

    if (request.method == 'POST'):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_image = form.save()

            ctx['id'] = upload_image.id

    return render(request, 'library/upload.html', ctx)