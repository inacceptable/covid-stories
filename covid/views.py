from django.shortcuts import render
from django.http import HttpResponse 
from .models import covid_story 
from django.core.paginator import Paginator
import re
from django.db.models import Count
def valid_email(email):
  	return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def check_email_use(email): 
	count_array = covid_story.objects.filter(email=email)
	count = 0 
	count = len(count_array) 
	return count 

def home(request):
	covid_stories = covid_story.objects.order_by("-updated_at")[:4]
	count = covid_story.objects.all().count()
	page_name = 'home'
	context = {
		'covid_stories' : covid_stories,
		'count' : count,
		'page_name' : page_name,
	}
	return render(request, 'html/home.html', context)

def read_story(request):
	stories = covid_story.objects.all()  
	paginator = Paginator(stories, 6) 
	page_number = request.GET.get('page') 
	page_obj = paginator.get_page(page_number) 
	context = {
		'stories' : page_obj 
	} 
	return render(request, 'html/read_story.html', context)
def story(request): 
	test = request.GET['story']
	x = covid_story.objects.get(story_id=test) 
	page_name = "story?story=" + str(x.story_id)
	context = { 
		'story' : x,
		'page_name' : page_name, 
	}
	return render(request, 'html/story.html', context)

def submit_story(request):
	context = {} 
	if request.method == 'POST':
		story_subject = str(request.POST.get('title'))
		email_address = str(request.POST.get('email'))
		story_content = str(request.POST.get('content'))
		email_valid = valid_email(email_address)
		if email_valid == False:
			return render(request, 'html/feedback_not_confirmed.html')
		else:
			pass

	count_email = check_email_use(email_address)
	context = {
		'count_email' : count_email,
		'email_valid' : email_valid,
	} 
	if count_email > 3: 
		return render(request, 'html/email_used_alot.html', context) 
	else:
		pass


		
	new_post = covid_story(subject=story_subject, email=email_address, content=story_content)
	new_post.save() 
	return render(request, 'html/feedback_confirmation.html', context) 	
