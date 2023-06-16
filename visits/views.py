import datetime

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import Visit
from .serializers import VisitSerializer


# Create your views here.
class VisitViewSet(viewsets.ModelViewSet):
    """_summary_
    """
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    def list(self, request):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if not request.GET.get('start_date') or not request.GET.get('end_date'):
            return Response({
                'error': 'start_date and end_date are required'
            }, 400)

        # validate date format
        try:
            datetime.date.fromisoformat(start_date)
            datetime.date.fromisoformat(end_date)
        except ValueError:
            return Response({
                'error': 'start_date and end_date are wrongly formatted'
            }, 400)

        visits = Visit.objects.filter(created_at__range=[start_date, end_date])

        serializer = VisitSerializer(visits, many=True)
        return Response(serializer.data)

    def create(self, request):
        return Response(status=405)

    def retrieve(self, request, pk=None):
        return Response(status=405)

    def update(self, request, pk=None):
        return Response(status=405)

    def partial_update(self, request, pk=None):
        return Response(status=405)

    def destroy(self, request, pk=None, *args, **kwargs):
        visit = get_object_or_404(Visit, pk=pk)
        if visit.status == 'finished':
            return super().destroy(request, pk, *args, **kwargs)
        return Response({
            'error': 'Cannot delete a visit that is not finished'
        }, 400)
