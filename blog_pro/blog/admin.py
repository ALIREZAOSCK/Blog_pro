from django.contrib import admin
from . import models

# Methods
class FilterByTitle(admin.SimpleListFilter):
    title = 'کلید ها پر تکرار'
    parameter_name = 'title'
    def lookups(self, request, model_admin):
        return (
            ('asp', 'ای اس پی'),
            ('django', 'جنگو')
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "created", "get_image")
    list_filter = ("title", "body", FilterByTitle)
    search_fields = ("title", "body")
# Register
admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Message)
admin.site.register(models.Like)
