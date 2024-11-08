from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Phone, self).save(*args, **kwargs)
