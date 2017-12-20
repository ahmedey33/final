from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'hobby'

urlpatterns = [
    # /hobby/
    url(r'^$', views.HobbyIndexView.as_view(), name='hobbyindex'),
    # /hobby/16/ - hobby id
    #url(r'^(?P<slug>[\w-]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^bloglist/(?P<pk>[0-9]+)/$', views.PostIndexView.as_view(), name='postindex'),
      #/blog/slug ex:blog/stem_collection
    url(r'^bloglist/(?P<slug>[\w-]+)/$', views.PostDetailView.as_view(), name='postdetailview'),

    url(r'^hobbyapi/', views.HobbyList.as_view()),
    url(r'^hobbyitemapi/', views.HobbyItemList.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
