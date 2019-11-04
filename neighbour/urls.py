from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='projects'

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'register/',views.register,name = 'register'),
    url(r'login/',views.login_view,name='login'),
    url(r'logout/',views.logout_view,name='logout'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)