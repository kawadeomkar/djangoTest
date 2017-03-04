from django.conf.urls import url
from . import views


urlpatterns = [
    # home page -- /
    url(r'^$', views.home, name='home'),

    # create account -- /signup/
    url(r'^signup/', views.signup, name='signup'),

    # search for parking spot -- /search/
    url(r'^search/', views.search, name='search'),
]