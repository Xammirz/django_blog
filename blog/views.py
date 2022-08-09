from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from . import models
class IndexView(generic.ListView):
    def get(self, request):
        all_posts = models.BlogPost.objects.all()
        categorys = models.Category.objects.all()
        latest_news = models.BlogPost.objects.order_by("-id")[0:5]
        paginator = Paginator(all_posts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'index.html', context={'posts': all_posts,
                    'latest_news': latest_news, 'categorys': categorys,
                    'page_obj': page_obj})
def post_category(request, url):
    posts = models.BlogPost.objects.filter(category__url=url)
    categorys = models.Category.objects.all()
    latest_news = models.BlogPost.objects.order_by("-id")[0:5]
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'category_posts.html', context={'posts': posts,
    'categorys': categorys, 'page_obj': page_obj, 'latest_news': latest_news,})
class NewsView(generic.ListView):
    def get(self, request):
        all_posts = models.BlogPost.objects.all()
        categorys = models.Category.objects.all()
        latest_news = models.BlogPost.objects.order_by("-id")[0:5]
        paginator = Paginator(all_posts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'news.html', context={'posts': all_posts,
                    'latest_news': latest_news, 'categorys': categorys,
                    'page_obj':page_obj})
class DetailNewsView(generic.DetailView):
    model = models.BlogPost
    template_name = 'single-post.html'
    context_object_name = 'post'


class CreatePost(generic.CreateView):
    model = models.BlogPost
    template_name = 'post_add.html'
    fields = ('category', 'title', 'image', 'small_description', 'description')
    success_url = ''
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePost(generic.UpdateView):
    model = models.BlogPost
    fields = ('category', 'title', 'image', 'small_description', 'description')
    template_name = 'post_update.html'

class DeletePost(generic.DeleteView):
    model = models.BlogPost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('mynews')

class AuthorNews(generic.ListView):
    def get(self, request):
        author_news = models.BlogPost.objects.filter(
            author = self.request.user
        )
        return render(request, 'mynews.html', context={
            'author_news':author_news
        })
            
# Create your views here.
