from django.shortcuts import render
from .forms import UploadForm
from .models import BookArticle
from django.views import generic

def book_list(request):
    title = 'Owned_Media'
    name = 'pavlov'
    ctx = {
        'title': title,
        'name': name,
        'book_list': BookArticle.objects.all(),
    }
    return render(request, 'library/book_list.html', ctx)

def book_detail(request, pk):
    title = 'Owned_Media'
    name = 'pavlov'
    ctx ={
        'title': title,
        'name': name,
        'book_detail': BookArticle.objects.get(pk=pk),
    }
    
    return render(request, 'library/book_detail.html', ctx)

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