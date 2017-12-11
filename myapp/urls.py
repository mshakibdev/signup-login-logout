
from django.conf.urls import url,include
from django.contrib import admin
from myform import views as form_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$',form_views.signupform, name='signup'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
