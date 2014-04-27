from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^mail/', include('bambu_mail.urls')),
)