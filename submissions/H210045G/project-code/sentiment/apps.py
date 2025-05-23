from django.apps import AppConfig


class SentimentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sentiment"

    def ready(self):
        import sentiment.signals