from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from payment.models import NetBanking,bhimUPI,MobileBanking,Cradit
from Login.models import Login
from Billing_System.models import Generate_Bill as g
from Billing_System.models import Payment_Status as ps
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re
import django.utils.timezone as tz

# Create your views here.
def payment(request):
    return render(request,'payment.html')
def netbanking(request):
    context = {}
    
    user = request.user
    if request.method == 'POST':
            error_message = set([]);
            customer_no = request.POST['customerNo']
            bill_no = request.POST['billNo']
            bill_amount = request.POST['billAmount']
            bank_name = request.POST['bankName']
            branch_code = request.POST['branchCode']
            account_no = request.POST['accountNumber']
            date    = request.POST['date']

            bill = g.objects.filter(key_id=request.user.id).latest('bill_no')
            
            if not bank_name:
                error_message.add("Required Field Bank Name")
            elif not re.match('[a-zA-Z]',bank_name): 
                error_message.add("Invalid Bank name")
            if not branch_code:
                error_message.add("Required Field Branch Code")
            
            if not account_no:
                error_message.add("Required Field Account No")
            elif account_no.find("AC") == -1:
                error_message.add("Invalid Account no , it must start with AC")
            if not error_message:
                ins = NetBanking(customer_no = customer_no, bill_no = bill_no, bill_amount = bill_amount, bank_name = bank_name, branch_code = branch_code , account_no = account_no)
                ins.save()
                if ps.objects.filter(date=bill).exists():
                    p = ps.objects.get(date=bill)
                    p.status = True
                    p.detail = "Mode = Netbanking \nAC no ="+account_no+"\n Bank name ="+bank_name+"\n Branch code="+branch_code
                    p.save(update_fields=["status","detail"])
                else:
                    status = ps(key_id=user,date=bill,status=True,detail="Mode = Netbanking \nAC no ="+account_no+"\n Bank name ="+bank_name+"\n Branch code="+branch_code)
                    status.save()
                messages.success(request, 'Payment Successful')
                return redirect('login_home');
            else:
                context = {
                'customer_no': request.user.id,
                'meter_no': request.user.meter_no,
                'bill_no':bill_no,
                'amount':bill_amount,
                'error_message':error_message,
                }
                return render(request,'netbanking.html',context)
    else:
        if user.is_authenticated:
            customer_no = request.user.id
            meter_no = request.user.meter_no
            try:
                bill = g.objects.filter(key_id=customer_no).latest('bill_no')
                bill_no = bill.bill_no
                p = ps.objects.get(date=bill)
                if p.status:
                    messages.success(request, 'Payment is already Done')
                    return redirect('login_home')

                amount = bill.amount
                date = bill.month
            except g.DoesNotExist:
                messages.success(request, 'There are no bill generated so first generate bill')
                return redirect('generate_bill')
            context = {
                'customer_no': request.user.id,
                'meter_no': request.user.meter_no,
                'bill_no':bill_no,
                'amount':amount,
                'date' : date,
             }
            return render(request,'netbanking.html',context)
        else:
            return redirect('login');

def mobilebanking(request):
    context = {}
    
    user = request.user
    if request.method == 'POST':
        error_message = set([]);
        customer_no = request.POST['customerNo']
        bill_no = request.POST['billNo']
        bill_amount = request.POST['billAmount']
        mobile_no = request.POST['mobileNumber']
        ssn = request.POST['ssn']
        date    = request.POST['date']

        bill = g.objects.filter(key_id=request.user.id).latest('bill_no')
        
        if not mobile_no:
            error_message.add("Require Field Phone number")
        elif not re.match(r'^\d{9,13}$',mobile_no):
            error_message.add("Phone number must be entered in the format: '999999999'. Up to 13 digits allowed.")
        
        if not ssn:
            error_message.add("Require Field SSN")
        elif not re.match(r'^[0-9]',ssn) or len(ssn)!=9:
            error_message.add("Invalid SSN,It must be 9 digit number")
        if not error_message:
            ins = MobileBanking(customer_no = customer_no, bill_no = bill_no, bill_amount = bill_amount, mobile_no = mobile_no, ssn = ssn)
            ins.save()
            if ps.objects.filter(date=bill).exists():
                    p = ps.objects.get(date=bill)
                    p.status = True
                    p.detail = "Mode = Mobilebanking \nMobile no ="+mobile_no
                    p.save(update_fields=["status","detail"])
            else:
                status = ps(key_id=user,date=bill,status=True,detail="Mode = Mobilebanking \nMobile no ="+mobile_no)
                status.save()
            messages.success(request, 'Payment Successful')
            return redirect('login_home')
        else:
            context = {
                'customer_no': request.user.id,
                'meter_no': request.user.meter_no,
                'bill_no':bill_no,
                'amount':bill_amount,
                'error_message':error_message,
                'date' : date,
                }
            return render(request,'mobilebanking.html',context)
    else:
        if user.is_authenticated:
            customer_no = request.user.id
            meter_no = request.user.meter_no
            try:
                bill = g.objects.filter(key_id=customer_no).latest('bill_no')
                bill_no = bill.bill_no
                p = ps.objects.get(date=bill)
                if p.status:
                    messages.success(request, 'Payment is already Done')
                    return redirect('login_home')
                amount = bill.amount
                date = bill.month
            except g.DoesNotExist:
                messages.success(request, 'There are no bill generated so first generate bill')
                return redirect('generate_bill')
            amount = bill.amount
            context = {
                'customer_no': request.user.id,
                'meter_no': request.user.meter_no,
                'bill_no':bill_no,
                'amount':amount,
                'date' : date,
            }
            return render(request,'mobilebanking.html',context)
        else:
            return redirect('login');

def bhim(request):
    context = {}
    
    user = request.user
    if request.method == 'POST':
        error_message = set([]);
        customer_no = request.POST['customerNo']
        meter_no = request.POST['meterNo']
        bill_no = request.POST['billNo']
        bill_amount = request.POST['billAmount']
        upi_id = request.POST['UPI_ID']
        date    = request.POST['date']

        bill = g.objects.filter(key_id=request.user.id).latest('bill_no')
        
        if not upi_id:
            error_message.add("Required Field UPI ID")
        elif upi_id.find("@upi") == -1 and upi_id.find("@bhim") == -1:
            error_message.add("Invalid UPI ID")
        if not error_message:
            ins = bhimUPI(customer_no = customer_no, bill_no = bill_no, bill_amount = bill_amount, upi_id = upi_id)
            ins.save()
            if ps.objects.filter(date=bill).exists():
                    p = ps.objects.get(date=bill)
                    p.status = True
                    p.detail = "Mode = Bhim \nUpi id ="+upi_id
                    p.save(update_fields=["status","detail"])
            else:
                status = ps(key_id=user,date=bill,status=True,detail="Mode = Bhim \nUpi id ="+upi_id)
                status.save()
            
            messages.success(request, 'Payment Successful')
            return redirect('login_home');
        else:
                context = {
                'customer_no': request.user.id,
                'meter_no': request.user.meter_no,
                'bill_no':bill_no,
                'amount':bill_amount,
                'error_message':error_message,
                'date' : date,
                }
                return render(request,'bhim.html',context)
    else:
        if user.is_authenticated:
            customer_no = request.user.id
            meter_no = request.user.meter_no
            try:
                bill = g.objects.filter(key_id=customer_no).latest('bill_no')
                bill_no = bill.bill_no
                p = ps.objects.get(date=bill)
                if p.status:
                    messages.success(request, 'Payment is already Done')
                    return redirect('login_home')
                amount = bill.amount
                date = bill.month
            except g.DoesNotExist:
                messages.success(request, 'There are no bill generated so first generate bill')
                return redirect('generate_bill')
            amount = bill.amount
            context = {
                'customer_no': request.user.id,
                'meter_no': request.user.meter_no,
                'bill_no':bill_no,
                'amount':amount,
                'date' : date,
            }
            return render(request,'bhim.html',context)
        else:
            return redirect('login');
def cradit(request):
    context = {}
    
    user = request.user
    if request.method == 'POST':
        error_message = set([]);
        customer_no = request.POST['customerNo']
        bill_no = request.POST['billNo']
        bill_amount = request.POST['billAmount']
        card_number = request.POST['cardNumber']
        cvv = request.POST['cvv']
        expiry_date = request.POST['expiryDate']
        date = request.POST['date']

        bill = g.objects.filter(key_id=request.user.id).latest('bill_no')
        
        if not card_number:
            error_message.add("Required Field Card No")
        elif not card_number.isalnum() or len(card_number)!=12:
            error_message.add("Invalid Card Number. It must have 12 numbers")
        
        if not cvv:
            error_message.add("Required Field CVV")
        elif not cvv.isalnum() or len(cvv)<3:
            error_message.add("Invalid CVV. It must have minimum 3 digit number")
            
        if not expiry_date:
            error_message.add("Required Field Expiry Date")
        elif re.match(r'^d(0-12)/d(0-99)$',expiry_date):
            error_message.add("Invalid Expiry Date. It must be in MM/YY Formate")
        elif int(expiry_date[2:5]) < int(str(tz.now().year)[2:4]):
            error_message.add("Your cart was already expired")
        if not error_message:
            ins = Cradit(customer_no = customer_no, bill_no = bill_no, bill_amount = bill_amount, card_number = card_number, cvv = cvv, expiry_date = expiry_date)
            ins.save()
            if ps.objects.filter(date=bill).exists():
                    p = ps.objects.get(date=bill)
                    p.status = True
                    p.detail = "Mode = Debit/Credit Card \nCard no ="+card_number
                    p.save(update_fields=["status","detail"])
            else:
                status = ps(key_id=user,date=bill,status=True,detail="Mode = Debit/Credit Card \nCard no ="+card_number)
                status.save()
            
            messages.success(request, 'Payment Successful')
            return redirect('login_home')
        else:
            context = {
                'customer_no': request.user.id,
                'meter_no': request.user.meter_no,
                'bill_no':bill_no,
                'amount':bill_amount,
                'error_message':error_message,
                'date' : date
                }
            return render(request,'cradit.html',context)
    else:
        if user.is_authenticated:
            customer_no = request.user.id
            meter_no = request.user.meter_no
            try:
                bill = g.objects.filter(key_id=customer_no).latest('bill_no')
                bill_no = bill.bill_no
                p = ps.objects.get(date=bill)
                if p.status:
                    messages.success(request, 'Payment is already Done')
                    return redirect('login_home')
                amount = bill.amount
                date = bill.month
            except g.DoesNotExist:
                messages.success(request, 'There are no bill generated so first generate bill')
                return redirect('generate_bill')
            amount = bill.amount
            
            context = {
                'customer_no': request.user.id,
                'meter_no': request.user.meter_no,
                'bill_no':bill_no,
                'amount':amount,
                'date' : date
            }
            return render(request,'cradit.html',context)
        else:
            return redirect('login');