from django.conf.urls import url

from wagtailimportexport import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
