from django.shortcuts import render
from django.views import generic
from .models import HobbyCat, HobbyItem
from addpost.models import Blog
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HobbyCatSerializer, HobbyItemtSerializer

#  Create your views here.


class HobbyIndexView(generic.ListView):
    template_name = 'hobby/hobbyindex.html'
    context_object_name = 'all_hobbycats'

    def get_queryset(self):
        return HobbyCat.objects.all()


class DetailView(generic.DetailView):
    model = HobbyCat
    template_name = 'hobby/detail.html'


class PostIndexView(generic.DetailView):
    model = HobbyItem
    template_name = 'hobby/postindex.html'

class PostDetailView(generic.DetailView):
	model = Blog
	template_name = 'hobby/postdetailview.html'   

class HobbyList(APIView):

	def get(self, request):
		hobbies = HobbyCat.objects.all()
		serializer = HobbyCatSerializer(hobbies, many = True)
		return Response(serializer.data)

	def post(self, request):
		serializer = HobbyCatSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HobbyItemList(APIView):

	def get(self, request):
		hobbyItems = HobbyItem.objects.all()
		serializer = HobbyItemtSerializer(hobbyItems, many = True)
		return Response(serializer.data)

	def post(self, request):
		serializer = HobbyItemtSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
