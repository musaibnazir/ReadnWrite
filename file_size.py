import os

#print(os.path.getsize('/home/mnr/Desktop/pythonAutomation/R e ad i n g a n d Writing File'))
#print(os.listdir('file_size.py'))

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)
