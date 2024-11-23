from django.views.generic import ListView
from wger.exercises.models import Exercise

class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercise_list.html'  # Replace with the actual template
    context_object_name = 'exercises'

