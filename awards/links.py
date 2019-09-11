from awards import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.conf import settings




urlpatterns=[
    url(r'^$', views.register, name='register'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^home/$',views.home, name='home'),
    url(r'^project/$',views.project,name ='project'),
    url(r'profile/',views.profile, name='profile'),
    url(r'^post/', views.upload_form, name='post'),
    url(r'^profile/update/(\d+)$',views.edit_prof,name='update_profile'),
    url(r'^search/',views.search, name='search'),
    url(r'^logout/$', auth_views.logout, {"next_page": '/'})
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)