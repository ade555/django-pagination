from .models import Post
from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_list_view.html'
    context_object_name = 'page'
    paginate_by = 2



# uncomment below for function-based view
"""
from django.shortcuts import render
from django.core.paginator import Paginator

def list_view(request):
    posts = Post.objects.all()
    paginated = Paginator(posts, 3)

    # Get the requested page number from the URL
    page_number = request.GET.get('page')
    
    page = paginated.get_page(page_number)
    return render(request, 'blog/blog_list_view.html', {'page':page})
"""