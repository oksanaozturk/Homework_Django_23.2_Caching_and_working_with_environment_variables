from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog


class BlogCreateView(CreateView):
    """Класс для создания нов.публикации """
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published', 'view_counter')
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    """Класс лоя просмотра всех публикаций."""
    model = Blog


class BlogDetailView(DetailView):
    """Класс для просмотра детальной информации публикации."""
    model = Blog


class BlogUpdateView(UpdateView):
    """Класс для редактирования публикации"""
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published', 'view_counter')
    success_url = reverse_lazy('blog:list')


class BlogDeleteView(DeleteView):
    """Класс  для удаления публикации"""
    model = Blog
    success_url = reverse_lazy('blog:list')
