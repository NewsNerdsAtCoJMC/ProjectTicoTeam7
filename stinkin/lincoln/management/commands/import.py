from django.core.management.base import BaseCommand, CommandError
import os, sys, csv
from datetime import date
from lincoln.models import Pothole
from django.template.defaultfilters import slugify
from dateutil import parser

class Command(BaseCommand):
	help = "Imports data for stinkin' lincoln project."

	def add_arguments(self, parser):
		parser.add_argument('file_location', nargs='+', type=str)

	def handle(self, *args, **options):
		for file in options['file_location']:
			try:
				reader = csv.reader(open(file, "r"), dialect=csv.excel)
			except IOError:
				raise CommandError('File %s does not exist' % file)
			next(reader)
			for row in reader:
				id = row[0]
				date = parser.parse(row[1])
				status = row[4]
				location = row[5]
				district = row[6]
				source = row[7]

				pothole, created = Pothole.objects.get_or_create(not_id=id, report_date=date, status=status, location=location, district=district, source=source)
				print(pothole.id)
