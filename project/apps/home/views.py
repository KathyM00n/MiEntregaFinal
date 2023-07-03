from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def crear_autor(request):
    if request.method == "POST":
        form = forms.AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("home:index")
    else:
        form = forms.AutorForm() 
        return render(request, "home/crear_autor.html", {"form": form})

def crear_post(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("home:index")
    else:
        form = forms.PostForm() 
        return render(request, "home/crear_post.html", {"form":form})    