from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(CreateView):
    """Класс для создания нов.публикации """
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published', 'view_counter')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        """ Метод для динамического формирования slug name для заголовка"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save() 

        return super().form_valid(form)


class BlogListView(ListView):
    """Класс лоя просмотра всех публикаций."""
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """Метод для выведения только статей, которые имеют положительный признак публикации."""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    """Класс для просмотра детальной информации публикации."""
    model = Blog

    def get_object(self, queryset=None):
        """Метод для работы счетчика просмотров публикации"""
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    """Класс для редактирования публикации"""
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published', 'view_counter')

    def get_success_url(self):
        """ Метод для перенаправлять пользователя на просмотр этой статьи после её редактирования"""
        return reverse('blog:view', args=[self.kwargs.get('slug')])


class BlogDeleteView(DeleteView):
    """Класс  для удаления публикации"""
    model = Blog
    success_url = reverse_lazy('blog:list')
