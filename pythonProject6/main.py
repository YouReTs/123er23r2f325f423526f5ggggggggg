# Port(IP)_Scanner(Threading).py
#  Многопоточный сканер портов

import threading  # Подключаем модуль threading для работы с потоками
import socket  # Подключаем модуль socket для работы с сокетами (интерфейс для обеспечения обмена данными между процессами)

print('-' * 35)
target = input('Enter host:\n\n')  # Ввод хоста для сканирования
print('-' * 35)


def portscan(port):  # Создаём функцию сканирования портов

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаём сокет
    s.settimeout(0.5)   # Выставляем таймаут

    try:
        connection = s.connect((target, port))  # Пытаемся приконнектиться к хосту
        print('Port :', port, "is open.")   # В случае соединения, пишем что порт открыт
        connection.close()   # Закрываем соединение
    except:
        pass   # Оператор-заглушка, в случае отсутствия соединения, ничего не выполняем


ports = [21, 22, 23, 25, 38, 43, 80, 109, 110, 115, 118, 119, 143,  # Список портов
194, 220, 443, 540, 585, 591, 1112, 1433, 1443, 3128, 3197,
3306, 4000, 4333, 5100, 5432, 6669, 8000, 8080, 9014, 9200]

for element in ports:   # Перебор в цикле портов
    t = threading.Thread(target=portscan, kwargs={'port': element})  # Создаём поток

    t.start()   # Запуск потока

input()
