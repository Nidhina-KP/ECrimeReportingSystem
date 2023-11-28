from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('',views.index),
    path('home',views.home),
    path('reg',views.reg),
    path('log',views.log),
    path('userupde',views.userupde),
    path('edit',views.edit),
    path('update',views.update),
    path('delete',views.delete),
    path('crime',views.crime),
    path('missing',views.missing),
    path('gallery' ,views.gallery),
    path('gallery1' ,views.gallery1),
    path('report' ,views.report),
    path('case' ,views.case),
    path('user_card' ,views.user_card),
    path('mview' ,views.mview),
    path('compview',views.compview ),
    path('childcase' ,views.childcase),
    path('wcase' ,views.wcase),
    path('mcase' ,views.mcase),
    path('rcase' ,views.rcase),
    path('ecrime_mail',views.ecrime_mail),
    path('status',views.status),
    path('status1',views.status1),
    path('status2',views.status2),
    path('wanted',views.wanted),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
