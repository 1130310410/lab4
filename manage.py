#!/usr/bin/env python
import os
import sys
#here is a change
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab3.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
