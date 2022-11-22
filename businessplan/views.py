from email import message
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,login,logout
from django.contrib import messages
from . models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            return render(request,'literacy.html')

        else:
            return redirect('login')
    return render(request, 'login.html')

def Aboutus(request):
    return render(request, 'aboutus.html') 
def Literacy(request):
    return render(request, 'literacy.html')     
    

def Business(request):
    if request.method == 'POST':
        businessname = request.POST['businessname']
        legalform = request.POST['legalform']
        fiveyearobjective = request.POST['fiveyearobjective']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        telephone = request.POST['telephone']
        email = request.POST['email']

        post = businessdetail(businessname=businessname,legalform=legalform,fiveyearobjective=fiveyearobjective,address=address,city=city,country=country,telephone=telephone,email=email)
        post.save()
        return redirect('resources')

    return render(request, '2.Business.html') 

def Resources(request):
        if request.method == 'POST':
            resource = request.POST['resource']
            proposedresource = request.POST['proposedresource']
            purchaseditem = request.POST['purchaseditem']
            post = resources(resource=resource,proposedresource=proposedresource,purchaseditem=purchaseditem).save()
            return redirect('personnel')
        return render(request, '3.resources.html')  


def Personnel(request):
    if request.method == 'POST':
        PER = personnel()
        PER.keyperson = request.POST['keyperson']
        PER.keypersonrole = request.POST['keypersonrole'] 
        PER.keypersonresponsibilities = request.POST['keypersonresponsibilities']
        PER.save()
        return redirect('market')
    return render(request, '4.personnel.html') 

def Market(request):
    if request.method == 'POST':
        Mkt = market()
        Mkt.productserviceoffer = request.POST['productserviceoffer']
        Mkt.targetcustomers = request.POST['targetcustomers'] 
        Mkt.geographicmarket = request.POST['geographicmarket']
        Mkt.competitiveadvantage = request.POST['competitiveadvantage']
        Mkt.save()
        return redirect('competitor')
    return render(request, '5.market.html')     
def Competitor(request):
    if request.method == 'POST':
        cmt = competitor()
        cmt.competitor = request.POST['competitor']
        cmt.competitorweakness = request.POST['competitorweakness'] 
        cmt.competitiveadvantages = request.POST['competitiveadvantages']
        cmt.save()
        return redirect('oportunity')
    return render(request, '6.competitor.html') 

def Oportunity(request):
    if request.method == 'POST':
        opt = opportunity()
        opt.opportunity = request.POST['opportunity']
        opt.save()
        return redirect('strategy')
    return render(request, '7.oportunity.html')  

def Strategy(request):
    if request.method == 'POST':
        str = strategy()
        str.strategicstep = request.POST['strategicstep']
        str.methodofselling = request.POST['methodofselling'] 
        str.advertising = request.POST['advertising']
        str.save()
        return redirect('finance')
    return render(request, '8.strategy.html')     
def Finance(request):
    return render(request, '9.finance.html')    

def Signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password1 =  request.POST['pass']
        confrim =request.POST['confirmpass']

        if password1==confrim:
            user = User.objects.create_user(username=username,email=email,password=password1)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "account created successfully")
            print('account have been  created successful')
        else:
            render('<script><h1 style="color"white";>alert("account created")</h1></script>')


    return render(request, 'signup.html') 