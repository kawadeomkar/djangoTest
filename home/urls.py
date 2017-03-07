from django.conf.urls import url
from . import views


urlpatterns = [
    # home page -- /
    url(r'^$', views.home, name='home'),

    # create account -- /signup/
    url(r'^signup/', views.signup, name='signup'),

    # search for parking spot -- /search/
    url(r'^search/', views.search, name='search'),

    # sign in page
    url(r'^signin/', views.signin, name='signin'),

    # account page
    url(r'^account/', views.account, name='account'),

    # selling page
    url(r'^sell/', views.sell, name='sell'),

    # log out
    url(r'^log_out/', views.log_out, name='log_out')
]

    # url(r'^signout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
