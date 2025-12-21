from django.shortcuts import render
from django.db.models import Q
from .models import Post

def search(request):
    if request.method == 'POST':
        query = request.POST['q']
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
        ).distinct()
        return render(request, 'blog/search.html', {'query': query, 'posts': posts})
    else:
        return render(request, 'blog/search.html', {})
