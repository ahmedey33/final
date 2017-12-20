from django.contrib import admin
from  .models import HobbyCat, HobbyItem, Tags
# Register your models here.
admin.site.register(HobbyCat)
admin.site.register(HobbyItem)
admin.site.register(Tags)
