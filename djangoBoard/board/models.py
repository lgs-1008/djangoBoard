from django.db import models

# Create your models here.
class Board(models.Model):
    writer = models.CharField(max_length=50, default='')
    title = models.CharField(max_length=100, null=False)
    contents = models.TextField(blank=True)
    createTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createTime']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board-detail', args=[str(self.id)])
