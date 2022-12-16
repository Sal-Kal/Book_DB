from django.contrib import admin

# Register your models here.

from .models import author, publisher, book

admin.site.register(author)
admin.site.register(publisher)
admin.site.register(book)
