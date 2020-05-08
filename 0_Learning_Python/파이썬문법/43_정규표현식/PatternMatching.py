import re

# raw string : consider escape character(\) as a character
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # re.Pattern 객체
mo = phoneNumRegex.search('my number is 415-555-4242')
print(mo.group())
print()

# Goruping with parenthesis & groups operation
print('😃grouping with parenthesis & groups operation')
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneRegex.search('my number is 415-555-4242')
print(mo.group(1)) # 415
print(mo.group(2)) # 555-4242
print(mo.group(0)) # 415-555-4242
areaCode, mainNumber = mo.groups()
print()


# groups : returns tuples
print('😃groups : returns tuples')
print('areaCode : {}, MainNumber : {}'.format(areaCode, mainNumber))
print()


# Matching Multiple Groups with the pipe
print('😃Matching Multiple Groups with the pipe')
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
m = batRegex.search('Batmobile')
print(m.group(1)) # group(1) : mobile
print(m.group(0)) # group(0) : Batmobile
print()


# Optional Matching with the Question Mark
# Question mark
# 1) Optional Matching
# 2) Nongreedy Matching followed by curly brackets / dot-star -> {start, end}? / .*?
batRegex = re.compile(r'Bat(wo)?man')   # (wo)? is optional
print('😃Optional Matching with the Question Mark')
m = batRegex.search('The Adventures of Batman')
m2 = batRegex.search('The Adventures of Batwoman')
print(m.group())
print(m2.group())
print()

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
p = phoneRegex.search('my number is 415-555-4242')
p2 = phoneRegex.search('my number is 555-4242')
print(p.group())
print(p2.group())
print()


# Zero or More with the star ( * )
print('😃Matching Zero or More with the star ( * )')
batRegex = re.compile(r'Bat(wo)*man')
m = batRegex.search('the adventure of Batman')
m2 = batRegex.search('the adventure of Batwoman')
m3 = batRegex.search('the adventure of Batwowoman')
print(m.group())    # Batman
print(m2.group())   # Batwoman
print(m3.group())   # Batwowoman
print()


# One or More with the star ( + )
print('😃Matching One or More with the star ( + )')
batRegex = re.compile(r'Bat(wo)+man')
m = batRegex.search('the adventure of Batman') # None
m2 = batRegex.search('the adventure of Batwoman')
m3 = batRegex.search('the adventure of Batwowoman')
print(m)            # None
print(m2.group())   # Batwoman
print(m3.group())   # Batwowoman
print()


# Matching Specific Repetitions with Curly Brackets
print('😃Matching Specific Repetitions with Curly Brackets')
haRegex = re.compile(r'(Ha){3,5}') # HaHaHa ~ HaHaHaHaHa
mo1 = haRegex.search('HaHaHa')
print(mo1.group())  # HaHaHa
mo2 = haRegex.search('Ha')
print(mo2)          # None


# Greedy and Nongreedy Matching
# Python regular expression matching is greedy by default
#   - In ambiguos situations, the longest is matched
# Nongreedy version of the curly brackets
#   - curly bracket follwoed by question mark
print('😃Greedy and Nongreedy Matching')
GreedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = GreedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())  #HaHaHaHaHa
NonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = NonGreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group()) #HaHaHa
print()


# findall() Method
# 1) Return a list of strings
# 2) if there are 'groups'(brackets), return a list of tuples
print('😃findall() Method')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo2 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())   # 415-555-9999
print(mo2)          # ['415-555-9999', '212-555-0000']
print()

print('😃findall() Method with groups : returns a list of tuples')
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo3 = phoneNumRegex2.findall('Cell: 415-555-9999 Work: 212-555-0000')
print('mo3 : ', mo3)          # [('415', '555', '9999'), ('212', '555', '0000')]
print('mo3[0]', mo3[0])
print('mo3[1]', mo3[1])
print()

print('😃re.match Method with groups : the matched group index starts with 1')
testRegex = re.compile(r'([a-zA-Z_][a-zA-Z0-9_]+)\((\w+)\)')
m = testRegex.match('print(1234)')
print(m.group())
print('group(0) : ', m.group(0))
print('group(1) : ', m.group(1))
print('group(2) : ', m.group(2))
# \w+ = [a-zA-Z_][a-zA-Z0-9_]
print()


# Character Classes
# \d        any numeric digit from 0 to 9
# \D        any non-numeric digit from 0 to 9
# \w        any letter, numeric digit, or the underscore ( word character )
# \W        any character that is not letter, numeric digit, or the underscore
# \s        any space, tab, newline character
# \S        any character that is not space, tab, newline character
# \b        any empty strings but onlyt at the biginning or end of a word
print('😃Character Classes')
xmasRegex = re.compile(r'\d+\s\w+')
# one or more numeric digits (\d+), followed by a whitespace character (\s), followed by one or more letter/digit/underscore characters (\w+)
m = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(m)
print()


# Making my own character classes : Square Brackets []
print('😃Making my own character classes : Square Brackets []')
vowelRegex = re.compile(r'[aeiouAEIOU]')    # all the vowels, both lowercase and upper case
v = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(v)                                    # ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

vowelRegex = re.compile(r'[^aeiouAEIOU]')   # all the non vowels.
v = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(v)                                    # ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

print()


# The Caret and dollar sign characters : ^\d  \d&
print('😃The Caret and dollar sign characters : ^\d  \d&')
beginsWithHello = re.compile(r'^Hello') # string that starts with number
m = beginsWithHello.search('Hello world!')
print(m.group())        # Hello

endsWithNumber = re.compile(r'\d$')     # string that ends with number
m = endsWithNumber.search('Your number is 42')
print(m.group())        # 2

wholeStringIsNum = re.compile(r'^\d+$') # string that starts and ends with number
m = wholeStringIsNum.search('1234567890')
print(m.group())        # 1234567890
print()


# The wildcard Character  . (dot)
print('😃The wildcard Character  . (dot)')
atRegex = re.compile(r'.at')     # any words that starts with 'any one letter' and ends with 'at'
m = atRegex.findall('The cat in the hut sat on the flat mat')
print(m)                         #   ['cat', 'sat', 'lat', 'mat']
print()


# Matching Everything with Dot-Star : .*
# .(dot)  : any single character except the newline
# *(star) : zero or more of the preceding character
print('😃Matching Everything with Dot-Star : .*?')
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group())       # First Name: Al Last Name: Sweigart
print(mo.group(1))      # AL
print(mo.group(2))      # Sweigart
print()


# Greedy/NonGreedy Matching Everything with Dot-Star : .*?
print('😃Greedy/NonGreedy Matching Everything with Dot-Star : .*?')
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())       # '<To serve man>'
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())       # '<To serve man> for dinner.>'
print()


# Matching Newlines with the Dot Character : re.compile(\'.*\', re.DOTALL)
print('😃re.compile(\'.*\', re.DOTALL) : Matching Newlines')
newLineRegex = re.compile('.*', re.DOTALL)
m = newLineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.')
print(m.group(), '\n')            # Serve the public trust.\nProtect the innocent. \nUphold the law.

noNewlineRegex = re.compile('.*')
m = noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.')
print(m.group())            # 'Serve the public trust.'


# Ingnore Cases : re.compile('pattern', re.I) / re.compile('pattern', re.IGNORECASE)
print('😃Ingnore Cases : re.compile(\'pattern\', re.I) / re.compile(\'pattern\', re.IGNORECASE)')
robocop = re.compile('ROBOCOp', re.I)
m = robocop.search('RoboCop is part man, part machine, all cop.')
print('re.compile(\'ROBOCOP\', re.I) => ', m.group())
print()


# Substituting Strings with the sub() Method : sub(\'Substitution\', String)
print('😃pattern.sub(\'Substitution\', String) Method')
namedRegex = re.compile(r'Agent \w+')
censoredString = namedRegex.sub('Censored', 'Agent Alice gave the secret documents to Agent Bob.')
print(censoredString)                     # Censored gave the secret documents to Censored.
print()


# Managing Comlex Regex : re.VERBOSE
# Ignore whitespaces and comments insdie the re.compile()
print('😃Managing Comlex Regex : re.VERBOSE')
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?  # area code
(\s|-|\.)?          # separator
\d{3}               # first 3 digits 
(\s|-|\.)           # separator
\d{4}               # last 4 digits
(\s*(ext|x|ext.)    # extnesion
\s*
\d{2,5})?
)''', re.VERBOSE)


# Combining re.compile() options : re.IGNORECASE, re.DOTALL, and re.VERBOSE
print('😃Combining re.compile() options : re.IGNORECASE, re.DOTALL, and re.VERBOSE')
print('''someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)''')


