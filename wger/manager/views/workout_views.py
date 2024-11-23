from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class WorkoutViewSet(ViewSet):
    """
    A simple ViewSet for listing workouts.
    """
    def list(self, request):
        return Response({"message": "List of workouts"})

