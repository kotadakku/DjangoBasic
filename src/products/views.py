from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import ProductForm, RawProductForm
from .models import Product


def render_initial_data(request):
    initial_data = {
        'title': "My this awesome title"
    }
    obj = Product.objects.get(pk=6)

    # form = RawProductForm(request.POST or None, initial=initial_data)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)
# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request, id):
    obj = Product.objects.get(pk=id)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

def products_delete_view(request,id):
    obj = get_object_or_404(Product, id =id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, "products/product_delete.html", context)

def products_list_view(request):
    obj = Product.objects.all()
    context ={
        'obj':obj
    }
    return render(request, 'products/product_list.html', context)
