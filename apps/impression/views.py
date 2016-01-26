from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect # inserted this line

def index(request):
	print "I am definitely being hit."
  	return render(request, 'impression/index.html') # updated this line 

def submit(request):
	try:
		request.session['count'] += 1
	except:
		request.session['count'] = 1

	if request.method != 'POST':
		raise Http404('Only POSTs are allowed')
	if 'name' not in request.POST:
		raise Http404('Name not submitted')
	request.session['name'] = request.POST['name']
	request.session['language'] = request.POST['language']
	request.session['location'] = request.POST['location']
	request.session['comments'] = request.POST['comments']
	return redirect('/results')

def results(request):
	
	return render(request, 'impression/results.html')