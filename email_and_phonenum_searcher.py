# This program is responsible for searching an e-mails and phone numbers in clipboard

import re

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

# TODO: Code contain a model to find e-mail address

# TODO: Code block looking for matches in clipboard

# TODO: Copying results to clipboard



