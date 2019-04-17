# This program is responsible for searching an e-mails and phone numbers in clipboard

import re, pyperclip

# This block of code contain a model to find phone numbers

phone_model = re.compile(r'''(
    (\+(\d{2})|(\d){4})?            # Phone code
    ((\s)|\-)?                      # separator - white sign or dash
    (\d{3})                         # 3 first numbers
    ((\s)|\-)?                      # separator - white sign or dash
    (\d{3})                         # Numbers from 4th to 6th
    ((\s)|\-)?                      # separator - white sign or dash       
    (\d{3})                         # Numbers from 7th to 9th 
)''', re.VERBOSE)

# Code containing a model to find e-mail address

email_model = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
\.
[a-zA-Z]{2,4}
)''', re.VERBOSE)

# Code block looking for matches in clipboard

text = str(pyperclip.paste())
matches = []

for groups in phone_model.findall(text):
    matches.append(groups[0])

for groups in email_model.findall((text)):
    matches.append(groups[0])

# TODO: Copying results to clipboard



