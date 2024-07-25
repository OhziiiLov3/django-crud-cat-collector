from django.urls import path 
from . import views 

urlpatterns=[
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('cats/',views.cat_index, name='cat-index'),
    path('cats/<int:cat_id>/',views.cat_detail, name='cat-detail'),
    path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),
    # Feedings
    path('cats/<int:cat_id>/add-feeding/', views.add_feeding, name='add_feeding'),
    path('feedings/<int:feeding_id>/delete-feeding/', views.delete_feeding, name='delete_feeding'),
]