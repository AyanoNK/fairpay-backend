"""_summary_
"""
from django.db import models

# Create your models here.


VISIT_STATES = (
    ('started', 'Started'),
    ('finished', 'Finished')
)


class Visit(models.Model):
    """_summary_
    """
    waiter = models.ForeignKey('waiters.Waiter', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, default='started', choices=VISIT_STATES)
    table = models.ForeignKey('tables.Table', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomerVisit(models.Model):
    """_summary_
    """
    visit = models.ForeignKey('Visit', on_delete=models.CASCADE)
    customer = models.IntegerField()
    tip_percentage = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomerVisitProduct(models.Model):
    """_summary_
    """
    customer_visit = models.ForeignKey(
        'CustomerVisit', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
