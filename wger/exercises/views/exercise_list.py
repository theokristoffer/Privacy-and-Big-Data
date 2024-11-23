from django.views.generic import ListView
from wger.exercises.models import Exercise

class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercises/exercise_list.html'
    context_object_name = 'exercises'
