#! python

#python_email.py - Finds phone numbers and email addresses on the clipboard.


import pyperclip, re


phoneregex = re.compile(r'''(

    (\d{3}|\(\d{3}\))?     # area code its optional, that's why we add the (?), also it can be without or (|) with parentheses

    (\s|-|\.)?   #separator can be a hyphen (-) or a a period (.), it's also optional, ex: 7627281136

    (\d{3})   # first 3 digits 

    (\s|-|\.)?   #separator

    (\d{4})   #Last 4 digits

    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension its optional


    )''', re.VERBOSE)

# TO DO: CREATE EMAIL REGEX.


emailregex = re.compile (r'''(

[a-zA-Z0-9._%+-]+    #username can have numbers and letter, upper or lower

@   # @ symbol

[a-zA-Z0-9._%+-]+    #domain name can have numbers and letter, upper or lower (it doesn't protect againsta fake domains eg: @chocolatecake)

(\.[a-zA-Z]{2,4})   # dot-something

)''', re.VERBOSE)

# TO DO: FIND MATCHES IN CLIPBOARD TEXT.

#First we need to get the tex which was on the clipboard, with pyperclip.paste
text = str(pyperclip.paste())

matches = []

for groups in phoneregex.findall(text):
    #Group 1: Area Code, Group 3,5 First and last digits, Group 8: Extension
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])#merging with - eg 762-728-1136

    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailregex.findall(text):
    matches.append(groups[0])

# TO DO: COPY RESULTS TO THE CLIPBOARD

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print ('Copied matches to clipboard:')
    print('\n'.join(matches))
else:
    print ('No phone numbers and email addresses found.')