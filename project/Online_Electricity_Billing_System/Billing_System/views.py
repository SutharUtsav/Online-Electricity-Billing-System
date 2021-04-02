from django.shortcuts import render,redirect,get_object_or_404
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import login,authenticate,logout
from django.template.context_processors import csrf
from Login.models import Login as L
from django.contrib import messages
from Billing_System.models import Generate_Bill as g
from Billing_System.models import Payment_Status as ps
from Login.forms import registrationForm,LoginAuthenticationForm,AccountUpdateForm



#initialization 
cost_per_unit = 4 

# Create your views here.
def Registration_view (request):
    context = {}
    if request.POST:
        form    =registrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            Phone_number = form.cleaned_data.get('Phone_number')
            meter_no = form.cleaned_data.get('meter_no')
            account = authenticate(email=email,password=password)
            auth.login(request,account)
            return redirect('login_home')
        else:
            context['registration_form']=form
    else:#GET request
        form = registrationForm()
        context['registration_form']=form 
    return render(request,"register.html",context)

    
def login_view(request):
    context={}

    user = request.user
    if user.is_authenticated:
        return redirect("login_home")
    if request.POST:
        form = LoginAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user  = authenticate(email=email,password=password)

            if user:
                auth.login(request,user)
                return redirect("login_home")
    else :
        form = LoginAuthenticationForm()

    context['login_form'] = form
    return render(request,'Billing_System/login.html',context)

def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            initial={
                        "email" : request.POST['email'],
                        "username" : request.POST['username'],
                        "Phone_number":request.POST['Phone_number'],
                        "meter_no"     :request.POST['meter_no']
                    }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(
                    initial={
                        "email" : request.user.email,
                        "username" : request.user.username,
                        "Phone_number":request.user.Phone_number,
                        "meter_no" : request.user.meter_no

                    }
                )
    context['account_form'] = form 
    return render(request,"Billing_System/account.html",context)
  
def home_screen_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("login")

    logins = L.objects.all()
    context['logins'] = logins

    return render(request,"home.html",context)
def view_bill(request):
    return render(request,'view_bill.html')

def generate_bill(request):
    context = {}
    
    user = request.user
    if request.method == 'POST':
        bill_no = request.POST['bill_no']
        try:
            unit  = request.POST['unit']
            if float(unit) > 100 :
                amount = float(unit) * 2 * cost_per_unit #float(request.session['cost_per_unit']) #double amount
            else:
                amount = float(unit) * cost_per_unit #float(request.session['cost_per_unit'])     
            gb = g( bill_no=bill_no,amount=amount,unit=unit,key= L.objects.get(pk=request.user.id))
            gb.save()
            status = ps(key_id=user,date=gb,status=False)
            status.save()
            
            messages.success(request, 'Bill Generated Now please pay the bill')
            return redirect('view_bill');
        except:
            messages.success(request, 'Invalid Unit unit can not more than 1250')
            return redirect('view_bill');
    else:
        if user.is_authenticated:
            try:
                bill = g.objects.latest('key')
                bill_no = bill.id+1
            except g.DoesNotExist:
                bill_no = 1
            context = {
                'meter_no' : request.user.meter_no,
                'bill_no'  : bill_no,
                'username' : request.user.username,
            }  
            return render(request,'generate_bill.html',context)
        else:
            return redirect('login');
def utility(request):
    return render(request,"utility.html",{})
def calculate(request):
    context = {}
    
    user = request.user
    if request.method == 'POST':
        unit  = request.POST['unit']
        if float(unit) > 100 :
            amount = float(unit) * 2 * cost_per_unit #float(request.session['cost_per_unit']) #double amount
        else:
            amount = float(unit) * cost_per_unit #float(request.session['cost_per_unit'])     
        context = {
            'unit' : unit,
            'amount' : amount, 
        }
        return render(request,'display.html',context)
    else:
        if user.is_authenticated: 
            return render(request,'calculate.html',{})
        else:
            return redirect('login');
def check_status(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        context = {
        'pay' : ps.objects.all(),
        'id' : request.user.id,

        }
        return render(request,"check_status.html",context)
    else:
        return render(request,"index.html",{}) 

def status_pdf_view(request,*args,**kwargs):
    pk = kwargs.get('pk')
    bill = get_object_or_404(ps,pk=pk)
    template_path = "pdf/pdf1.html"
    context = {
    "bill" : bill,
    "pk" : pk,
    "bill":bill,}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Bill.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    #create pdf
    pisa_status = pisa.CreatePDF(
                        html,dest=response)
    if pisa_status.err:
        return HttpResponse('we had some error <pre>'+html+'</pre>')
    return response
def status_pdf_download(request,*args,**kwargs):
    pk = kwargs.get('pk')
    bill = get_object_or_404(ps,pk=pk)
    template_path = "pdf/pdf1.html"
    context = {"bill" : bill}
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'attachment; filename="Bill.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    #create pdf
    pisa_status = pisa.CreatePDF(
                        html,dest=response)
    if pisa_status.err:
        return HttpResponse('we had some error <pre>'+html+'</pre>')
    return response

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/Billing_System/login_view/')


#by utsav
def index(request):
    return render(request,'index.html')
    
def home(request):
    if request.user.is_authenticated:

        return render(request,'home.html')
    else:
        return render(request,"index.html")

