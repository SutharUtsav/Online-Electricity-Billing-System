from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
#for pdf
import os
from django.conf import settings
from xhtml2pdf import pisa
from django.template.loader import get_template
from Billing_System.models import Generate_Bill
from django.views.generic import ListView

def generate_bill_view(request):
	context = {}
	if request.user.is_authenticated:
		context = {
			'model' : Generate_Bill.objects.all(),
			'id' : request.user.id,
			}
		return render(request,"pdf/view.html",context)
	else:
		return render(request,"index.html",{}) 
def render_pdf_view(request,*args,**kwargs):
	pk = kwargs.get('pk')
	bill = get_object_or_404(Generate_Bill,pk=pk)
	template_path = "pdf/pdf2.html"
	context = {"bill" : bill}
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="Demo Bill.pdf"'

	template = get_template(template_path)
	html = template.render(context)

	#create pdf
	pisa_status = pisa.CreatePDF(
						html,dest=response)
	if pisa_status.err:
		return HttpResponse('we had some error <pre>'+html+'</pre>')
	return response
def render_pdf_download(request,*args,**kwargs):
	pk = kwargs.get('pk')
	bill = get_object_or_404(Generate_Bill,pk=pk)
	template_path = "pdf/pdf2.html"
	context = {"bill" : bill}
	response = HttpResponse(content_type='application/pdf')

	response['Content-Disposition'] = 'attachment; filename="Demo Bill"'+bill.key.username+'".pdf"'

	template = get_template(template_path)
	html = template.render(context)

	#create pdf
	pisa_status = pisa.CreatePDF(
						html,dest=response)
	if pisa_status.err:
		return HttpResponse('we had some error <pre>'+html+'</pre>')
	return response
def render_pdf_delete(request,*args,**kwargs):
	pk = kwargs.get('pk')
	try:
		bill = get_object_or_404(Generate_Bill,pk=pk).delete()
		context = {"bill" : bill}
		pk = kwargs.get('pk')
		messages.success(request, 'Bill Deleted')
		return render(request,"view_bill.html",context)
	except:
		messages.success(request, 'There Is no bill left')
		return render(request,"home.html",{})
	if pisa_status.err:
		return HttpResponse('we had some error <pre>'+html+'</pre>')
	return response