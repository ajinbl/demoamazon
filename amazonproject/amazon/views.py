from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from amazon.forms import ProductForm
from amazon.models import Product


def index(request):
    obj = Product.objects.all()
    return render(request,'index.html',{'product':obj})

def detail(request,id):
    obj = Product.objects.get(id=id)
    return render(request,'detail.html',{'product':obj})
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        mrp = request.POST.get('mrp',)
        price = request.POST.get('price',)
        image = request.FILES['image']
        product = Product(name=name,desc=desc,mrp=mrp,price=price,image=image)
        product.save()
    return render(request,'add.html')

def update(request,id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None,request.FILES,instance=product)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'update.html',{'form':form,'product':product})

def delete(request,id):
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('/')

    return render(request,'delete.html')