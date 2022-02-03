import os

print(os.path.join('usr','bin','spam'))

myfiles = ['accounts.txt','details.csv','invite.docx']
for filename in myfiles:
    print(os.path.join('usr/bin/spam',filename))
