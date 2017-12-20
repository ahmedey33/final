from django.db import models
# Create your models here.
from hobby.models import HobbyCat, HobbyItem


class Blog(models.Model):
    hobbyitem = models.ForeignKey(HobbyItem, on_delete = models.CASCADE)
    title = models.CharField(max_length = 250)
    slug = models.SlugField (max_length = 1000)
    created_date = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    description = models.CharField(max_length =140)
    content = models.TextField()
    link = models.URLField(blank = True)
    updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)

    def _str_(self):
        return self.title