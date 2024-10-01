

from django.views.generic import ListView #NEW
from .models import Post

class PostList(ListView): #NEW
    model = Post
    template_name = "post_list.html"
