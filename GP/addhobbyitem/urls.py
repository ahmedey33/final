from django.conf.urls import url
from . import views

app_name = 'addhobbyitem'

urlpatterns = [
    # /addhobby/addhobbyitmeform/
    url(r'^$', views.AddHobbyItemFormView.as_view(), name='addhobbyitem'),
    url(r'^itemlist$', views.HobbyItemIndexView.as_view(), name='hobbyitemindex'),

]
