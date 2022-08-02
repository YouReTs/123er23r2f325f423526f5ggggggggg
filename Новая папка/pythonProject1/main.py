from random import choices
from tqdm.auto import tqdm


class LetterFile:
    def __init__(self, letter, max_lines):
        self.letter = letter
        self.number = 0
        self.line_count = 0
        self.max_lines = max_lines
        self.create()

    def create(self):
        self.open('w')

    def open(self, mode='w+'):
        self.file = open(self.letter + str(self.number) + '.txt', mode)

    def close(self):
        self.file.close()

    def append(self, line):
        self.file.write(line)
        self.line_count += 1
        if self.line_count >= self.max_lines:
            self.close()
            self.number += 1
            self.line_count = 0
            self.open()


def get_latin_letters():
    for ch in range(ord('a'), ord('z') + 1):
        yield chr(ch)


input_file_name = 'data.txt'
input_file_rows = 150_000_000
max_lines = 3000000_000
str_len = 15
alphabet = list(get_latin_letters())
print(*alphabet)

print('generating input file')
with open(input_file_name, 'w') as f:
    for i in tqdm(range(input_file_rows)):
        s = ''.join(choices(alphabet, k=str_len))
        f.write(s)
        f.write('\n')

files = {}

print('create files')
for ch in alphabet:
    f = LetterFile(ch, max_lines)
    files[ch] = f

print('process input file')
with open(input_file_name) as fr:
    for s in tqdm(fr.readlines()):
        fw = files[s[0]]
        fw.append(s)

print('closing files')
for ch in alphabet:
    f = files[ch]
    f.close()