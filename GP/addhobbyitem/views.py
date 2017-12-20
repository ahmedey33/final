from django.views.generic import TemplateView
# Create your views here.
from hobby.models import HobbyCat, HobbyItem
from .forms import HobbyItemForm
from django.views import generic

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class AddHobbyItemFormView(LoginRequiredMixin, TemplateView):
    login_url = 'login/'
    template_name = 'addhobbyitem/addhobbyitemform.html'

    def get(self, request):
        form = HobbyItemForm()
        hobbyitems = HobbyItem.objects.all()
        args = {'form': form, 'hobbyitems': hobbyitems}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HobbyItemForm(request.POST)
        if form.is_valid():
            hobbyitem = form.save(commit=False)
            hobbyitem_title = form.cleaned_data['hobbyitem_title']
            hobbyitem_dic = form.cleaned_data['hobbyitem_dic']
            hobbyitem.save()
            form = HobbyItemForm()
            args = {'form': form, 'hobbyitem_title': hobbyitem_title, 'hobbyitem_dic': hobbyitem_dic}
            return redirect('addhobbyitem:hobbyitemindex')

class HobbyItemIndexView(generic.ListView):
    template_name = 'addhobbyitem/hobbyitemindex.html'
    context_object_name = 'hobbyitems'

    def get_queryset(self):
        return HobbyItem.objects.all()