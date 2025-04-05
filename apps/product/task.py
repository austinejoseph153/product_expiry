from apscheduler.schedulers.background import BackgroundScheduler
from .utils import check_expired_product

# automatic update for cruiselines, ships, and ship itineraries
def schedule_product_expiration_check():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_expired_product, 'interval', minutes=50)
    scheduler.start()
