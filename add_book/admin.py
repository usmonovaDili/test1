from django.contrib import admin
from .models import AuthorModel, GenerModel, BookModel

# Register your models here.


admin.site.register(GenerModel)
admin.site.register(BookModel)
admin.site.register(AuthorModel)
