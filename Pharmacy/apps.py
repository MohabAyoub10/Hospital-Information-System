from django.apps import AppConfig


class PharmacyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Pharmacy'
    def ready(self) -> None:
        import Pharmacy.signals