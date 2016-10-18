#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings.sites.bmshow")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings.sites.nashvillenote")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
