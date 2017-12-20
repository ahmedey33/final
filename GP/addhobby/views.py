from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import HobbyForm
# Create your views here.
from hobby.models import HobbyCat
#
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin


# With login
class AddHobbyFormView(LoginRequiredMixin, TemplateView):
    login_url = 'login/'
    template_name = 'addhobby/addhobbyform.html'

    def get(self, request):
        form = HobbyForm()
        hobbycats = HobbyCat.objects.all()
        args = {'form': form, 'hobbycats': hobbycats}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HobbyForm(request.POST)
        if form.is_valid():
            hobbycat = form.save(commit=False)

            hobbycat_title = form.cleaned_data['hobbycat_title']
            hobbycat_logo = form.cleaned_data['hobbycat_logo']
            hobbycat.save()
            form = HobbyForm()
            args = {'form': form, 'hobbycat_title': hobbycat_title, 'hobbycat_logo': hobbycat_logo}
            return redirect('hobby:hobbyindex')


# class UserFormView(TemplateView):
#     template_name = 'addhobby/registration_form.html'
#
#     # display blanck form
#     def get(self, request):
#         form = UserForm()
#         args = {'form': form}
#         return render(request,self.template_name,args)
#
#     def post(self, request):
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)  # Q Why it is False??
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save();
#
#             # return user object if credentials are correct
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('hobby:hobbyindex')
#         return render(request, self.template_name,{'form':form})


