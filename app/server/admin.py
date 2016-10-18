import string
import random
import datetime

from models import *

from threading import Thread

from django.contrib import admin


class SiteInfoAdmin(admin.ModelAdmin):
	list_filter =  ('name',)
	fieldsets = (
		(
			'Basic Info',
			{
				'fields': ('name','description','prompt')
			}
		),
		(
			'Visual Components',
			{
				'fields': ('logo','background','background_image')
			}
		),
		(
			'Contact Info',
			{
				'fields': ('twitter','facebook','instagram','youtube','email')
			}
		),
		(
			'Open Graph Components',
			{
				'fields': ('ogimg','ogtitle','ogdescription')
			}
		),
		(
			'Advanced',
			{
            	'classes': ('collapse',),
				'fields': ('website','gatracking')
			}
		),
	)


def email_newsletter(modeladmin, requst, queryset):
	emails = list(queryset)
	
	for email in emails:
		tr = Thread(target=email.sendEmail)
		tr.start()
email_newsletter.short_description = "Send newsletter"

def email_newsletter_to_remaining(modeladmin, requst, queryset):
	emails = list(queryset)
	
	for email in emails:
		tr = Thread(target=email.sendEmail, args=(False,True,))
		tr.start()
email_newsletter.short_description = "Send newsletter to those that haven't received it yet"

def email_test_newsletter(modeladmin, requst, queryset):
	emails = list(queryset)
	
	for email in emails:
		tr = Thread(target=email.sendEmail, args=(True,False,))
		tr.start()
email_test_newsletter.short_description = "Send newsletter to testers"


class AuthorAdmin(admin.ModelAdmin):
	fields = ('name','bio','img','twitter','facebook','instagram','linkedin','contact_email',)
	
	def save_model(self, request, obj, form, change):
		if not obj.id:
			obj.created_at = datetime.date.today()
				
		obj.updated_at = datetime.datetime.today()
		super(AuthorAdmin, self).save_model(request, obj, form, change)

class EmailNoteAdmin(admin.ModelAdmin):
	fields = ('content','tags','category',)
	


class EmailNoteInline(admin.TabularInline):
	model = EmailNote
	extra = 1
	max_num = 20
	
	

class EmailAdmin(admin.ModelAdmin):
	list_filter = ('website',)
	list_display = ['id', 'subject','get_recipient_count','get_open_rate','sent']
	fields = ('subject','header','introimg','author','website',)
	actions = [email_newsletter, email_test_newsletter, email_newsletter_to_remaining]
	inlines = [EmailNoteInline]
	
	def save_model(self, request, obj, form, change):
		if not obj.id:
			obj.created_at = datetime.date.today()
			
			obj.hash_name = ""
			for x in range(0, 20):
				obj.hash_name += random.choice(string.letters)
				
		obj.updated_at = datetime.datetime.today()
		super(EmailAdmin, self).save_model(request, obj, form, change)
		
	def get_recipient_count(self, obj):
		sent = EmailLog.objects.filter(email=obj, subscriber__is_test=False).count()
		if sent == 0:
			return "N/A"
		return sent
	get_recipient_count.short_description = 'Recipients'
		
	def get_open_rate(self, obj):
		opened = EmailLog.objects.filter(email=obj, opened_at__isnull=False, subscriber__is_test=False).count()
		sent = EmailLog.objects.filter(email=obj, subscriber__is_test=False).count()
		
		if sent == 0:
			return "N/A"
			
		if opened == 0:
			return "0%"
		
		return str(round((float(opened) / float(sent)) * 100, 2)) + "%"
	get_open_rate.short_description = 'Open Rate'


class SubAdmin(admin.ModelAdmin):
	list_filter = ('website','is_test',)
	list_display = ['email','get_received_count','get_open_rate','website',]
	fields = ('email','website','is_test')

	def get_received_count(self, obj):
		received = EmailLog.objects.filter(subscriber=obj).count()
		return received
	get_received_count.short_description = 'Received'

	def get_open_rate(self, obj):
		received = EmailLog.objects.filter(subscriber=obj).count()
		opened = EmailLog.objects.filter(subscriber=obj, opened_at__isnull=False).count()
		
		if received == 0 or opened == 0:
			return "0%"
		
		return str(round((float(opened) / float(received)) * 100, 2)) + "%"
	get_open_rate.short_description = 'Open Rate'


class EmailLogsAdmin(admin.ModelAdmin):
	list_filter = ('email', 'subscriber',)
	list_display = ['email','subscriber','sent_at','opened_at',]
	fields = ('email','subscriber','stats','sent_at','opened_at',)
	
admin.site.register(Email,EmailAdmin)
admin.site.register(EmailLog,EmailLogsAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Subscriber,SubAdmin)
admin.site.register(SiteInfo,SiteInfoAdmin)