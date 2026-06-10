from django.db import models
from django.contrib.auth.models import User

class PerfilMembro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    area_principal = models.CharField(max_length=100, help_text="Ex: Biomedicina, Nutrição, Medicina, Enfermagem")
    registro_profissional = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.area_principal}"

class Topico(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    tags_multidisciplinares = models.CharField(max_length=200, help_text="Cruze as disciplinas. Ex: Bioquímica + Imunologia")
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo