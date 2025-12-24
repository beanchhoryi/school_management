from django.apps import AppConfig

class AppSchoolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_school'

    def ready(self):
        from .utils.init_admin import create_admin
        create_admin()

