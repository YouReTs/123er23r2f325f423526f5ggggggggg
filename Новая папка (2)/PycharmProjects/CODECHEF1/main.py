# CODECHEF1
# https://github.com/Sashi-7204/CODECHEF1

# Эта программа помогает нам читать 10 numbeers из файла. Записывайте четные и нечетные числа в отдельные файлы четными.txt и нечетными.txt
# Сначала создадим пустой список.
# Затем мы открываем номера файлов.txt в режиме чтения.
# Затем мы перебираем каждую строку в файле и добавляем строку в список.
# Наконец, мы печатаем список.

my_list = []
f = open('numbers.txt', "r")
for line in f:
    my_list.append((line.strip('\n')))
print(my_list)
f.close()
e = open("even.txt", "a")
o = open("odd.txt", "a")
for ele in my_list:
    if (int(ele) % 2 == 0):
        e.write(ele + "\n")
    else:
        o.write(ele + "\n")
e.close()
o.close()
