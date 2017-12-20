from django.conf.urls import url
from . import views

app_name = 'addhobby'

urlpatterns = [
    # /addhobby/addhobbyform/
    url(r'^$', views.AddHobbyFormView.as_view(), name='addhobby'),

    # /addhobby/register/
    # url(r'^register/$', views.UserFormView.as_view(), name='register'),

]
