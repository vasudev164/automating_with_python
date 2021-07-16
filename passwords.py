import sys
import pyperclip
passwords = {
  'email': 'vasudev',
}

if len(sys.argv)<2:
    print("managing passwords with python!")
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print("The password for "+account+" is copied to clipboard")
else:
    print("There is no account saved with name : "+account)
