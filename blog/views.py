from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
