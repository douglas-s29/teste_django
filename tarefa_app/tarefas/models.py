from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    inicio = models.DateTimeField(default=timezone.now)
    fim = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.titulo:
            # Gera o título automaticamente se ele não foi definido
            self.titulo = f"Tarefa de {self.user.username} - {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class TimeEntry(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='time_entries')
    data_registro = models.DateTimeField(auto_now_add=True)
    duracao = models.DurationField()
    descricao = models.TextField()

    def __str__(self):
        return f"{self.task.descricao} - {self.duracao}"
