from django.db import models

# Create your models here.
class ComentarioModel(models.Model):
    texto = models.TextField()
    sentimento = models.CharField(max_length=20)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.texto[:30]}... ({self.sentimento})"