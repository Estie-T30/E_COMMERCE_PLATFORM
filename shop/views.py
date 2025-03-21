from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

# Create a new product
def product_create(request):
    if request.method == 'POST':   # Redirect to product list after saving
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list') # Redirect to product list
    else:  # Show empty form on GET request
        form = ProductForm()
    return render(request, 'shop/product_form.html', {'form': form})

# Update an existing product
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/product_form.html', {'form': form})

# Delete a product
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'shop/product_confirm_delete.html', {'product': product})

