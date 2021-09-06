from django.shortcuts import render
from django.http import HttpResponse 
from .models import covid_story 
from django.core.paginator import Paginator
import re
from django.db.models import Count
def valid_email(email):
  	return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def check_email_use(email): 
	queryset = covid_story.objects.all().annotate(count = Count(email))
	return count 

def home(request):
	covid_stories = covid_story.objects.order_by("-updated_at")[:4]
	count = covid_story.objects.all().count()
	context = {
		'covid_stories' : covid_stories,
		'count' : count
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
	context = { 
		'story' : x,
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
		

	new_post = covid_story(subject=story_subject, email=email_address, content=story_content)
	new_post.save() 
	return render(request, 'html/feedback_confirmation.html', context) 