from django.contrib import admin
from django.urls import path
from MySql_CRUD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'), 
    path('insert/', views.insert),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    # path('view/', views.view, name='View'),
    # path('search/', views.search, name='Search'),
    # path('logout/', views.logout, name='Logout'),
]
