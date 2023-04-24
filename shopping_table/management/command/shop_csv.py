import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import django


from shopping_table.models import Alcohol


class Command(BaseCommand):
    help = 'Load data from csv'


    def handle(self, *args, **options):
        apps.check_apps_ready()
        # drop the data from the table so that if we rerun the file, we don't repeat values
        Alcohol.objects.all().delete()
        print("table dropped successfully")

        # open the file to read it into the database
        beer_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(beer_dir)+'/disaster_table/ShoppingSource/Product_range.csv', newline='') as f:
            reader =csv.reader(f, delimiter=",")
            next(reader)
            # skip the header line

            for row in reader:
                print(row)
                product_object = Alcohol.objects.create(

                    product_name=row[3],
                    product_id=row[1],
                    product_country=row[6],
                    product_price=row[4],
                    product_size=row[7],
                    product_ABV=row[8]
                )
                product_object.save()
                print("data parsed successfully")
