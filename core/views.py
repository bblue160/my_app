from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
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

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        movie = Movie.objects.get(id=self.kwargs['pk'])
        reviews = Review.objects.filter(movie=movie)
        context['reviews'] = reviews
        user_reviews = Review.objects.filter(movie=movie, user=self.request.user)
        context['user_reviews'] = user_reviews
        return context

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'movie/movie_form.html'
    fields = ['title', 'synopsis']

    def get_object(self, *args, **kwargs):
        object = super(MovieUpdateView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')

    def get_object(self, *args, **kwargs):
        object = super(MovieDeleteView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

class ReviewCreateView(CreateView):
    model = Review
    template_name = "review/review_form.html"
    fields = ['text']

    def get_success_url(self):
        return self.object.movie.get_absolute_url()

    def form_valid(self, form):
        movie = Movie.objects.get(id=self.kwargs['pk'])
        if Review.objects.filter(movie=movie, user=self.request.user).exists():
            raise PermissionDenied()
        form.instance.user = self.request.user
        form.instance.movie = Movie.objects.get(id=self.kwargs['pk'])
        return super(ReviewCreateView, self).form_valid(form)

class ReviewUpdateView(UpdateView):
    model = Review
    pk_url_kwarg = 'review_pk'
    template_name = 'review/review_form.html'
    fields = ['text']

    def get_success_url(self):
        return self.object.movie.get_absolute_url()

    def get_object(self, *args, **kwargs):
        object = super(ReviewUpdateView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

class ReviewDeleteView(DeleteView):
    model = Review
    pk_url_kwarg = 'review_pk'
    template_name = 'review/review_confirm_delete.html'

    def get_success_url(self):
        return self.object.movie.get_absolute_url()

    def get_object(self, *args, **kwargs):
        object = super(ReviewDeleteView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object