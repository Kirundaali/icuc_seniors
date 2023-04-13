from django.shortcuts import render

# Create your views here.

def checkout(request):
    bradcrumb_list = ['cart','checkout']
    context = {
        'title':'Checkout Page',
        'bradcrumb_list':bradcrumb_list,
    }
    return render(request, 'orders/checkout.html',context)

