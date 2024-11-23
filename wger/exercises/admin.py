from django.contrib import admin
from .models import (
    Exercise,
    ExerciseCategory,
    Equipment,
    Muscle,
    Variation,
    ExerciseImage,
    ExerciseComment,
)

# Register models in the admin interface
admin.site.register(Exercise)
admin.site.register(ExerciseCategory)
admin.site.register(Equipment)
admin.site.register(Muscle)
admin.site.register(Variation)
admin.site.register(ExerciseImage)
admin.site.register(ExerciseComment)
