from django.shortcuts import render,redirect
from .models import AddImage
import os

# Create your views here.
def addProduct(request):
    return render(request,'addProduct.html')

def addToDb(request):
    if request.method=='POST':
        Pro=request.POST['PName']
        Pri=request.POST['PPrice']
        Qua=request.POST['PQuantity']
        Img=request.FILES.get('file')
        pdt=AddImage(Product=Pro,Price=Pri,Quantity=Qua,Image=Img)
        print("Save data..")
        pdt.save()
        return redirect(table)
    
def table(request):
    products=AddImage.objects.all()
    return render(request,'table.html',{'products':products})

def edit(request,pk):
    products=AddImage.objects.get(id=pk)
    return render(request,'edit.html',{'products':products})

def EditProduct(request,pk):
    if request.method=='POST':
        products=AddImage.objects.get(id=pk)
        products.Product=request.POST.get('PName')
        products.Price=request.POST.get('PPrice')
        products.Quantity=request.POST.get('PQuantity')
        if len(request.FILES)!=0:
            if len(products.Image)>0:
                os.remove(products.Image.path)
            products.Image=request.FILES.get('file')
        products.save()
        return redirect('table')
    return render(request,'edit.html')

def delete(request,pk):
    p=AddImage.objects.get(id=pk)
    p.delete()
    return redirect('table')

