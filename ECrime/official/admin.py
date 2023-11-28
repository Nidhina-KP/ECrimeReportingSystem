from django.contrib import admin
from . models import offreg_tbl,cmnt_tbl,news_tbl

# Register your models here.
admin.site.register(offreg_tbl)
admin.site.register(cmnt_tbl)
admin.site.register(news_tbl)
