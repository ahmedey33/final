from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

app_name = 'account'

urlpatterns = [
    # /register
    url(r'^$', views.UserFormView.as_view(), name='register'),

    # login
    url(r'^login/$', login, {'template_name': 'account/login.html'}, name='login'),

    # logout
    url(r'^logout/$', logout, name='logout'),

]
