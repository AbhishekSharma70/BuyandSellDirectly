from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name='core'
urlpatterns=[
    path('',views.index,name='index'),
    path('terms_of_use',views.terms_of_use,name='terms_of_use'),
    path('private_policy',views.private_policy,name='private_policy'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login')

]