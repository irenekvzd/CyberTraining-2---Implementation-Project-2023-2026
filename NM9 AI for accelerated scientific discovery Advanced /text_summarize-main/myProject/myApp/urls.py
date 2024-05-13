from django.conf import settings
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # path('summary/', views.summary, name='input'),
    path('home/', views.index, name='input'),
    path('', views.index, name='input'),
    path('upload/', views.upload, name='upload'),
    path('text_summary/upload/', views.upload, name='upload'),
    path('text_summary/', views.text_summary, name='text'),
    path('pdf_input/', views.pdf_input, name='pdf_input'),
    #path('/pdf_summary/', views.pdf_summary, name='pdf_summary'),
    path('article_summary/', views.article_summary, name='article'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
