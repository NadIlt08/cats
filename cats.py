from tkinter import *
from PIL import Image,  ImageTk
import requests # Модуль, который отправляет запросы в интернет
from io import BytesIO # Позволяет работать с выводом инф и работать с байтами (1 и 0)(чтобы из байтов превратить в нормальное изображение)

from bottle import response
from image.views import image


def load_image():
    try:
        response = requests.get(url) # делаем запрос по этой ссылке и то, что вернется, положим в ответ(response).
        response.raise_for_status() # для обработки исключений: если будет ошибка, то появится тут
        image_data = BytesIO(response.content) # в эту переменную ложим обработанное изображение
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img) # эту img положим в img ниже (img = load_image(url))
    except Exception as e:
        print (f"Произошла ошибка: {e}")
        return None

window = Tk()
window.title("Cats!")
window.geometry("600x480")

label = Label()
label.pack()

url = "https://cataas.com/cat"
img = load_image(url) # функция загрузки изображения, эту img положим в другую ниже (label.image = img)

if img:
    label.config(image=img)
    label.image = img # чтобы сборщик мусора пайтона картинку не убрал, присваиваем метке

window.mainloop()