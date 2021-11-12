from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .forms import CustomerRegistrationForm
from django.contrib import messages

#def home(request):
 #return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topweare = Product.objects.filter(category='TW')
        bottomweare = Product.objects.filter(category='BW')
        mobile = Product.objects.filter(category='M')
        return render(request, 'app/home.html' , {'bottomweare': bottomweare,'topweare':topweare,'mobile':mobile})


#def product_detail(request):
# return render(request, 'app/productdetail.html')

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'product':product})


def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def mobile(request, data=None):
    if data==None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'Huawei' or data == 'Samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'Below':
        mobiles = Product.objects.filter(category='M').filter(discount_price__lt=23000)
    elif data == 'Above':
        mobiles = Product.objects.filter(category='M').filter(discount_price__gt=23000)
    return render(request, 'app/mobile.html', {'mobiles':mobiles})



# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congractulation!! Registration SuccessFul')
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})
    

def checkout(request):
 return render(request, 'app/checkout.html')
