from django.urls import path
from account_app.views import LoginView


urlpatterns = [
    path('login/', LoginView.as_view())
]
