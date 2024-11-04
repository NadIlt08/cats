from tkinter import *
from PIL import Image,  ImageTk
import requests # Модуль который отправляет запросы в интернет
from io import BytesIO # Позволяет работать с выводом инф и работать с байтами (1 и 0)(чтобы из байтов превратить в нормальное изображение)

from Scripts.калькулятор import window

window = Tk()
window.title("Cats!")
window.geometry("600x480")

label = Label()
label.pack()

url = "https://cataas.com/cat"
img = load_image(url) # функция загрузки изображения

if img:
    label.config(image=img)
    label.image = img # чтобы сборщик мусора пайтона картинку не убрал, присваиваем метке

window.mainloop()