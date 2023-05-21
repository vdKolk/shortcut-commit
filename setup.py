#!/usr/bin/env python3

import getpass

# get the Shortcut token
scToken = getpass.getpass('Enter your scToken token: ')

# write the tokens to a file
with open('storage/secrets', 'w', encoding='UTF-8') as file:
    file.write(f'{scToken}')
    file.close()

print('Shortcut committer is now initialized and ready for use')
