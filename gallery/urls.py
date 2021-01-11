from django.urls import path
from . import views

urlpatterns = [
    path("", views.ImagesListView.as_view(), name="image_list"),
    path("created_image/", views.CreateImageView.as_view(), name="created_image"),
    path('<int:pk>/', views.ImageDetailView.as_view(), name='detail_image'),
    path('<slug:slug>/', views.ResizingImageView.as_view(), name='resizing_image'),
    path('handler/<int:pk>/', views.ResizingImageHandlerView.as_view(), name='resizing_handler'),
]
