from django.shortcuts import render, HttpResponse, redirect
from poll.models import Poll

# Create your views here.
def home(request):
	questions = Poll.objects.all()
	return render(request, "home.html", {"questions":questions})
	
def vote(request, poll_id):
	questions = Poll.objects.get(pk=poll_id)
	
	if request.method == "POST":
		selected_option = request.POST.get('type', None)
		
		if selected_option ==  'option1':
			questions.option1_count = questions.option1_count + 1
		elif selected_option == 'option2':
			questions.option2_count = questions.option2_count + 1
		elif selected_option == 'option3':
			questions.option3_count = questions.option3_count + 1
		else:
			print('None Selected')
	
		questions.save()

		#return render(request, "results.html", {"questions":questions})
		return redirect(f'/result/{poll_id}/')
		
	return render(request, "vote.html", {"questions":questions})
	
def result(request, poll_id):
	questions = Poll.objects.get(pk=poll_id)
	return render(request, "results.html", {"questions":questions})
