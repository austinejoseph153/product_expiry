from .models import Product
from django.utils import timezone
from sms import send_sms

def send_expiry_notifications():
    message = "Hello, this is a reminder that the following products are about to expire:"
    recipient = "+2349021994595"
    send_sms(message, recipient)
send_expiry_notifications()

def check_expired_product():
    print("checking database for expired products....")
    current_date = timezone.now().date()
    products = Product.objects.all()
    for product in products:
        if product.expiry_date < current_date:
            product.status = "expired"
            product.save()
        else:
            if abs(product.expiry_date - product.maufacturing_date).days <= 30:
                product.status = "near-expired"
                product.save()
    print("task is done")
    
