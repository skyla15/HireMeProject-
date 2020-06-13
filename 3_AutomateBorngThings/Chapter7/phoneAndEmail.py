# TODO : USE THE PAPERCLIP MODULE TO COPTY AND PASTE STRINGS
import pyperclip, re


# TODO : Create PhoneNumber regex
phoneRegex = re.compile(r'''
(\d{3}|\(\d{3}\))?              # area code         group 0
(\s|-|\.)?                      # seperator         group 1
(\d{4})                         # first 4 digits    group 2
(\s|-|\.)                       # seperator         group 3
(\d{4})                         # last 4 digits     group 4
''', re.VERBOSE)


# TODO : Create email regex
emailRegex = re.compile(r'''
.+                              # email accound preceding @
@                               # at 
.+                              # domain name 
\.                              # dot
\w+                             # co or com
\.?                             # optional dot for national code
\w{2,3}?                        # national codee
''', re.VERBOSE)
# Reference -> [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})


# TODO : Find matches in clipboard text
text = str(pyperclip.paste())
print(text)


# store the matches
matches = []


# phone number matches
for groups in phoneRegex.findall(text):     # phoneRegex grouping 되어있음
    print('phoneNum : ', groups)            # (xxx,-,xxxx,-,xxxx)   0 , 2 , 4
    phoneNum = '-'.join([groups[0], groups[2], groups[4]])
    matches.append(phoneNum)


# email matches
for groups in emailRegex.findall(text):
    print('mail gorup: ', groups)
    matches.append(groups)


# TODO : copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email adrresses are found.')




#
# 800-4203-7240
# 415-8463-9900
# 415-8563-9950
# info@nostarch.com
# media@nostarch.com
# academic@nostarch.com
# help@nostarch.com
#
