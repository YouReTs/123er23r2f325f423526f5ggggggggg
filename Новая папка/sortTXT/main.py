# https://github.com/Ilylej00/SortingTXT

from genericpath import exists


# Read the file, put each line into an array
def readFileToArray(filename):
    # first version
    lines = []
    for line in open(filename):
        lines.append(line)
    return lines


# main
print('What .txt file would you like to sort?')
fileToSort = input('File Name: ')

# check if properly formatted and the file exists
while not fileToSort.lower().endswith('.txt') or not exists(fileToSort):
    fileToSort = input('File Name: ')

# sort the file, line based
elements = readFileToArray(fileToSort)
elements.sort()

# creates output file in the format 'fileName + _Sorted.txt'
outputName = fileToSort.split('.', -1)[0] + ('_Sorted.txt')
print(outputName)

# writes the sorted elements to output file (line based)
with open(outputName, 'w') as out:
    for element in elements:
        if element.endswith('\n'):
            out.write(element)
        else:
            out.write(element + '\n')
