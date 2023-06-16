from django.db.models import Sum
from rest_framework import serializers

from .models import CustomerVisit, Visit


class CustomerVisitSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """

    class Meta:
        """_summary_
        """
        model = CustomerVisit
        fields = ('id', 'visit', 'products',
                  'created_at', 'updated_at')


class VisitSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    summary = serializers.SerializerMethodField()

    def get_summary(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_

        Returns:
            _type_: _description_
        """
        customer_visits = obj.customervisit_set.all()
        data = {
            'checks_total': 0,
            'tips_total': 0
        }
        for visit in customer_visits:
            customer_visit_total = visit.customervisitproduct_set.all(
            ).aggregate(total=Sum('product__price'))['total'] or 0
            data['checks_total'] += customer_visit_total
            data['tips_total'] += customer_visit_total * \
                visit.tip_percentage / 100
        return data

    class Meta:
        """_summary_
        """
        model = Visit
        fields = ('id', 'waiter', 'table', 'summary',
                  'created_at', 'updated_at')
