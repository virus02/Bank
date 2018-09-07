import requests
from django.shortcuts import render,redirect
from .models import bank,b_city
from .forms import bankForm,b_cityForm

def list(request):
    banks=bank.objects.all()
    return render(request,'app/list.html',{'banks':banks})

def index(request):
    form=bankForm(request.POST or None)  
    #ifsc_code='CNRB0000653'
    #url='https://ifsc.firstatom.org/key/463r7Sx1h135x4u347sWfX6HN/ifsc/CNRB0000653'
    if form.is_valid():
       form.save()
       return redirect('list')
    
    return render(request,'app/ifse.html',{'form':form})

def branch(request,id):

    ifsc=bank.objects.get(id=id)

    url='http://www.ifschub.in/devapi/?ifsc={}'
    
    r=requests.get(url.format(ifsc)).json()
    bank_i= {
            "ifsc":r['success']['ifsc'],
            "branch":r['success']['branch'],
            "address":r['success']['address'],
            "contact":r['success']['contact'],
            "district":r['success']['district'],
            "state":r['success']['state'],
    }
    context={'bank_i':bank_i}
    return render(request,'app/branch.html',context,{'ifsc':ifsc})

def blist(request):
    b=b_city.objects.all()
    return render(request,'app/blist.html',{'b':b})

def dash(request):
    form=b_cityForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blist')
    
    return render(request,'app/dash.html',{'form':form})

def city(request,id):
    city=b_city.objects.get(id=id)

    url='http://www.ifschub.in/devapi/?city={}'

    r=requests.get(url.format(city)).json()

    city_c={
        "branch":r['success']['branch'],
    }
    context={'city_c':city_c}
    return render(request,'app/city.html',context,{'city':city})