"""
App models to store tables-related data.

"""
from django.db import models

# Create your models here.


STATUS_CHOICES = (
    ('available', 'available'),
    ('busy', 'busy')
)


class Table(models.Model):
    """
    Table class.
    alias = table name
    created_at = date of creation
    updated_at = date of last update
    """
    alias = models.CharField(max_length=255)
    status = models.CharField(
        max_length=255, default='available', choices=STATUS_CHOICES)
    capacity = models.IntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Verbose name for Table model.
        """
        verbose_name = "Table"
        verbose_name_plural = "Tables"
