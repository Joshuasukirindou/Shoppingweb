import csv
from decimal import Decimal
import decimal
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
        with open(str(beer_dir)+'/shopping_table/ShoppingSource/Product_range.csv', encoding='utf-8', newline='') as f:
            reader =csv.reader(f, delimiter=",")
            next(reader)
            # skip the header line

            for row in reader:
                print(row)
                try:
                    product_object = Alcohol.objects.create(
                        product_id=row[0],
                        product_name=row[2],
                        product_price=int(float(row[3])) if row[3] else 0,
                        product_country=row[5],
                        product_size=Decimal(row[6]) if row[6] else Decimal('0'),
                        product_ABV=Decimal(row[7]) if row[7] else Decimal('0'),
                    )
                except decimal.InvalidOperation:
                    print(f"Failed to convert {row[6]} or {row[7]} to Decimal")
                    continue
                product_object.save()
                print("data parsed successfully")
