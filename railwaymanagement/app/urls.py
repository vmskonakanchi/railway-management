from django.urls import path
from . import views

urlpatterns = [
    path('',views.UserView.as_view(),name='user'),
    path('bookings/',views.user_bookings,name='user_bookings'),
    path('book/<int:id>/' ,views.book , name='book')
]