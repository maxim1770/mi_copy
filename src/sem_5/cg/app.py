from tkinter import Frame, Menu, Label, Canvas, Button, Tk, Scale
from tkinter import Scrollbar, filedialog, messagebox, CENTER
from PIL import ImageTk, Image, ImageDraw, ImageFilter
import random
import math


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.create_menu()

        self.image = None
        self.photo = None

        self.display = Canvas(self.parent, width=400, height=400, bg="gray")
        self.display_img = self.display.create_image(0, 0)
        self.display.pack()

    def open(self):
        self.filename = filedialog.askopenfilename()
        if self.filename:
            self.image = Image.open(self.filename)
            self.photo = ImageTk.PhotoImage(self.image)
            self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")

            self.file_menu.entryconfig("Сохранить", state='active')

            self.parametr_menu.entryconfig("Яркость", state='active')
            self.parametr_menu.entryconfig("Контрастность", state='active')
            self.parametr_menu.entryconfig("Цветовой баланс", state='active')
            self.parametr_menu.entryconfig("Увеличить 'Билинейная интерполяция'", state='active')

            self.filters_menu.entryconfig("Негатив", state='active')
            self.filters_menu.entryconfig("Шум", state='active')
            self.filters_menu.entryconfig("Оттенки серого", state='active')
            self.filters_menu.entryconfig("Сепия", state='active')
            self.filters_menu.entryconfig("Черно-белый", state='active')
            self.filters_menu.entryconfig("Оттенки красного", state='active')

            self.scr1 = Scrollbar(root, command=self.display.yview, orient='vertical')
            self.scr1.place(x=133, y=3)

            self.scr2 = Scrollbar(root, command=self.display.xview, orient="horizontal")
            self.scr2.place(x=145, y=452)

            self.btn_save.config(state="normal")

            self.btn_clear.config(state="normal")

            self.btn_yar.config(state="normal")
            self.btn_contr.config(state="normal")
            self.btn_cvb.config(state="normal")
            self.btn_enl_biln.config(state="normal")

    def save(self):
        path = filedialog.asksaveasfilename()
        if path:
            try:
                self.image.save(path)
                messagebox.showinfo('Сохранение', 'Успех! Файл сохранен.')
            except KeyError:
                messagebox.showerror('Ошибка', 'Не задано расширение')

    def clear(self):
        self.image = Image.open(self.filename)
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")

    def close(self):
        if messagebox.askyesno('Выход', 'Вы уверены?'):
            self.parent.destroy()
        else:
            messagebox.showinfo("Отмена", "Выход отменен")

    def brightness(self):
        draw = ImageDraw.Draw(self.image)
        width = self.image.size[0]
        height = self.image.size[1]
        pix = self.image.load()
        factor = self.scale.get()
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0] + factor
                b = pix[i, j][1] + factor
                c = pix[i, j][2] + factor
                if (a < 0):
                    a = 0
                if (b < 0):
                    b = 0
                if (c < 0):
                    c = 0
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        del draw

    def brightness_click(self):
        root = Tk()
        root.geometry('%dx%d+%d+%d' % (150, 100, 400, 400))
        label = Label(root, text='Выберете значение яркости')
        label.pack(anchor=CENTER)

        self.scale = Scale(root, from_=-100, to=100, orient="horizontal")
        self.scale.pack(anchor=CENTER)

        def reset_brightness():
            self.brightness()

        def close():
            root.destroy()

        button_rnd = Button(root, text="Ок", command=reset_brightness)
        button_rnd.place(x=25, y=62)

        button_close = Button(root, text="Закрыть", command=close)
        button_close.place(x=70, y=62)

    def contrast(self):
        draw = ImageDraw.Draw(self.image)
        width = self.image.size[0]
        height = self.image.size[1]
        pix = self.image.load()
        factor = self.scale_contrast.get()
        contrast1 = (259 * (factor + 255)) / (255 * (259 - factor))
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                a = round(contrast1 * (a - 128) + 128)
                b = round(contrast1 * (b - 128) + 128)
                c = round(contrast1 * (c - 128) + 128)
                if (a < 0):
                    a = 0
                if (b < 0):
                    b = 0
                if (c < 0):
                    c = 0
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        del draw

    def contrast_click(self):
        root_contrast = Tk()
        root_contrast.geometry('%dx%d+%d+%d' % (150, 100, 400, 400))
        label_contrast = Label(root_contrast, text='Выберете значение контрастности')
        label_contrast.pack(anchor=CENTER)
        self.scale_contrast = Scale(root_contrast, from_=-100, to=100, orient="horizontal")
        self.scale_contrast.pack(anchor=CENTER)

        def reset_contrast():
            self.contrast()

        def close():
            root_contrast.destroy()

        button_rnd = Button(root_contrast, text="Ок", command=reset_contrast)
        button_rnd.place(x=25, y=62)
        button_close = Button(root_contrast, text="Закрыть", command=close)
        button_close.place(x=70, y=62)

    def rgb_balans(self):
        draw = ImageDraw.Draw(self.image)
        width = self.image.size[0]
        height = self.image.size[1]
        pix = self.image.load()
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0] + self.scale_r.get()
                b = pix[i, j][1] + self.scale_g.get()
                c = pix[i, j][2] + self.scale_b.get()
                if (a < 0):
                    a = 0
                if (b < 0):
                    b = 0
                if (c < 0):
                    c = 0
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        del draw

    def rgb_balans_click(self):
        root_rgb_balans = Tk()
        root_rgb_balans.geometry('%dx%d+%d+%d' % (200, 225, 400, 400))

        label_r = Label(root_rgb_balans, text='Выберете значение крсаного')
        label_r.pack(anchor=CENTER)
        self.scale_r = Scale(root_rgb_balans, from_=-256, to=256, orient="horizontal")
        self.scale_r.pack(anchor=CENTER)

        label_g = Label(root_rgb_balans, text='Выберете значение зеленого')
        label_g.pack(anchor=CENTER)
        self.scale_g = Scale(root_rgb_balans, from_=-256, to=256, orient="horizontal")
        self.scale_g.pack(anchor=CENTER)

        label_b = Label(root_rgb_balans, text='Выберете значение синего')
        label_b.pack(anchor=CENTER)
        self.scale_b = Scale(root_rgb_balans, from_=-256, to=256, orient="horizontal")
        self.scale_b.pack(anchor=CENTER)

        def reset_rgb_balans():
            self.rgb_balans()

        def close():
            root_rgb_balans.destroy()

        button_rnd = Button(root_rgb_balans, text="Ок", command=reset_rgb_balans)
        button_rnd.place(x=45, y=190)
        button_close = Button(root_rgb_balans, text="Закрыть", command=close)
        button_close.place(x=100, y=190)

    def enlarge_bilinear(self):
        width = self.image.size[0]
        height = self.image.size[1]
        pix = self.image.load()
        percent = self.scale.get()

        image = Image.new("RGBA", (width * percent, height * percent), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        for i in range(width - 1):
            for j in range(height - 1):

                P: tuple[int, int, int] = pix[i, j]
                A: tuple[int, int, int] = pix[i - 1, j]
                D: tuple[int, int, int] = pix[i + 1, j]
                C: tuple[int, int, int] = pix[i, j - 1]
                B: tuple[int, int, int] = pix[i, j + 1]

                if C == A and C != D and A != B:
                    draw.point((i - 1, j), A)
                else:
                    draw.point((i - 1, j), P)

                if A == B and A != C and B != D:
                    draw.point((i - 1, j + 1), B)
                else:
                    draw.point((i - 1, j + 1), P)

                if B == D and B != A and D != C:
                    draw.point((i, j + 1), D)
                else:
                    draw.point((i, j + 1), P)

                if D == C and D != B and C != A:
                    draw.point((i, j), C)
                else:
                    draw.point((i, j), P)

        self.photo = ImageTk.PhotoImage(image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        del draw

    def enlarge_bilinear_click(self):
        root = Tk()
        root.geometry('%dx%d+%d+%d' % (150, 100, 400, 400))
        label = Label(root, text='Выберите насколько увеличить изображение')
        label.pack(anchor=CENTER)

        self.scale = Scale(root, from_=0, to=4, orient="horizontal")
        self.scale.pack(anchor=CENTER)

        def reset_enlarge_bilinear():
            self.enlarge_bilinear()

        def close():
            root.destroy()

        button_rnd = Button(root, text="Ок", command=reset_enlarge_bilinear)
        button_rnd.place(x=25, y=62)

        button_close = Button(root, text="Закрыть", command=close)
        button_close.place(x=70, y=62)

    def negativ_clic(self):
        draw = ImageDraw.Draw(self.image)
        width = self.image.size[0]
        height = self.image.size[1]
        pix = self.image.load()
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                draw.point((i, j), (255 - a, 255 - b, 255 - c))
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        del draw

    def rnd_noise(self):
        draw = ImageDraw.Draw(self.image)
        width = self.image.size[0]
        height = self.image.size[1]
        pix = self.image.load()
        factor = self.scale_rnd.get()
        for i in range(width):
            for j in range(height):
                rand = random.randint(-factor, factor)
                a = pix[i, j][0] + rand
                b = pix[i, j][1] + rand
                c = pix[i, j][2] + rand
                if (a < 0):
                    a = 0
                if (b < 0):
                    b = 0
                if (c < 0):
                    c = 0
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))

        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        del draw

    def rnd_noise_click(self):
        root = Tk()
        root.geometry('%dx%d+%d+%d' % (150, 100, 400, 400))

        label_rnd = Label(root, text='Выберете значение шума')
        label_rnd.pack(anchor=CENTER)

        self.scale_rnd = Scale(root, from_=0, to=100, orient="horizontal")
        self.scale_rnd.pack(anchor=CENTER)

        def reset_rnd():
            self.rnd_noise()

        def close():
            root.destroy()

        button_rnd = Button(root, text="Ок", command=reset_rnd)
        button_rnd.place(x=25, y=62)
        button_close = Button(root, text="Закрыть", command=close)
        button_close.place(x=70, y=62)

    def gray_click(self):
        draw = ImageDraw.Draw(self.image)
        width = self.image.size[0]
        height = self.image.size[1]
        pix = self.image.load()
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a + b + c) // 3
                draw.point((i, j), (S, S, S))
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        del draw

    def sepia_click(self):
        depth = 30
        draw = ImageDraw.Draw(self.image)
        width = self.image.size[0]
        height = self.image.size[1]
        pix = self.image.load()
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a + b + c) // 3
                a = S + depth * 2
                b = S + depth
                c = S
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        del draw

    def black_white_click(self):
        draw = ImageDraw.Draw(self.image)
        width = self.image.size[0]
        height = self.image.size[1]
        pix = self.image.load()
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = a + b + c
                if (S > (((255) // 2) * 3)):
                    a, b, c = 255, 255, 255
                else:
                    a, b, c = 0, 0, 0
                draw.point((i, j), (a, b, c))
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        del draw

    def rnd_red_click(self):
        draw = ImageDraw.Draw(self.image)
        width = self.image.size[0]
        height = self.image.size[1]
        pix = self.image.load()
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                Red = (255 - (255 - a))
                if b > 10:
                    b = b // 100
                if c > 10:
                    c = c // 100
                draw.point((i, j), (Red, b, c))
        self.photo = ImageTk.PhotoImage(self.image)
        self.display.itemconfigure(self.display_img, image=self.photo, anchor="nw")
        del draw

    def create_menu(self):
        menu = Menu(self.parent)
        self.file_menu = Menu(menu)
        self.filters_menu = Menu(menu)
        self.parametr_menu = Menu(menu)

        menu.add_cascade(label="Файл", menu=self.file_menu)
        menu.add_cascade(label="Параметры", menu=self.parametr_menu)
        menu.add_cascade(label="Фильтры", menu=self.filters_menu)

        self.file_menu.add_command(label="Открыть", command=self.open)
        self.file_menu.add_command(label="Сохранить", command=self.save, state='disabled')
        self.file_menu.add_command(label="Очистить", command=self.clear, state='disabled')
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=self.close)

        self.parametr_menu.add_command(label="Яркость", command=self.brightness_click,
                                       state='disabled')
        self.parametr_menu.add_command(label="Контрастность",
                                       command=self.contrast_click, state='disabled')
        self.parametr_menu.add_command(label="Цветовой баланс",
                                       command=self.rgb_balans_click, state='disabled')
        self.parametr_menu.add_command(label="Увеличить 'Билинейная интерполяция'", command=self.enlarge_bilinear_click,
                                       state='disabled')

        self.filters_menu.add_command(label="Негатив", command=self.negativ_clic,
                                      state='disabled')
        self.filters_menu.add_command(label="Шум", command=self.rnd_noise_click,
                                      state='disabled')
        self.filters_menu.add_command(label="Оттенки серого", command=self.gray_click,
                                      state='disabled')
        self.filters_menu.add_command(label="Сепия", command=self.sepia_click,
                                      state='disabled')
        self.filters_menu.add_command(label="Черно-белый",
                                      command=self.black_white_click, state='disabled')
        self.filters_menu.add_command(label="Оттенки красного",
                                      command=self.rnd_red_click, state='disabled')

        label_fail = Label(root, text='Параметры файла')
        label_fail.place(x=22, y=30)

        self.btn_open = Button(text="Открыть", height=2, width=12, command=self.open)
        self.btn_open.place(x=25, y=60)

        self.btn_save = Button(text="Сохранить", height=2, width=12, command=self.save,
                               state='disabled')
        self.btn_save.place(x=25, y=105)

        self.btn_clear = Button(text="Очистить", height=2, width=12, command=self.clear,
                                state='disabled')
        self.btn_clear.place(x=25, y=150)

        self.btn_exit = Button(text="Выход", height=2, width=12, command=self.close)
        self.btn_exit.place(x=25, y=195)

        label_fail_par = Label(root, text='Параметры изображения')
        label_fail_par.place(x=650, y=30)

        self.btn_yar = Button(text="Яркость", height=2, width=20,
                              command=self.brightness_click, state='disabled')
        self.btn_yar.place(x=675, y=60)

        self.btn_contr = Button(text="Контрастность", height=2, width=20,
                                command=self.contrast_click, state='disabled')
        self.btn_contr.place(x=675, y=105)

        self.btn_cvb = Button(text="RGB баланс", height=2, width=20,
                              command=self.rgb_balans_click, state='disabled')
        self.btn_cvb.place(x=675, y=150)

        self.btn_enl_biln = Button(text="Увеличить 'Билинейная интерполяция'", height=2, width=20,
                                   command=self.enlarge_bilinear_click, state='disabled')
        self.btn_enl_biln.place(x=675, y=195)

        self.parent.config(menu=menu)


if __name__ == '__main__':
    root = Tk()
    root.title("Урок 6 - Добавления функциональности пункту меню 'Фильтры'")
    root.geometry("825x500+250+100")
    app = Example(root)
    root.mainloop()
