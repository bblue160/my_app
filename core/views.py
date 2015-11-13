from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class MovieCreateView(CreateView):
    model = Movie
    template_name = "movie/movie_form.html"
    fields = ['title', 'synopsis']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MovieCreateView, self).form_valid(form)