from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='projects'

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)