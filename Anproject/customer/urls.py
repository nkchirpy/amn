from django.conf.urls import url
from customer import views

app_name = 'customer'

urlpatterns = [

    url(r'^contact_us$',views.Contactview.as_view(),name='contact_us'),
]
