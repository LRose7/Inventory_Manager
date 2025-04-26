from django.urls import path
from .views import (index,
                    inventory_list,
                    per_product_view,
                    add_inventory,
                    update_inventory,
                    delete_inventory,
                    dashboard,
                   )

urlpatterns = [
    path("", index, name="index"),
    path("inventory_list/", inventory_list, name="inventory_list"),
    path("per_product/<int:pk>", per_product_view, name="per_product"),
    path("add_inventory/", add_inventory, name="add_inventory"),
    path("update_inventory/<int:pk>", update_inventory, name="update_inventory"),
    path("delete_inventory/<int:pk>", delete_inventory, name="delete_inventory"),
    path("dashboard/", dashboard, name="dashboard"), 
]