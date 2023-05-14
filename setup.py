#!/usr/bin/env python3

import getpass

# first get the shortcut token
ghToken = getpass.getpass('Enter your GitHub token: ')

# second get the GitHub token
scToken = getpass.getpass('Enter your scToken token: ')


# write the tokens to a file
file = open('storage/secrets', 'w')
file.write(f'{ghToken};{scToken}')

file.close()

print('Shortcut committer is now initialized and ready for use')
