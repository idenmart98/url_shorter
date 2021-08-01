import uuid

from django.conf import settings



def generate_random_string(string_length=5):
    random = str(uuid.uuid4()) 
    random = random.upper()
    random = random.replace("-","")
    return random[0:string_length]


def get_full_url(url):
    return f"{settings.SITE_URL}{url.short_code}"