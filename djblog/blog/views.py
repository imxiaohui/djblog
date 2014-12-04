# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from blog.models import Post


def index(request):
    """blog list"""

    posts = Post.objects.all()
    return render_to_response("blog/index.html",
        {"posts": posts},
        content_instance=RequestContext(request))

def post(request, pk):
    """single post"""

    post = get_object_or_404(Post, pk=pk)
    return render_to_response("blog/post.html",
        {"post": post},
        context_instance=RequestContext(request))
