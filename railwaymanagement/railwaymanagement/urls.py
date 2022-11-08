from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('adminhome/', admin.site.urls),
    path('user/', include('app.urls')),
    path('admin/', views.AdminView.as_view(), name='admin_home'),
    path('admin/addbooking/', views.AdminAddBooking.as_view(), name='admin_add_booking'),
    path('admin/users/',views.users , name='users'),
    path('admin/trains/',views.trains , name='trains'),
    path('admin/reject/<int:id>',views.accept , name='delete_train'),
    path('admin/accept/<int:id>',views.reject , name='delete_train'),
    path('admin/delete/<int:id>',views.delete , name='delete_train'),
    path('admin/edit/<int:id>',views.EditTrainView.as_view() , name='delete_train'),
    path('admin/requests/',views.AdminUserRequests.as_view(),name='requests'),    
    path('', views.index, name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/',views.logout_user,name='logout')
]
