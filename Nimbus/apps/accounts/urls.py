from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
from nimbus.apps import debug_urls


urlpatterns = debug_urls()

admin.autodiscover()

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r"^$", views.index, name="index"),
    url(r"^login$", views.login_view.as_view(), name="login"),
    url(r"^logout$", views.logout_view, name="logout"),
    url(r"^(?P<media_type>(images)|(links)|(text)|(archives)|(audio)|(video)|(other))$", views.dashboard_view, name="filter_media"),
    url(r"^upload", views.upload_file, name="upload")
)
