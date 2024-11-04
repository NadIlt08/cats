
from tkinter import *
from tkinter import ttk
from PIL import Image,  ImageTk
import requests # Модуль, который отправляет запросы в интернет
from io import BytesIO # Позволяет работать с выводом инф и работать с байтами (1 и 0)(чтобы из байтов превратить в нормальное изображение)

Allowed_tags = ["sleep", "jump", "fight", "white", "bengal", "siamese", "cute", "black"]

def load_image(url):
    try:
        response = requests.get(url) # делаем запрос по этой ссылке и то, что вернется, положим в ответ(response).
        response.raise_for_status() # для обработки исключений: если будет ошибка, то появится тут
        image_data = BytesIO(response.content) # в эту переменную ложим обработанное изображение
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS) # загрузка изображения под определенный размер
        return ImageTk.PhotoImage(img) # эту img положим в img ниже (img = load_image(url))
    except Exception as e:
        print (f"Произошла ошибка: {e}")
        return None

def open_new_window():
    tag = tag_combobox.get()
    url_tag = f"https://cataas.com/cat/{tag}" if tag else "https://cataas.com/cat"
    img = load_image(url_tag) # функция загрузки изображения, эту img положим в другую ниже (label.image = img)
    if img:
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.pack()
        label.image = img # чтобы сборщик мусора пайтона картинку не убрал, присваиваем метке

def exit():
    window.destroy()

window = Tk()
window.title("Cats!")
window.geometry("600x520")

# tag_entry = Entry()
# tag_entry.pack()

mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Файл", menu=filemenu)
filemenu.add_command(label="Загрузить фото", command=open_new_window)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=exit)

# update_button = Button(text="Обновить", command=set_image)
# update_button.pack()

url = "https://cataas.com/cat"

tag_label = Label(text="Выбери тег")
tag_label.pack()

tag_combobox = ttk.Combobox(values=Allowed_tags)
tag_combobox.pack()

load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()

window.mainloop()