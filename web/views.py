from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from products.models import Product


@login_required(login_url="users/login")
def index(request):
    instance=Product.objects.filter(is_deleted=False)
    
    context={
        "title": "OnlineStore | Home",
        "instances":instance
    }

    return render(request, "index.html",context)

@login_required(login_url="users/admin-login")
def admin_view(request):
    instance=Product.objects.filter(is_deleted=False)
    
    context={
        "title": "OnlineStore | Home",
        "instances":instance
    }

    return render(request, "admin_home.html",context)