import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    # def handle(self, *args, **options):
    #     with open('work_with_database/phones.csv', 'r') as file:
    #         phones = list(csv.DictReader(file, delimiter=';'))

    #     for phone in phones:
    #         # TODO: Добавьте сохранение модели
    #         Phone.objects.create(
    #             id=phone['id'],
    #             name=phone['name'],
    #             image=phone['image'],
    #             price=phone['price'],
    #             release_date=phone['release_date'],
    #             lte_exists=phone['lte_exists'],
    #             slug=slugify(phone['name'])
    #         )
