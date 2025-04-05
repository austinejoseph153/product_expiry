from django.db import models

class Batch(models.Model):
    name = models.CharField(max_length=100, verbose_name="Batch Name")
    quantity = models.IntegerField(verbose_name="Quantity of Product in Batch")
    manufacturing_date = models.DateField(verbose_name="Batch Manufacturing Date")
    expiry_date = models.DateField(verbose_name="Batch Expiry Date")
    description = models.TextField(verbose_name="Batch Description", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Batch Creation Date")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Product Batch"
        verbose_name_plural = "Product Batches"

class Product(models.Model):
    EXPIRY_CHOICES = (
        ("active", "ACTIVE"),
        ("expired","EXPIRED"),
        ("near-expired", "NEAR EXPIRY")
    )
    name = models.CharField(max_length=100, verbose_name="Product Name", unique=True)
    manufacturer = models.CharField(max_length=100, verbose_name="Manufacturers Name")
    quantity = models.IntegerField(verbose_name="Product Quantity")
    category = models.CharField(max_length=100, verbose_name="Product Category")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Product Price")
    maufacturing_date = models.DateField(verbose_name="Product Manufacturing Date")
    expiry_date = models.DateField(verbose_name="Product Expiry Date")
    image = models.ImageField(upload_to='product_images/', verbose_name="Product Image")
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, verbose_name="Product Batch")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Product Creation Date")
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default="active", choices=EXPIRY_CHOICES)
    description = models.TextField(verbose_name="Product Description")

    def __str__(self):
        return self.name
