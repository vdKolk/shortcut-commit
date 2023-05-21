#!/usr/bin/env python3

import sys
from github_def import GitHub


try:
    if sys.argv[1] == '-a':
        GitHub.amend_commit()
        sys.exit(0)
except IndexError:
    pass

GitHub.create_commit()
