from django.db import models

# Create your models here.


#Vendor Model
class Vendor(models.Model):
	vendor_title = models.CharField(max_length=50)
	vendor_email = models.CharField(max_length=50)
	vendor_verified = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.vendor_title
	


#Project Model	
class Project(models.Model):
	vendor = models.ForeignKey(Vendor)
	project_title = models.CharField(max_length=200)
	project_url = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.project_title
	
		