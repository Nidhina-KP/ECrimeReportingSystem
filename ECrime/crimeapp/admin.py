from django.contrib import admin
from . models import reg_tbl,crime_tbl,miss_tbl,report_tbl
# Register your models here.
admin.site.register(reg_tbl)
admin.site.register(crime_tbl)
admin.site.register(miss_tbl)
admin.site.register(report_tbl)