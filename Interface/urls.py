from django.conf.urls import url
from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about/', views.aboutus, name='aboutus'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search, name = 'search'),
    path('chart', views.chart),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="rest_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uib64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

#path('search/<slug:stock_symbol>', views.search, name='search'),
#url(r'^search/', views.search, name='search')