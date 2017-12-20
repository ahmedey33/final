from django.views.generic import TemplateView
from .forms import UserForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.
class UserFormView(TemplateView):
    template_name = 'account/registration_form.html'

    # display blanck form
    def get(self, request):
        form = UserForm()
        args = {'form': form}
        return render(request,self.template_name,args)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Q Why it is False??
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save();

            # return user object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('hobby:hobbyindex')
        return render(request, self.template_name,{'form':form})
