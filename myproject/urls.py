from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponse
from myapp.views import ProtectedView  # Імпортуємо наше представлення

# Просте представлення для домашньої сторінки
def home(request):
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/protected/', ProtectedView.as_view(), name='protected_view'),  # Додаємо новий маршрут для захищеного ендпоінту
    path('', home, name='home'),  # Додаємо маршрут для домашньої сторінки
]

def home(request):
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', home, name='home'),  # Додано простий маршрут для кореневої сторінки
]