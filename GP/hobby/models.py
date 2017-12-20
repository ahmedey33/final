from django.db import models

# Create your models here.


class Tags(models.Model):
    label = models.CharField(max_length = 30,)

    def __str__(self):
        return self.label


class HobbyCat(models.Model):
    hobbycat_disc = models.CharField(max_length = 1000)
    hobbycat_title = models.CharField(max_length = 250)
    hobbycat_logo = models.CharField(max_length = 1000)

    def __str__(self):
        return self.hobbycat_title


class HobbyItem(models.Model):
    hobbycat = models.ForeignKey(HobbyCat, on_delete = models.CASCADE)
    hobbyitem_logo = models.CharField(max_length = 1000)
    hobbyitem_title = models.CharField(max_length = 250)
    hobbyitem_dic = models.CharField(max_length = 1000)

    def __str__(self):
        return self.hobbyitem_title
