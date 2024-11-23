#!/usr/bin/env python3

# Standard Library
import os
import sys

# Django
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wger.settings')
    execute_from_command_line(sys.argv)
