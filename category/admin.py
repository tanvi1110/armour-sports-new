from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')
    search_fields = ['category_name', 'slug']

admin.site.register(Category, CategoryAdmin)


# from django.contrib import admin
# from .models import Book

# Register your models here.
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'author', 'year')
#     search_fields = ['title', 'author']

# admin.site.register(CategoryAdmin, Category)

# class PhotoAdmin(admin.ModelAdmin):
#     ...
#     search_fields = ['name', 'description','catergories', 'user__related_fieldname','keyword', ]

# admin.site.register(Video,VideoAdminModel)


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'author', 'year')
#     search_fields = ['title', 'author']

# admin.site.register(Book, BookAdmin)