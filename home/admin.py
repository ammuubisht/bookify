from django.contrib import admin
from .models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('book_name', )}
    list_display = ('book_name', 'author',)

admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Comment)