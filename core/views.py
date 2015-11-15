from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class MovieCreateView(CreateView):
    model = Movie
    template_name = "movie/movie_form.html"
    fields = ['title', 'synopsis']
    success_url = reverse_lazy('movie_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MovieCreateView, self).form_valid(form)

class MovieListView(ListView):
    model = Movie
    template_name = "movie/movie_list.html"

class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie/movie_detail.html"

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'movie/movie_form.html'
    fields = ['title', 'synopsis']

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')
    
class ReviewCreateView(CreateView):
    model = Review
    template_name = "review/review_form.html"
    fields = ['text']
    
    def get_success_url(self):
        return self.object.movie.get_absolute_url()
      
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.movie = Movie.objects.get(id=self.kwargs['pk'])
        return super(ReviewCreateView, self).form_valid(form)