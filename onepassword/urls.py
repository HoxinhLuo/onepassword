from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from onepassword.views import index, generaterandompassword

urlpatterns = [
    path('', index, name='index'),
    path('accounts/login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('generaterandompassword/', generaterandompassword, name='generaterandompassword'),
]
