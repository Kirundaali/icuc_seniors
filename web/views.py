from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from products.models import Product, ProductImage,Category
from django.contrib.auth.decorators import login_required

# This all_category carry the whole products category objects
all_category = Category.objects.all()

# this function for custom made 404 page view
def error_404_view(request, exception):
    return render(request, '404.html', status=404)

# this is home page view

def index(request):
    featured_cakes = Product.objects.all().filter(featured_cake=True)
    context = {
        "title": "Test title",
        "featured_cakes": featured_cakes,
    }
    return render(request, "home.html", context)


# this is about page view
def about(request):
    breadcrumb_list = ["about-us"]
    context = {
        "title": "About Us",
        "breadcrumb_list": breadcrumb_list,
    }
    return render(request, "about-us.html", context)


# this is cake-flavour page view
def cake_flavours(request):
    breadcrumb_list = ["cake-flavours"]
    context = {
        "title": "Cake Flavours",
        "breadcrumb_list": breadcrumb_list,
    }
    return render(request, "cake-flavours.html", context)


# this contact-us page view
def contacts(request):
    breadcrumb_list = ["contact-us"]
    context = {
        "title": "Contact Us",
        "breadcrumb_list": breadcrumb_list,
    }
    return render(request, "contact-us.html", context)


# this is faqs page view
def faqs(request):
    breadcrumb_list = ["faqs"]
    context = {
        "title": "frequently asked questions",
        "breadcrumb_list": breadcrumb_list,
    }
    return render(request, "faqs.html", context)
