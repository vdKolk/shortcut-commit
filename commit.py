#!/usr/bin/env python3

import sys
from github_def import GitHub

if sys.argv[1] == '-a':
    GitHub.amend_commit()
else:
    GitHub.create_commit()
