from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify

class Category(models.Model):

    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
class Article(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=30)
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, unique=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})
    def get_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px;" height="50px;">')
        else:
            return format_html('<h3>تصویری وجود ندارد</h3>')
    get_image.short_description = 'تصویر'
    class Meta:
        ordering = ('-created',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"

class Comment(models.Model):

    articles = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]
    class Meta:
        verbose_name = 'نظر کاربر'
        verbose_name_plural = 'نظرات کاربران'

class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like', verbose_name='کابر')
    article = models.ForeignKey(Article, on_delete=models.CharField, related_name='like', verbose_name="مقاله")
    def __str__(self):
        return f'{self.user.username}-{self.article.title}'
    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'