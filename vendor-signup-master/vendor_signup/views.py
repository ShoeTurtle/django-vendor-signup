from django.http import HttpResponse
from django.template import RequestContext, loader


def home(request):
	template = loader.get_template('home.html')
	context = RequestContext(request, {})

	return HttpResponse(template.render(context))	
	
	
def register(request, vendor_id):
	
	return HttpResponse('Vendor Registration For Id: %s' % vendor_id)