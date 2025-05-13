from django.contrib import admin
from . models import Member
from . models import Category
from . models import Product


admin.site.register(Member)
admin.site.register(Category)
admin.site.register(Product)
