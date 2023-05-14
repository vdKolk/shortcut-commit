#!/usr/bin/env python3

from shortcut_def import Shortcut

scNumber = Shortcut.get_story_number()

if not scNumber:
    raise LookupError('The shortcut number was not found, check cwd and branch name')
else:
    # for now just print number
    print(scNumber)