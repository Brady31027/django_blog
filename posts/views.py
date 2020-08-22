from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_create(request):
    context = {
        "title": "Create",
    }
    return render(request, "index.html", context)

def post_detail(request):
    context = {
        "title": "Detail",
    }
    return render(request, "index.html", context)

def post_list(request):
    #if request.user.is_authenticated:
    #    context = {
    #        "title": "List",
    #        "user": request.user,
    #    }
    #else:
    #    context = {
    #        "title": "You need to login first",
    #        "user": request.user,
    #    }
    queryset = Post.objects.all()
    context = {
        "title": "List",
        "queryset": queryset,
    }
    return render(request, "index.html", context)

def post_update(request):
    context = {
        "title": "Update",
    }
    return render(request, "index.html", context)

def post_delete(request):
    context = {
        "title": "Delete",
    }
    return render(request, "index.html", context)

