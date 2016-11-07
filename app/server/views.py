VERSION = 'v1'

import datetime

from forecastiopy import *

from server.models import *

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.core.validators import validate_email
from django.core.validators import ValidationError
from django.contrib.sites.models import Site

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

def index(request):
	archive = []
	site = Site.objects.get_current()
	siteInfo = SiteInfo.objects.get(website=site)
	
	if site.domain == "thenashvillenote.com":
		archive = Email.objects.filter(website=site, sent=True).order_by('-created_at')
		current = archive[0]
		archive = archive[1:]
		
		fio = ForecastIO.ForecastIO(settings.DS_API_KEY, latitude=settings.NASHVILLE[0], longitude=settings.NASHVILLE[1])
		todaily = FIODaily.FIODaily(fio)
		
		today = datetime.datetime.now()
		weather = {
			"summary": todaily.summary,
			"days": []
		}
		for i in xrange(0, 5):
			dateString = today.strftime("%a %-m/%-d")
			day = todaily.get_day(i)
			weather['days'].append({
				"dow":	dateString,
				"icon": day["icon"],
				"high":	int(round(day["apparentTemperatureMax"])),
				"low":	int(round(day["apparentTemperatureMin"]))
			})
			today = today + datetime.timedelta(days=1)
		
		content = {
			"weather":	weather,
			"intro": 	EmailNote.objects.filter(email=current.id, category=1),
			"briefs": 	EmailNote.objects.filter(email=current.id, category=2),
			"beats": 	EmailNote.objects.filter(email=current.id, category=3),
			"quotes":	EmailNote.objects.filter(email=current.id, category=5),
		}
		
		setattr(current, "content", content)
		return render(request, "nashnote/index.html", {'site': siteInfo, 'current': current, 'archive': archive})
	
	return render(request, "index.html", {'site': siteInfo, 'archive': archive})
	

def issue_view(request, id):
	site = Site.objects.get_current()
	siteInfo = SiteInfo.objects.get(website=site)
	
	if site.domain == "thenashvillenote.com":
		current = Email.objects.get(id=id)
	
		archive = Email.objects.filter(website=site).order_by('-created_at')
		
		content = {
			"intro": 	EmailNote.objects.filter(email=current.id, category=1),
			"briefs": 	EmailNote.objects.filter(email=current.id, category=2),
			"beats": 	EmailNote.objects.filter(email=current.id, category=3),
			"quotes":	EmailNote.objects.filter(email=current.id, category=5),
		}
		
		setattr(current, "content", content)
		return render(request, "nashnote/issue.html", {'site': siteInfo, 'current': current, 'archive': archive})
	
	return render(request, "index.html", {'site': siteInfo, 'archive': []})

@api_view(['POST'])
def list_subscribe(request):
	ip = request.META.get('REMOTE_ADDR')
	email = request.POST['email']
	ref = request.POST.get('ref', False)
	site = Site.objects.get_current()

	if email == None:
		return Response({"msg": "no_email"}, status=status.HTTP_400_BAD_REQUEST)

	try:
		validate_email(email)
	except ValidationError:
		return Response({"msg": "bad_email"}, status=status.HTTP_400_BAD_REQUEST)

	users = Subscriber.objects.filter(email=email, website=site)
	if len(users) > 0:
		return Response({"msg": "user_exists"}, status=status.HTTP_409_CONFLICT)
	
	user = Subscriber(email=email, ip=ip, website=site)
	user.save()

	return Response()


@api_view(['GET'])
def list_unsubscribe(request, hash):
	try:
		sub = Subscriber.objects.get(hash_name=hash)
		email = sub.email
		sub.delete()
		print 'deleted '+email
	except:
		print 'no sub found with hash '+hash

	return HttpResponse("Successfully unsubscribed. Come back some time.")


@api_view(['GET'])
def track_open(request, hash, track_id):
		site = Site.objects.get_current()
		
		track_id = track_id.replace("=", "")
		track_id = track_id.replace("%3D", "")
	
		email = Email.objects.get(hash_name=hash)
		subscriber = Subscriber.objects.get(hash_name=track_id)

		if EmailLog.objects.filter(email=email, subscriber=subscriber, opened_at__isnull=True).count() > 0:
			try:
				log = EmailLog.objects.get(email=email, subscriber=subscriber)
				log.opened_at = datetime.datetime.now()
				log.save()
			except Exception:
				print 'already exists'

		image_data = open("/var/www/static/img/pixel.png", 'rb').read()
		return HttpResponse(image_data, content_type="image/png")
