from tkinter import *


def go_decode():
    if r_btn.get() == 0 or r_btn.get() == 1:
        go_code()
    else:
        tOutput.delete(1.0, END)
        t_in = tInput.get(1.0, END)
        t_in = t_in[0:len(t_in) - 1]
        t_out = ""
        if r_btn.get() == 2:
            for i in range(len(t_in)):
                t_out += chr(ord(t_in[i]) - 1)
        elif r_btn.get() == 3:
            p = 0
            for i in range(len(t_in)):
                t_out += chr(ord(t_in[i]) - p)
                p = (p + 1) % 33
        tOutput.insert(1.0, t_out)


def go_code():
    tOutput.delete(1.0, END)
    t_in = tInput.get(1.0, END)
    t_in = t_in[0:len(t_in) - 1]
    t_out = ""
    if r_btn.get() == 0:
        for i in range(len(t_in) - 1, -1, -1):
            t_out += t_in[i]
    elif r_btn.get() == 1:
        for i in range(0, len(t_in) - 1, 2):
            t_out += t_in[i + 1] + t_in[i]
    elif r_btn.get() == 2:
        for i in range(len(t_in)):
            t_out += chr(ord(t_in[i]) + 1)
    elif r_btn.get() == 3:
        p = 0
        for i in range(len(t_in)):
            t_out += chr(ord(t_in[i]) + p)
            p = (p + 1) % 33
    tOutput.insert(1.0, t_out)


def clear_text():
    tInput.delete(1.0, END)
    tOutput.delete(1.0, END)


def res_to_def():
    tInput.delete(1.0, END)
    txt = tOutput.get(1.0, END)
    txt = txt[0:len(txt) - 1]
    tInput.insert(1.0, txt)


def paste_from_clipboard():
    try:
        tInput.insert(END, root.clipboard_get())
    except:
        tInput.insert(END, "\nОшибка: Буфер пуст")


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(tOutput.get(1.0, END))


def set_menu_pos(event):
    menuInput.post(event.x_root, event.y_root)


# Инициализация окна
root = Tk()
root.resizable(False, False)
root.title("Шифровальщик")

# Настройка геометрии
WIDTH = 800
HEIGHT = 320
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

# Текстовые метки
textInput = Label(text='Введите исходный текст:')
textInput.place(x=2, y=1)
textOutput = Label(text='Результат:')
textOutput.place(x=2, y=157)

# Текстовые поля
tInput = Text(width=70, height=8, wrap=WORD)
tInput.place(x=5, y=20)
tInput.insert(1.0, """Экземпляры Checkbutton также могут быть визуально оформлны в группу,
но каждый флажок независим от остальных. Каждый может быть в состоянии "Установлен" или 
"Снят", независимо от состояний других флажков. Другими словами, в группе Checkbutton 
можно сделать множественный выбор, в группе Radiobutton - нет.""")

scrollInput = Scrollbar(command=tInput.yview, width=20)
scrollInput.place(x=570, y=20, height=132)
tInput["yscrollcommand"] = scrollInput.set

tOutput = Text(width=70, height=8, wrap=WORD)
tOutput.place(x=5, y=180)

scrollOutput = Scrollbar(command=tOutput.yview, width=20)
scrollOutput.place(x=570, y=180, height=132)
tOutput['yscrollcommand'] = scrollOutput.set

# Меню на правую кнопку мыши
menuInput = Menu(tearoff=False)
menuInput.add_command(label='Копировать результат', command=copy_to_clipboard)
menuInput.add_command(label='Вставить в исходный текст', command=paste_from_clipboard)
menuInput.add_command(label='Результат -> Исходный', command=res_to_def)
menuInput.add_command(label='Очистить текст', command=clear_text)
tInput.bind('<Button-3>', set_menu_pos)

btnCode = Button(text='Шифровать', width=25, command=go_code)
btnCode.place(x=600, y=20)

btnDecode = Button(text='Дешифровать', width=25, command=go_decode)
btnDecode.place(x=600, y=50)

# Радиокнопки
textAlgo = Label(text="Алгоритм:")
textAlgo.place(x=600, y=100)
r_btn = IntVar()
r_btn.set(0)
algo01 = Radiobutton(text='Инвертировать', variable=r_btn, value=0)
algo02 = Radiobutton(text='Замена с соседней', variable=r_btn, value=1)
algo03 = Radiobutton(text='+1', variable=r_btn, value=2)
algo04 = Radiobutton(text='+ позиция (до 33)', variable=r_btn, value=3)
algo01.place(x=600, y=120)
algo02.place(x=600, y=140)
algo03.place(x=600, y=160)
algo04.place(x=600, y=180)

root.mainloop()

# Зашифрую текста немножечка)
# Еще чуть-чуть циферок 33064к123
# будем считать, что это код от подъезда
