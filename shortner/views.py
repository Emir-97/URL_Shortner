from django.shortcuts import render, redirect
from .models import Url
import uuid
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'index.html')

def create(request):
	if request.method == 'POST':
		link = request.POST['link']
		if("http://" not in link) and ("https://" not in link):
			link = "http://" + link
		uid = str(uuid.uuid4())[:5]
		new_url = Url(link=link, uuid=uid)
		new_url.save()
		return HttpResponse(uid)

def website(request, id):
    url_details = Url.objects.get(uuid=id)
    return redirect(url_details.link)
