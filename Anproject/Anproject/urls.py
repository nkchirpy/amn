from django.conf.urls import url,include
from django.contrib import admin
from customer import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.Introview.as_view(),name='intro'),
    url(r'^home$',views.Indexview.as_view(),name='index'),
    url(r'^about_us$',views.Aboutview.as_view(),name='about_us'),
    url(r'^services$',views.Serviceview.as_view(),name='services'),
    url(r'',include('customer.urls')),
]
