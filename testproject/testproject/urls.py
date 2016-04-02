from django.conf.urls import include, url

urlpatterns = (
    url(r'^mail/', include('bambu_mail.urls')),
)
