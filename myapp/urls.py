from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 
from myapp import views


router = routers.SimpleRouter()

router.register(r'book', views.BookModelViewset, basename="book")
router.register(r'borrow', views.BorrowModelViewset, basename="borrow")
router.register(r'register', views.UserRegisterModelViewset, basename="register")

urlpatterns = [
    path('login/', obtain_auth_token, name="obtain-auth-token")

]+ router.urls