from django.contrib import admin
from .models import covid_story


class CovidAdmin(admin.ModelAdmin): 
	pass 

admin.site.register(covid_story, CovidAdmin)