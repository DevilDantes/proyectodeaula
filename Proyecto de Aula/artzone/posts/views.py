from django.shortcuts import render, redirect
from .models import Post
from django.core.files.storage import FileSystemStorage

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')  # Usa get para evitar KeyError
        content = request.POST.get('content', '')
        image_url = None

        if 'image' in request.FILES:
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            image_url = fs.url(filename)

        post = Post(username=username, content=content, image=image_url)
        post.save()
        return redirect('home')

    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})
