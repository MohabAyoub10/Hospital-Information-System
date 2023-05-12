from django.apps import AppConfig


class LabRadiologyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Lab_Radiology'
    def ready(self) -> None:
        import Lab_Radiology.signals