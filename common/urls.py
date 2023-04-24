from django.urls import path
# django.contrib.auth는 장고의 로긘 로그아웃을 도와주는 앱
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns =[
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]