import json

from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from products.forms import ProductForm
from products.functions import generate_form_errors
from products.models import Product,Cart


@staff_member_required 
def create_product(request):
    if request.method == 'POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()

            response_data = {
                "title": "Successfully submitted",
                "message": "Successfully submitted",
                "status": "success",
                "redirect": "yes",
                "redirect_url": "/"
            }
        else:
            error_message = generate_form_errors(form)
            response_data = {
                "title": "form validation error",
                "message": str(error_message),
                "status": "error",
                "stable": "yes",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    else:
        form = ProductForm()
        context = {
            "form": form,
            "title": "Add a new Product"

        }
        return render(request, "products/create-product.html", context=context)


@staff_member_required 
def edit_product(request,id):
    instance=get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form=ProductForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()

            response_data = {
                "title": "Successfully submitted",
                "message": "Successfully submitted",
                "status": "success",
                "redirect": "yes",
                "redirect_url": "/"
            }
        else:
            error_message = generate_form_errors(form)
            response_data = {
                "title": "form validation error",
                "message": str(error_message),
                "status": "error",
                "stable": "yes",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    
    else:
        form = ProductForm(instance=instance)
        print(form)
        context = {
            "form": form,
            "title": "Edit Product"

        }
        return render(request, "products/create-product.html", context=context)  



@staff_member_required 
def delete_product(request, id):
    instance = get_object_or_404(Product, id=id)
    instance.is_deleted = True
    instance.delete()

    response_data = {
        "title": "successfully deleted",
        "message": "post deleted successfully",
        "status": "success"
    }

    return HttpResponse(json.dumps(response_data), content_type="application/json")
            

# view cart items
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        item.total_price = item.quantity * item.product.price
    context = {
        'cart': cart_items
    }
    return render(request, 'products/view_cart.html', context=context)


# add to cart functionality
@login_required(login_url="/users/login/")
def add_to_cart(request,id):
    instance=get_object_or_404(Product,id=id)
    cart, created = Cart.objects.get_or_create(user=request.user, product=instance)

    if not created:
        cart.quantity += 1
        cart.save()

    return redirect('products:view_cart')


