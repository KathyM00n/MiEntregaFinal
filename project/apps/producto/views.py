from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.template import context
from django.views.generic import DetailView
from . import forms, models
# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "producto/index.html")

def producto_categoria_list(request):
    categorias = models.ProductoCategoria.objects.all()
    context = {"categorias": categorias}
    return render(request, "producto/producto_categoria_list.html", context)

def producto_categoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:index")
    else:
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/producto_categoria_create.html", {"form":form})

#def producto_categoria_detail(request): HttpRequest , pk) -> HttpResponse:
#    categoria = models.ProductoCategoria.objects.get(id=pk)
#    return render(request, "producto/producto_categoria_detail.html", {"object":categoria})
 
class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria


