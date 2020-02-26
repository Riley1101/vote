"""Voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Index.views import AppAPI,PopularData,KingQueenDataAPI,Result,ImeiAPI,ReqAPI,KingAPI,QueenAPI,MisterAPI,MissAPI,CosAPI,CheckMultiple,MisterMissDataAPI,PopMissAPI,PopMisterAPI
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #fking statics
    path('admin/', admin.site.urls),
    path('kq/',KingQueenDataAPI.as_view(),name='kingqueendata'),
    path('mm/',MisterMissDataAPI.as_view(),name='mistermissdata'),
    path('imei/',ImeiAPI.as_view(),name='imei'),
    path('pop/',PopularData),
    path('key/',ReqAPI,name='key'),


    #fking posts
    path('king/',KingAPI.as_view(),name='king'),
    path('queen/',QueenAPI.as_view(),name='queen'),
    path('mister/',MisterAPI.as_view(),name='mister'),
    path('miss/',MissAPI.as_view(),name='miss'),
    path('cos/',CosAPI.as_view(),name='cos'),
    path('pmister/',PopMisterAPI.as_view(),name='popmister'),
    path('pmiss/',PopMissAPI.as_view(),name='pmiss'),

    #fking check
    path('c/',CheckMultiple.as_view(),name='c'),
    path('result/',Result,name="result")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
