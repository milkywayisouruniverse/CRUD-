from django.shortcuts import render, get_object_or_404, redirect
from clothing.models import Product
from .forms import ProductForm

# Create your views here.
def clothing(request):
    form = ProductForm()
    pro_img = Product.objects.all()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductForm()  # reset form after saving

    return render(request, 'clothing/fashion.html',{'pro_img': pro_img,'form':form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('clothing')  # Make sure 'clothing' is a valid URL name

    else:
        form = ProductForm(instance=product)

    return render(request, 'clothing/edit_product.html', {'form': form, 'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        product.delete()
        return redirect('clothing')  # Ensure this is a valid URL name

    return render(request, 'clothing/confirm_delete.html', {'product': product})
