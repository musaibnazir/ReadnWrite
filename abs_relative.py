import os

print(os.path.abspath('.'))
print(os.path.abspath('./new'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('-')))
print(os.path.relpath('/home/mnr/Desktop/pythonAutomation/R e ad i n g a n d Writing Files'))

os.path.basename(path)
os.path.dirname(path)
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
os.path.split(calcFilePath)
(os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
calcFilePath.split(os.path.sep)
'/usr/bin'.split(os.path.sep)
