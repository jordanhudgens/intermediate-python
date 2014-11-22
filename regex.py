__author__ = 'admin'

import re

str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation jordan@test.com ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. chase@yahoo Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia tiffany@example.com deserunt mollit anim id est laborum'

# search() will find the first email address it finds
# match = re.search(r'[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z]+', str)
# if match:
#     print(match.group())

# findall() will return a collection of all of the matches
matches = re.findall(r'[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z]+', str)

# Iterating through the collection of matches returned
for match in matches:
    print(match)