#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("JEEVES_SETTINGS_MODULE", "settings")

    from jeeves.core.management import execute_from_command_line

    execute_from_command_line(sys.argv[1:])
