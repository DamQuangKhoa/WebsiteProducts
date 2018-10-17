from django.urls import path
from feature import views

app_name = 'feature'


urlpatterns = [
    path('',views.Index_view.as_view(),name ="index" ),
    path('products/',views.Products.as_view(),name ="products" ),
    path('<int:pk>/products',views.Product_Detail.as_view(),name ="detail" ),
    path('orders/',views.Orders.as_view(),name ="orders" ),
    path('orders/update/<int:pk>',views.OrderUpdate.as_view(success_url="/feature/orders"),name ="order_update" ),
    path('orders/detail/<int:pk>',views.OrderDetail.as_view(),name ="order_detail" ),
    path('orders/delete/<int:pk>',views.OrderDelete.as_view(success_url="/feature/orders"),name ="order_delete" ),
    path('orders/create/<int:pk>',views.OrderCreate.as_view(success_url="/feature/orders"),name ="order_create" ),
    path('orders/customer/<int:pk>',views.Customer_order.as_view(),name ="order_customer" ),

]