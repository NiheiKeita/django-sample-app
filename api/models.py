from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', '未着手'),
        ('in_progress', '進行中'),
        ('done', '完了'),
    ]

    title = models.CharField('タイトル', max_length=200)
    description = models.TextField('説明', blank=True)
    status = models.CharField('状態', max_length=20, choices=STATUS_CHOICES, default='todo')
    due_date = models.DateField('期限', null=True, blank=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'タスク'
        verbose_name_plural = 'タスク'

    def __str__(self):
        return self.title
