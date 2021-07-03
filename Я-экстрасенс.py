from tkinter import *
import random as rdm
import tkinter.messagebox as mb


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.start()
        btn_info = Button(root, text="Узнать!", bg="#4f92f1", font=("Comic Sans MS", 7),
                             command=self.show_info)
        btn_info.place(x=350, y=70, width=60, height=25)

    def show_info(self):
        msg = "Найди работу!"
        mb.showinfo("Ты серьёзно?", msg)

    def start(self):
        btn = Button(root, text="Туз(1)", bg="#4f92f1", font=("Comic Sans MS", 15),
                     command=lambda x=1: self.btn_click(x))
        btn2 = Button(root, text="Вишня(2)", bg="#4f92f1", font=("Comic Sans MS", 15),
                      command=lambda x=2: self.btn_click(x))
        btn3 = Button(root, text="Три(3)", bg="#4f92f1", font=("Comic Sans MS", 15),
                      command=lambda x=3: self.btn_click(x))

        btn.place(x=10, y=100, width=120, height=50)
        btn2.place(x=155, y=100, width=120, height=50)
        btn3.place(x=300, y=100, width=120, height=50)

        self.lbl = Label(root, text="Ты экстрасенс?", bg="#f0f8ff", font=("Comic Sans MS", 23, "bold"))
        self.lbl.place(x=160, y=20)

        self.win = self.lose = 0

        self.lbl2 = Label(root, justify="left", font=("Comic Sans MS", 13),
                         text=f"Было угадано: {self.win}\nБыло больно:"
                              f" {self.lose}",
                         bg="#f0f8ff")
        self.lbl2.place(x=5, y=20)

    def btn_click(self, choise):
        comp_choise = rdm.randint(1, 3)
        self.lbl3 = Label(root, justify="left", font=("Comic Sans MS", 13),
                          text=f"Загадано: {comp_choise}", bg="#f0f8ff")
        self.lbl3.place(x=220, y=3)
        self.lbl4 = Label(root, justify="left", font=("Comic Sans MS", 13),
                          text=f"Выбрано: {choise}", bg="#f0f8ff")
        self.lbl4.place(x=220, y=70)
        if choise == comp_choise:
            self.win += 1
            self.lbl.configure(text="Верно!")
        else:
            self.lose += 1
            self.lbl.configure(text="ϟУдар токомϟ")

        self.lbl2.configure(text=f"Было угадано: {self.win}\nБыло больно:"
                              f" {self.lose}")

        del comp_choise


if __name__ == '__main__':
    root = Tk()
    root.geometry("430x160+200+200")
    root.title("А не экстрасенс ли я?")
    root["bg"] = "#f0f8ff"
    app = Main(root)
    app.pack()
    root.mainloop()
