from django.urls import path
from .views import (
    add_batch_form_view, add_product_form_view,
      product_list_view, batch_list_view, delete_product, 
      expired_product_list_view, create_new_user
)

app_name = "product"
urlpatterns = [
    path("add/batch/", view=add_batch_form_view, name="add_batch"),
    path("batch/list/", view=batch_list_view, name="batch_list"),
    path("add/product/", view=add_product_form_view, name="add_product"),
    path("product/list/", view=product_list_view, name="product_list"),
    path("expired-product/list/", view=expired_product_list_view, name="expired_product_list"),
    path("delete/product/<int:pk>/", view=delete_product, name="delete_product"),
    path("create/new/user/", view=create_new_user, name="create_new_user"),
]