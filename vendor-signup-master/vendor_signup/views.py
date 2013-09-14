from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.utils import simplejson as json

from vendor_signup.models import Vendor,Project


def home(request):
	template = loader.get_template('home.html')
	context = RequestContext(request, {})

	return HttpResponse(template.render(context))	
	
	
def register(request, vendor_id):
	
	#1. Query the vendor name from the vendor id
	#2. Create Context and pass it over to the view
	
	#Saving the vendor_id into a session variable
	request.session['vendor_id'] = vendor_id
	vendorObj = get_object_or_404(Vendor, pk=vendor_id)

	template = loader.get_template('home.html')
	context = RequestContext(request, {
		'vendor_id': vendor_id,
		'vendor_email': vendorObj.vendor_email,
		'vendor_title': vendorObj.vendor_title
	})

	return HttpResponse(template.render(context))
	
	
def saveproject(request):

	project_data = json.loads(request.GET.get('project_data'))	
	v_id = request.session['vendor_id']

	for val in project_data:
		Project(vendor_id=v_id, project_title=val['title'], project_url=val['url']).save()
			
	return HttpResponse("OK")

	