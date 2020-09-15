from django.contrib import admin

from .models import Author, Category, Post, Comment, PostView
from django.db import models
from django.forms import TextInput, Textarea


# class YourModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size':'200'})},
#         models.TextField: {'widget': Textarea(attrs={'rows':400, 'cols': 40})},
#     }




admin.site.register(Author)
admin.site.register(Category)
#admin.site.register(Post, YourModelAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
