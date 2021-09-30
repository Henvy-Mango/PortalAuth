"""project entry point.

Using `python <project_package>` or `python -m <project_package>` command.
"""

if not __package__:
    import os
    import sys

    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from auth.gmccAuth import gmccAuth

if __name__ == '__main__':
    gmccAuth().run()