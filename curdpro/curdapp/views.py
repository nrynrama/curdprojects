from django.shortcuts import render
from .models import ProductData
from .forms import ProductForm,UpdateForm,DeleteForm
from django.http.response import HttpResponse

def homeview(request):
    return render(request,'curdhome.html')

def inserting(request):
    if request.method =="POST":
        pform = ProductForm(request.POST)
        if pform.is_valid():
            pid = request.POST.get('product_id','')
            pname = request.POST.get('product_name','')
            pcost = request.POST.get('product_cost','')
            pcolor = request.POST.get('product_color','')
            pclass = request.POST.get('product_class','')
            nprods  = request.POST.get('number_of_products','')
            cname = request.POST.get('customer_name','')
            mobile = request.POST.get('mobile_number','')
            email = request.POST.get('email','')

            data = ProductData(
                product_id=pid,
                product_name=pname,
                product_cost=pcost,
                product_color=pcolor,
                product_class=pclass,
                number_of_products=nprods,
                customer_name=cname,
                mobile_number=mobile,
                email=email
            )
            data.save()
            pform = ProductForm()
            return render(request,'curdinserting.html',{'pform':pform})
    else:
        pform = ProductForm()
        return render(request,'curdinserting.html',{'pform':pform})


def retrieving(request):
    data = ProductData.objects.all()
    return render(request,'curdretrieving.html',{'data':data})


def updating(request):
    if request.method =="POST":
        uform = UpdateForm(request.POST)
        if uform.is_valid():
            pid = request.POST.get('product_id','')
            pcost = request.POST.get('product_cost','')
            prod_id = ProductData.objects.filter(product_id=pid)
            if not prod_id:
                return HttpResponse("<h1>Data Is Not Avilable</h1>")
            else:
                prod_id.update(product_cost = pcost)
                uform = UpdateForm()
                return render(request,'curdupdating.html',{'uform':uform})
        else:
            return HttpResponse("Invalid Form")
    else:
        uform = UpdateForm()
        return render(request,'curdupdating.html',{'uform':uform})

def deleting(request):
    if request.method == "POST":
        dform = DeleteForm(request.POST)
        if dform.is_valid():
            pid = request.POST.get('product_id','')
            prod_id = ProductData.objects.filter(product_id=pid)
            if not prod_id:
                return HttpResponse("<h1>Data Is Not Available</h1>")
            else:
                prod_id.delete()
                dform = DeleteForm()
                return render(request,'curddeleting.html',{'dform':dform})
        else:
            return HttpResponse("Form Is Invalid")
    else:
        dform = DeleteForm()
        return render(request,'curddeleting.html',{'dform':dform})















