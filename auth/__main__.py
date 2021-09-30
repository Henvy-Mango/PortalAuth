"""project entry point.

Using `python <project_package>` or `python -m <project_package>` command.
"""
from auth import Adapter, gmccAuth

if not __package__:
    import os
    import sys

    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

if __name__ == '__main__':
    Adapter(gmccAuth).run()
