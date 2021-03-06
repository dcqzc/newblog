from django.contrib import admin
from .models import Article,Category,Tag
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Article, PostAdmin)