import os
import django
from django.conf import settings

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_management.settings')
django.setup()

from django.db import connection

try:
    connection.ensure_connection()
    print("✅ Django is connected to PostgreSQL!")
    print(f"Database: {connection.settings_dict['NAME']}")
    print(f"Host: {connection.settings_dict['HOST']}:{connection.settings_dict['PORT']}")

    # Test a simple query
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"PostgreSQL Version: {version[0]}")

except Exception as e:
    print(f"❌ Connection failed: {e}")