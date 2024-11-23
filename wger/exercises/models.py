from django.db import models
from wger.exercises.models import ExerciseBase  # Confirm ExerciseBase is here
from wger.core.models import ExerciseCategory, License  # Adjust path if models are in core

class ExerciseBase(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    # Additional fields (update based on your schema)
    license_title = models.CharField(max_length=300)
    license_object_url = models.URLField(max_length=200)
    license_author = models.TextField(null=True, blank=True)
    license_author_url = models.URLField(max_length=200)
    license_derivative_source_url = models.URLField(max_length=200)
    uuid = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    # Many-to-many relationships
    equipment = models.ManyToManyField('Equipment', related_name='exercise_bases', blank=True)
    muscles = models.ManyToManyField('Muscle', related_name='primary_exercise_bases', blank=True)
    muscles_secondary = models.ManyToManyField(
        'Muscle', related_name='secondary_exercise_bases', blank=True
    )

    # Foreign key relationships
    category = models.ForeignKey(
        'ExerciseCategory', on_delete=models.CASCADE, related_name='exercise_bases'
    )
    license = models.ForeignKey('License', on_delete=models.CASCADE, related_name='exercise_bases')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'exercises'
