from django.shortcuts import render
# from testsite.utils.testsite.testpy import count
from django.http import HttpResponse
from .models import Question

# Create your views here.

testData = [{'user': 'Jogn M',
			 'post_date': 'April 28',
			 'post_content': 'this is the first post!'},
			{'user': 'Jo R',
			 'post_date': 'April 29',
			 'post_content': 'this is the Second post!'}]

def index(request):
	passedData = {'posts': testData}
	print (passedData)
	'''this is where you'd put any python code to do whatever things you want them to do. The info is retrieved from models.py Then pass the info as a dictionary into the return'''
	return render(request, 'testsite/testtemplate.html', passedData)

def link(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.question_text for q in latest_question_list])
	# return render(request, 'testsite/testlink.html', {'count': data})
	return HttpResponse('Hey!')