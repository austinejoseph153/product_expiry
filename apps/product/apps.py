from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'apps.product'
    verbose_name = 'Product'

    def ready(self):
        from . import task
        task.schedule_product_expiration_check()