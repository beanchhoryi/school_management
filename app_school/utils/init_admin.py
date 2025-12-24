import os
from django.contrib.auth import get_user_model

def create_admin():
    if os.environ.get("INIT_ADMIN") != "true":
        return

    User = get_user_model()
    admin_email = os.environ.get("ADMIN_EMAIL")
    admin_username = os.environ.get("ADMIN_USERNAME")
    admin_password = os.environ.get("ADMIN_PASSWORD")

    if not User.objects.filter(username=admin_username).exists():
        User.objects.create_superuser(
            username=admin_username,
            email=admin_email,
            password=admin_password
        )
        print("Admin created")
    else:
        print("Admin already exists")
