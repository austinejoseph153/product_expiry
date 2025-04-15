from .models import Product
from django.utils import timezone
from twilio.rest import Client
from django.conf import settings


def send_sms(to, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILLIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message,
        from_=settings.TWILLIO_FROM_NUMBER,
        to=to
    )
    return message.sid

# send_sms("+2349021994595","Hello, this is a reminder that the following products are about to expire <a href='http://127.0.0.1:8000/product/list/'></a>")


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
    
