from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog import models


class IndexView(ListView):
    model = models.BlogPost
    template_name = 'index.html'
    paginate_by = 5
    queryset = models.BlogPost.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = models.Category.objects.all()
        context['latest_news'] = models.BlogPost.objects.order_by("-id")[:5]
        return context


def post_category(request, url):
    posts = models.BlogPost.objects.filter(category__url=url)
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'category_posts.html',
                  context={'posts': posts,
                           'categorys': models.Category.objects.all(),
                           'page_obj': page_obj,
                           'latest_news': models.BlogPost.objects.order_by("-id")[:5]
                           })


class NewsView(ListView):
    model = models.BlogPost
    template_name = 'news.html'
    paginate_by = 5
    queryset = models.BlogPost.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = models.Category.objects.all()
        context['latest_news'] = models.BlogPost.objects.order_by("-id")[:5]
        return context


class DetailNewsView(DetailView):
    model = models.BlogPost
    template_name = 'single-post.html'
    context_object_name = 'post'


class CreatePost(CreateView):
    model = models.BlogPost
    template_name = 'post_add.html'
    fields = ('category', 'title', 'image', 'small_description', 'description')
    success_url = reverse_lazy('mynews')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(UpdateView):
    model = models.BlogPost
    fields = ('category', 'title', 'image', 'small_description', 'description')
    template_name = 'post_update.html'


class DeletePost(DeleteView):
    model = models.BlogPost
    template_name = 'post_delete.html'