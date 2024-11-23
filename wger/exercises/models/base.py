#  This file is part of wger Workout Manager <https://github.com/wger-project>.
#  Copyright (C) 2013 - 2021 wger Team
#
#  wger Workout Manager is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  wger Workout Manager is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Standard Library
import uuid  # Add this line for UUID generation

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Third Party
from simple_history.models import HistoricalRecords

# wger
from wger.utils.models import AbstractLicenseModel, AbstractHistoryMixin
from wger.core.models import License
from wger.exercises.managers import ExerciseBaseManagerAll
from .category import ExerciseCategory
from .equipment import Equipment
from .muscle import Muscle
from .variation import Variation


class ExerciseBase(AbstractLicenseModel, AbstractHistoryMixin, models.Model):
    """
    Model for an exercise base
    """

    uuid = models.UUIDField(
        default=uuid.uuid4,  # Generate a unique identifier
        editable=False,
        unique=True,
        verbose_name="UUID",
    )

    category = models.ForeignKey(
        ExerciseCategory,
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
    )

    muscles = models.ManyToManyField(
        Muscle,
        blank=True,
        verbose_name=_("Primary muscles"),
    )

    muscles_secondary = models.ManyToManyField(
        Muscle,
        verbose_name=_("Secondary muscles"),
        related_name="secondary_muscles_base",
        blank=True,
    )

    equipment = models.ManyToManyField(
        Equipment,
        verbose_name=_("Equipment"),
        blank=True,
    )

    variations = models.ForeignKey(
        Variation,
        verbose_name=_("Variations"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    created = models.DateTimeField(_("Date"), auto_now_add=True)
    last_update = models.DateTimeField(_("Date"), auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.category}: {self.uuid}"