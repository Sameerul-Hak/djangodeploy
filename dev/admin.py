from django.contrib import admin
from dev.models import Post,Comments,Like
# Register your models here.
admin.site.register([Post,Comments,Like])