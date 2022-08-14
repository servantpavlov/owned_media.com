from django.shortcuts import render

def top(request):
    title = 'Owned_Media'
    ctx = {'title': title}
    return render(request, 'library/top.html', ctx)