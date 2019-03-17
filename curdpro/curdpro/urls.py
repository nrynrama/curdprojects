from django.conf.urls import include, url
from django.contrib import admin
from curdapp import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.homeview),
    url(r'^insert/',views.inserting),
    url(r'^retrieve',views.retrieving),
    url(r'^update/',views.updating),
    url(r'^delete/',views.deleting)
]