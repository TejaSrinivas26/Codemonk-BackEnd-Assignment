"""
URL configuration for bookapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books.views import BookListAPIView, BookDetailAPIView
from books.views import SignupAPIView, VerifyEmailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('verifyemail/<str:uidb64>/<str:token>/', VerifyEmailAPIView.as_view(), name="verify-email"),
    path('books/', BookListAPIView.as_view()),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
]
