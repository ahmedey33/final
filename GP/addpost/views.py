from . forms import AddpostForm
from . models import Blog
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer


class AddPostFormView(LoginRequiredMixin, TemplateView):
    login_url = 'login/'
    template_name = 'addpost/addpostform.html'

    def get(self, request):
        form = AddpostForm()
        blogs = Blog.objects.all()
        args = {'form': form, 'blogs': blogs}
        return render(request, self.template_name, args)

    def post(self, request):
        form = AddpostForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            slug = form.cleaned_data['slug']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            blog.save()
            form = AddpostForm()
            args = {'form': form, 'title': title, 'slug': slug, 'content': content}
            # return render(request, self.template_name, args)
            return redirect('addpost:bloglist')


class BlogItemIndexView(generic.ListView):
    template_name = 'addpost/postitemindex.html'
    context_object_name = 'blog'

    def get_queryset(self):
        return Blog.objects.all()


class BlogDetailView(generic.DetailView):
   model = Blog
   template_name = 'addpost/addpostdetail.html'


class PostList(APIView):
    def get(self, request):
        postlist = Blog.objects.all()
        serializer = PostSerializer(postlist, many = True)
        return Response(serializer.data)

	def post(self, request):
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)