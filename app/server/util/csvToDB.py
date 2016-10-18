#######
# Reads a CSV list of emails and puts them in database
#
import os, sys
sys.path.append("/home/ubuntu/note_2/app")
os.environ['DJANGO_SETTINGS_MODULE'] = 'server.settings.sites.bmshow'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


import re
import csv
import argparse

from django.contrib.sites.models import Site

from server.models import Subscriber


# Initialize argparsers
parser = argparse.ArgumentParser(description='Takes a CSV containing emails and put them in database as subscribers.')

parser.add_argument('-s', '--site', help='Specify the site to add subscribers to.')
parser.add_argument('-f', '--file', help='Specify the CSV file to read from.')

args = parser.parse_args()

# Get site from CLI arg
if args.site:
	if args.site == "bmshow":
		site = Site.objects.get(domain="benandmoreyshow.com")
	elif args.site == "nashvillenote" or args.site == "nashnote":
		site = Site.objects.get(domain="thenashvillenote.com")
else:
	print "ERROR: Must specify a site to add subscriber list to."
	exit()

# Get CSV from CLI arg
if args.file:
	i = 1
	EMAIL_PATTERN = re.compile('([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)')

	with open(args.file, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in reader:
			row = ' '.join(row)
			email = re.findall(EMAIL_PATTERN, row)
			
			subscriber = Subscriber(website=site, email=email[0][0])
			subscriber.save()
			
			
else:
	print "ERROR: Must specify a file to read."
	exit()
	
exit()
