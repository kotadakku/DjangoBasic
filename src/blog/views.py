from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
#
from .models import Article
from .forms import ArticleForm


class ArticleListView(ListView):
    queryset = Article.objects.all()
    template_name = 'articles/article_list.html'

class ArticleDetailView(DetailView):
    # queryset = Article.objects.filter(id__gt=1)
    template_name = 'articles/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
    form_class = ArticleForm
    queryset = Article.objects.all()
    template_name = 'articles/article_create.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    form_class = ArticleForm
    queryset = Article.objects.all()
    template_name = 'articles/article_create.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blog:list')