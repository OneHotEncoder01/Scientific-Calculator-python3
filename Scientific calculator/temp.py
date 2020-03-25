from tkinter import *


root = Tk()
root.title("Scientific rootulator")
root.configure(background="#d3dbd3")
root.resizable(width = False, height = False)
root.geometry("480x568+0+0")

textDisplay = Entry(root, font=('arial',20), bg = "#d3dbd3", bd = 12, width = 30, justify=RIGHT)
textDisplay.grid(row=0, column=0, columnspan = 4, pady=1)
textDisplay.insert(0,"0")

numberpad = "789456123"
i = 0
buttons = []
for j in range(2,5):
		for k in range(3):
			buttons.append(Button(root , width=6, height=2, font=('arial',20,'bold'), bd = 4, text = numberpad[i]))
			buttons[i].grid(row=j, column=k, pady = 1)
			i += 1

def Scientific():
	scientific_calc.main()
	root.destroy()


def Standart():
	return

def Exit_m():
	return

menubar = Menu(root)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu =filemenu)
filemenu.add_command(label = "Standart", command = Standart)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = Exit_m)

editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu=editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_command(label = "Paste")

helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu=helpmenu)
helpmenu.add_command(label = "View Help")

root.configure(menu = menubar)
root.mainloop()
