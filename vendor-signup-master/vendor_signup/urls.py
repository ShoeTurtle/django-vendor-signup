from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

	#Direct the user to the home page that shows the information about EmVito
	url(r'^$', 'vendor_signup.views.home', name='home'),
	url(r'^vendor/$', 'vendor_signup.views.home', name='home'),	

	#Landing page for the vendor to register projects
	url(r'^vendor\/(?P<vendor_id>\d+)/$', 'vendor_signup.views.register', name='register'),

	#Saving project data onto the database
	url(r'^vendor\/saveproject/$', 'vendor_signup.views.saveproject', name='saveproject')
)
