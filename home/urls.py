from django.conf.urls import url
from django.views.generic import ListView, DetailView
from home.models import ParkingSpot
from . import views


urlpatterns = [
    # home page -- /
    url(r'^$', views.home, name='home'),

    # create account -- /signup/
    url(r'^signup/', views.signup, name='signup'),

    # search for parking spot -- /search/
    url(r'^search/', views.SearchView.as_view(), name='search'),

    # sign in page
    url(r'^signin/', views.signin, name='signin'),

    # account page
    url(r'^account/', views.UserDetail.as_view(), name='account'),

    # selling page
    url(r'^sell/', ListView.as_view(queryset=ParkingSpot.objects.all()), name='sell'),

    # log out
    url(r'^log_out/', views.log_out, name='log_out'),

    # about page
    url(r'^about/', views.about, name='about'),
]

    # url(r'^signout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
