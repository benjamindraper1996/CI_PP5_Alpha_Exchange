"""
A Module to hold all the URL's for the products app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListProducts.as_view(), name='all_products'),
    path('search/', views.SearchProduct.as_view(), name='search_products'),
    path('<product_id>', views.ProductDetail.as_view(), name='product_detail'),
    path('categories/', views.categories, name="categories"),
    path('categories_list/<str:cats>', views.categories_view,
         name="categories_list"),
    path(
        'create_product/', views.ProductCreate.as_view(),
        name='create_product'),
    path(
        'update/<str:pk>/', views.ProductUpdate.as_view(),
        name='update_product'),
    path(
        'delete/<str:pk>/', views.ProductDelete.as_view(),
        name='delete_product'),
    path(
        'create_category/', views.CategoryCreate.as_view(),
        name='create_category'
        ),
    path(
        '<int:pk>/update_category/', views.CategoryUpdate.as_view(),
        name='update_category'
        ),
    path(
        '<int:pk>/delete_category/', views.CategoryDelete.as_view(),
        name='delete_category'
        ),
    path(
        'like/<product_id>/', views.ProductLike.as_view(),
        name='product_like'),
    path(
        'edit_review/<int:pk>', views.EditReview.as_view(),
        name="edit_review"),
    path(
        'delete_review/<int:review_id>', views.delete_review,
        name="delete_review"),
]
