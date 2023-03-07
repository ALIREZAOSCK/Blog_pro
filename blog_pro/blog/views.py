from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from blog.models import Article, Category, Comment, Message, Like
from django.core.paginator import Paginator
from .forms import ContactUsForm, MessageForm


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')  # برای قسمت ریپلای است.
        body = request.POST.get('body')
        Comment.objects.create(body=body, articles=article, user=request.user, parent_id=parent_id)
    return render(request, 'blog/article_details.html', {'article': article})


def articles_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get("page")
    paginator = Paginator(articles, 1)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', {'articles': object_list})


def category_detail(request, pk):
    category = Category.objects.get(id=pk)
    articles = category.article_set.all()
    return render(request, 'blog/articles_list.html', {'articles': articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get("page")
    paginator = Paginator(articles, 1)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', {'articles': object_list})


def contact_us(request):
    if request.method == "POST":
        form = MessageForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            text = form.cleaned_data.get('text')
            email = form.cleaned_data.get('email')
            Message.objects.create(title=title, text=text, email=email)
    else:
        form = MessageForm()
    return render(request, 'blog/contact_us.html', {'form': form})

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.like.filter(article__slug=self.object.slug, user_id=self.request.user.id).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False
        return context


def like(request, slug, pk):
    try:
        like = Like.objects.get(article__slug=slug, user_id=request.user.id)
        like.delete()
    except:
        Like.objects.create(article_id=pk, user_id=request.user.id)
    return redirect('blog:article_detail', slug)
