from tkinter import *

root = Tk()
root.configure(bg="#91bac4")

x_height = 40
y_width = 20
long_width = 35
entry_borderwidth = 5
bg_color ='#7eb5c2'

entry_space = Entry(root,width=long_width, borderwidth=entry_borderwidth)
entry_space.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def onClick(number):
    current = entry_space.get()
    entry_space.delete(0, END)
    entry_space.insert(0, str(current)+ str(number))

def onClick_add():
    first_number= entry_space.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry_space.delete(0,END)

def onClick_sub():
    first_number= entry_space.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    entry_space.delete(0,END)

def onClick_mult():
    first_number= entry_space.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry_space.delete(0,END)

def onClick_div():
    first_number= entry_space.get()
    global f_num
    global math
    math = "divition"
    f_num = int(first_number)
    entry_space.delete(0,END)


def onClick_delete():
    entry_space.delete(0, END)


def onClikc_procces():
    second_number = entry_space.get()
    entry_space.delete(0, END)

    if math == "addition":
        entry_space.insert(0, f_num + int(second_number))

    if math == "substraction":
        entry_space.insert(0, f_num - int(second_number))

    if math == "multiplication":
        entry_space.insert(0, f_num * int(second_number))

    if math == "divition":
        entry_space.insert(0, f_num / int(second_number))




myButton1 = Button(root, bg=bg_color, text=1 ,padx=x_height ,pady=y_width, command=lambda:onClick(1) ).grid(row=1 ,column=0 )
myButton2 = Button(root, bg=bg_color, text=2 ,padx=x_height ,pady=y_width, command=lambda:onClick(2) ).grid(row=1 ,column=1 )
myButton3 = Button(root, bg=bg_color, text=3 ,padx=x_height ,pady=y_width, command=lambda:onClick(3) ).grid(row=1 ,column=2 )

myButton4 = Button(root, bg=bg_color, text=4 ,padx=x_height ,pady=y_width, command=lambda:onClick(4) ).grid(row=2 ,column=0 )
myButton5 = Button(root, bg=bg_color, text=5 ,padx=x_height ,pady=y_width, command=lambda:onClick(5) ).grid(row=2 ,column=1 )
myButton6 = Button(root, bg=bg_color, text=6 ,padx=x_height ,pady=y_width, command=lambda:onClick(6) ).grid(row=2 ,column=2 )

myButton7 = Button(root, bg=bg_color, text=7 ,padx=x_height ,pady=y_width, command=lambda:onClick(7) ).grid(row=3 ,column=0 )
myButton8 = Button(root, bg=bg_color, text=8 ,padx=x_height ,pady=y_width, command=lambda:onClick(8) ).grid(row=3 ,column=1 )
myButton9 = Button(root, bg=bg_color, text=9 ,padx=x_height ,pady=y_width, command=lambda:onClick(9) ).grid(row=3 ,column=2 )

myButton0 = Button(root, bg=bg_color, text=0 ,padx=x_height ,pady=y_width, command=lambda:onClick(0) ).grid(row=4 ,column=0 )
myButton_add = Button(root, bg=bg_color, text="+" ,padx=39 ,pady=y_width, command=onClick_add ).grid(row=4 ,column=1 )
myButton_sub = Button(root, bg=bg_color, text="-" ,padx=41 ,pady=y_width, command=onClick_sub ).grid(row=4 ,column=2 )

myButton_multipy = Button(root, bg=bg_color, text="*" ,padx=x_height ,pady=y_width, command=onClick_mult ).grid(row=5 ,column=0 )
myButton_divide = Button(root, bg=bg_color, text="/" ,padx=41 ,pady=y_width, command=onClick_div ).grid(row=5 ,column=1 )
myButton_clear = Button(root, bg=bg_color, text="C" ,padx=x_height ,pady=y_width, command=onClick_delete ).grid(row=5 ,column=2 )

myButton_enter = Button(root, bg="#5eb1c4", text="enter" ,padx=x_height ,pady=y_width, width=long_width, command=onClikc_procces ).grid(row=6, column=0, columnspan=3, padx=10, pady=10)


root.mainloop()