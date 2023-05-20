

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("owner/", views.dashboard, name="dashboard"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/customer/", views.CustomerSignUpForm.as_view(), name="customer-signup"),
    path("signup/owner/", views.OwnerSignUpView.as_view(), name="owner-signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name="pages/index.html"), name="logout"),
]
