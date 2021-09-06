from django.db import models

class covid_story(models.Model): 
	story_id = models.AutoField(primary_key=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	subject = models.CharField(max_length = 200) 
	email = models.CharField(max_length=50)
	content = models.TextField()