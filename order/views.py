from django.shortcuts import render

# Create your views here.

def checkout(request):
    breadcrumb_list = ['cart','checkout']
    context = {
        'title':'Checkout Page',
        'breadcrumb_list':breadcrumb_list,
    }
    return render(request, 'orders/checkout.html',context)

