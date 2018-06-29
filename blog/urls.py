from django.conf.urls import url
from django.contrib import admin

urlpatterns =[
    url(r'ˆadmin/', admin.site.urls)
]