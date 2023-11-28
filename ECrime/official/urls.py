from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('official' ,views.official),
    path('officiallog' ,views.officiallog),
    path('dash',views.dash),
    path('cmt',views.cmt),
    path('cmtview',views.cmtview),
    path('cmp',views.cmp),
    path('news',views.news),
    path('news_view',views.news_view),
    path('n_view',views.n_view)
    

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)