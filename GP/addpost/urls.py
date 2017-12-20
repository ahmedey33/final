from django.conf.urls import url, include
from django.contrib import admin
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'addpost'

urlpatterns = [
    url(r'^$', views.AddPostFormView.as_view(), name = 'addpost'),
    url(r'^bloglist/$', views.BlogItemIndexView.as_view(), name='bloglist'),
   #ur   #/blog/slug ex:blog/stem_collection
    url(r'^bloglist/(?P<slug>[\w-]+)/$', views.BlogDetailView.as_view(), name='blogdetailview'),
    url(r'^postlistapi/', views.PostList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
