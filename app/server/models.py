import re
import os
import string
import random
import datetime

import jsonfield

from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.template import loader, Context
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from django.db.models.signals import pre_save
from django.contrib.sites.models import Site

from tinymce.models import HTMLField

from taggit.managers import TaggableManager

import boto3
mail = boto3.client(
	'ses',
	region_name=settings.REGION,
	aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
)


class Author(models.Model):
	def __unicode__ (self):
		return self.name
		
	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField(editable=False)
	
	img = models.ImageField(upload_to='img/profile/')
	
	name = models.CharField(max_length=255)
	bio = models.TextField(default="A hero or a villain writing for The Nashville Note.", blank=False, help_text="Brief bio about author.")

	contact_email = models.EmailField(blank=False, default=None)

	twitter = models.URLField(blank=True)
	facebook = models.URLField(blank=True)
	linkedin = models.URLField(blank=True)
	instagram = models.URLField(blank=True)


		
def get_upload_path_logo(instance, filename):
	folder = ''.join(instance.name.split()).lower()
	return os.path.join(folder, "img", "logo", filename)

def get_upload_path_bg(instance, filename):
	folder = ''.join(instance.name.split()).lower()
	return os.path.join(folder, "img", "bg", filename)

def get_upload_path_og(instance, filename):
	folder = ''.join(instance.name.split()).lower()
	return os.path.join(folder, "img", "ogimg", filename)

class SiteInfo(models.Model):
	def __unicode__ (self):
		return self.name
	
	name = models.CharField(max_length=255, help_text="Name of site to be used as page's title, og:title and anywhere the title is requested.")
	description = models.TextField(blank=True, help_text="Description of site. Shown on signup splash pages.")
	prompt = models.CharField(max_length=500, default="", verbose_name="Signup Prompt", help_text="Text to be shown above email signup form.")
	
	gatracking = models.CharField(max_length=100, default="", blank=False, verbose_name="GA Tracking Code")
	
	ogimg = models.ImageField(upload_to=get_upload_path_og, default="", help_text="Image to be used for Open Graph crawls. Dimensions: 1200px x 630px", verbose_name="OG Image")
	ogtitle = models.CharField(blank=False, default="", max_length=255, help_text="Title to be displayed in OG crawls.", verbose_name="OG Title")
	ogdescription = models.CharField(max_length=512, default="", help_text="Description to be displayed in OG crawls.", verbose_name="OG Description")

	twitter = models.URLField(blank=True, verbose_name="Twitter URL")
	facebook = models.URLField(blank=True, verbose_name="Facebook URL")
	instagram = models.URLField(blank=True, verbose_name="Instagram URL")
	youtube = models.URLField(blank=True, verbose_name="YouTube URL")

	email = models.EmailField(help_text="Publicly displayed contact email.")

	logo = models.ImageField(upload_to=get_upload_path_logo)
	background = models.CharField(max_length=9,blank=True, help_text="Background color as HEX value.", verbose_name="Background Color")
	background_image = models.ImageField(upload_to=get_upload_path_bg, blank=True, help_text="Background image to be repeated as a tile.", verbose_name="Background Image")

	website = models.ForeignKey(Site, on_delete=models.CASCADE, default=None)
	



class Email(models.Model):
	def __unicode__ (self):
		return self.subject

	created_at = models.DateTimeField(editable=False)
	updated_at = models.DateTimeField(editable=False)

	subject = models.CharField(max_length=255)
	
	header = models.BooleanField(default=False, help_text="Show logo at top of email?")
	headline = models.CharField(max_length=255, blank=False, default=None)
	
	introimg = models.ImageField(upload_to='img/covers/', default=None, blank=True)
	introimgtext = models.CharField(max_length=512, default=None, blank=True)

	hash_name =  models.CharField(unique=True,max_length=255,blank=True,editable=False)
	
	sent = models.BooleanField(default=False)

	website = models.ForeignKey(Site, on_delete=models.CASCADE, default=None)
	
	author = models.ForeignKey(Author, default=1)
				
	
	
	def replaceLinks(subscriber, notes):
		for n in notes:
			n.content = re.sub(r'(?<=href=(\"|\'))([^\"\']+)(?=\"|\')', r'http://thenashvillenote.com/link/' + re.escape(subscriber.hash_name) + r'/' + re.escape(n.email.hash_name) + r'?url=\2', n.content)
		return notes
	
	
	def renderTemplate(self, email, site, info, sub, header=True):
		today = datetime.datetime.now()
		
		if site.domain == 'benandmoreyshow.com':
			prompt = 'Know someone who might like the show?'
		else:
			prompt = "Know someone who needs " + info.name
		
		if email.introimg:
			introimg = email.introimg.url
			introimgtext = email.introimgtext
		else:
			introimg = False
			introimgtext = ""
		
		header 	= self.header
		headline = self.headline
		intro 	= self.replaceLinks(sub, EmailNote.objects.filter(email=email, category=1))
		briefs 	= self.replaceLinks(sub, EmailNote.objects.filter(email=email, category=2))
		beats 	= self.replaceLinks(sub, EmailNote.objects.filter(email=email, category=3))
		events 	= self.replaceLinks(sub, EmailNote.objects.filter(email=email, category=6))
		
		pixelURL = 'http://' + site.domain + '/v1/' + email.hash_name + '/' + sub.hash_name
		pixelURL = pixelURL.replace("=", "")
		
		if site.domain == 'thenashvillenote.com':
			t = loader.get_template('email/nashnote/temp-v1.html')
		else:
			t = loader.get_template('email/temp-v1.html')
			
		c = Context({
			'header':	header,
			'headline': headline,
			'sub': 		sub, 
			'introimg':	introimg,
			'introimgtext': introimgtext,
			'intro':	intro,
			'site': 	site,
			'email': 	email,
			'briefs':	briefs,
			'events':	events,
			'beats':	beats,
			'siteInfo': info,
			'prompt':	prompt,
			'pixel': 	pixelURL
		})
		rendered = t.render(c)
		
		return rendered
		
		
	def sendEmail(self, tester=False, remaining=False):
		site = self.website
		siteInfo = SiteInfo.objects.get(website=site)

		if tester:
			subscribers = Subscriber.objects.filter(is_test=True, website=site)	
		elif remaining:
			subscribers = Subscriber.objects.filter(website=site)	
			received = EmailLog.objects.filter(email=self)
			removed = [ r.subscriber.id for r in received ]
			subscribers = subscribers.exlude(pk__in=removed)
		else:
			subscribers = Subscriber.objects.filter(website=site)		
			
		if site.domain == 'benandmoreyshow.com':
			subject = "This Week " + self.subject
		else:
			subject = self.subject
		
		if not tester:
			self.sent = True
		self.sent_at = datetime.datetime.now()
		self.save()

		for sub in subscribers:
			tempHTML = self.renderTemplate(self, site, siteInfo, sub)

			response = mail.send_email(
				Source='"' + siteInfo.name + '" <' + siteInfo.email + '>',
				Destination={
					'ToAddresses': [
						sub.email,
					]
				},
				Message={
					'Subject': {
						'Data': subject
					},
					'Body': {
						'Html': {
							'Data': tempHTML
						}
					}
				},
				ReplyToAddresses=[
					siteInfo.email,
				],
				ReturnPath=siteInfo.email
			)

			if response['ResponseMetadata']['HTTPStatusCode'] == 200:
				log = EmailLog(email=self, subscriber=sub, sent_at=datetime.datetime.now())
				log.save()
				


class EmailNote(models.Model):
	NOTE_TYPE = (
		(1, 'Intro'),
		(2, 'Brief'),
		(3, 'Beat'),
		(4, 'Poster'),
		(5, 'Quote'),
		(6, 'Event'),
	)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	content = HTMLField(default=None)
	subtitle = models.CharField(max_length=255, default="", blank=True)

	tags = TaggableManager(blank=True)
	
	email = models.ForeignKey(Email)
	
	category = models.IntegerField(choices=NOTE_TYPE)

	def save(self):
		if not self.id:
			self.created_at = datetime.date.today()
		super(EmailNote, self).save()



class EmailLink(models.Model):
	def __unicode__(self):
		return self.url
	
	url = models.URLField(verbose_name="Link URL", blank=False)
	
	email = models.ForeignKey(Email)
	


class Subscriber(models.Model):
	def __unicode__ (self):
		return self.email

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	email = models.EmailField(_('email address'),blank=True,null=True,unique=False)

	ip = models.CharField(max_length=255,blank=False,default="")
	hash_name = models.CharField(unique=True,max_length=255,blank=True,editable=False)
	
	is_test = models.BooleanField(default=False)

	website = models.ForeignKey(Site, on_delete=models.CASCADE, default=None)
	
	def save(self):
		if not self.id:
			self.created_at = datetime.date.today()
			
			self.hash_name = ""
			for x in range(0, 20):
				self.hash_name += random.choice(string.letters)
				
		self.updated_at = datetime.datetime.today()
		super(Subscriber, self).save()
	


class EmailLinkLog(models.Model):
	clicked_at = models.DateTimeField(blank=True)
	
	link = models.ForeignKey(EmailLink)
	subscriber = models.ForeignKey(Subscriber)
	
	def save(self, force_insert=False, force_update=False, using=None):
		if not self.id:
			self.clicked_at = datetime.datetime.today()
		super(EmailLinkLog, self).save()



class EmailLog(models.Model):

	sent_at = models.DateTimeField(blank=False)
	opened_at = models.DateTimeField(blank=True, null=True)

	email = models.ForeignKey(Email, blank=True)
	subscriber = models.ForeignKey(Subscriber, blank=True)
	stats = jsonfield.JSONField(blank=True)

	def save(self, force_insert=False, force_update=False, using=None):
		if not self.id:
			self.sent_at = datetime.datetime.today()
		super(EmailLog, self).save()
