from django.contrib import admin
from . import models

#for category creation
@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','id','status','slug','author')
    prepopulated_fields = {'slug':('title',), }

admin.site.register(models.Category)