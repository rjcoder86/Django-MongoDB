from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import blogs
# from .forms import BlogsForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BlogsList(ListView):
    model = blogs
    template_name='allblogs.html'
    context_object_name= 'allblogs'

class BlogCreate(CreateView):
    model = blogs
    template_name='create.html'
    fields = '__all__'
    success_url=reverse_lazy('home')
    
class BlogUpdate(UpdateView):
    model = blogs
    template_name='updateblog.html'
    fields = '__all__'
    success_url=reverse_lazy('home')
    context_object_name = 'b'

class BlogDelete(DeleteView):
    model = blogs
    template_name='deleteblog.html'
    context_object_name='batman'
    success_url = reverse_lazy('home')

class GetBlog(DeleteView):
    model = blogs
    template_name='getblog.html'
    context_object_name= 'b'