from tkinter import*
import math
import parser
import tkinter.messagebox
import sys


def main():
	root = Tk()
	root.title("Scientific Calculator")
	root.configure(background="#d3dbd3")
	root.resizable(width = False, height = False)
	root.geometry("1022x568+0+0")

	calc = Frame(root)
	calc.grid()

	textDisplay = Entry(calc, font=('arial',20), bg = "#d3dbd3", bd = 12, width = 30, justify=RIGHT)
	textDisplay.grid(row=0, column=0, columnspan = 8, pady=1)
	textDisplay.insert(0,"0")

	numberpad = "789456123"
	i = 0
	buttons = []
	for j in range(2,5):
		for k in range(3):
			buttons.append(Button(calc, width=6, height=2, font=('arial',20,'bold'), bd = 4, text = numberpad[i]))
			buttons[i].grid(row=j, column=k, pady = 1)

			i +=1


	def Scientific():
		scientific_calc.main()

	def Exit_m():
		Exit_m = tkinter.messagebox.askyesno("Scientific Calculator","confirm if you want to exit")
		if Exit_m > 0:
			root.destroy()
			return
#column_0---------------------------------------------------------------------------------------------------------------
	button_clear = Button(calc, text=chr(67), width = 6, height=2, font=('arial',20,'bold'),
					  	  bg = "#68706c", bd = 4).grid(row=1, column=0, pady=1)
	button_zero = Button(calc, text="0", width = 6, height=2, font=('arial',20,'bold'),
						  bd = 4).grid(row=5, column=0, pady=1)
	button_percent = Button(calc, text="%", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4).grid(row=6, column=0, pady=1)
#column_1---------------------------------------------------------------------------------------------------------------
	button_clear_All = Button(calc, text="CE", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4).grid(row=1, column=1, pady=1)
	button_Dot = Button(calc, text=".", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4).grid(row=5, column=1, pady=1)
	button_min = Button(calc, text="min", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4).grid(row=6, column=1, pady=1)
#column_2---------------------------------------------------------------------------------------------------------------
	button_Pm = Button(calc, text=chr(177), width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4).grid(row=5, column=2, pady=1)
	button_sr = Button(calc, text="√", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4).grid(row=1, column=2, pady=1)
	button_max = Button(calc, text="max", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4).grid(row=6, column=2, pady=1)
#column_3---------------------------------------------------------------------------------------------------------------
	button_Add = Button(calc, text="+", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4).grid(row=1, column=3, pady=1)
	button_Sub = Button(calc, text="-", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4).grid(row=4, column=3, pady=1)
	button_Multy = Button(calc, text="*", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4).grid(row=3, column=3, pady=1)
	button_Div = Button(calc, text=chr(247), width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4).grid(row=2, column=3, pady=1)
	button_Equal = Button(calc, text="=", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4).grid(row=6, column=3, pady=1)
	button_power = Button(calc, text='x²', width = 6, height=2, font=('arial',20,'bold'),
					  bg = "#68706c", bd = 4).grid(row=5, column=3, pady=1)
#column_4---------------------------------------------------------------------------------------------------------------
	button_factorial = Button(calc, text="!", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=1, column=4, pady=1)
	button_e = Button(calc, text="e", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=4, column=4, pady=1)
	button_pi = Button(calc, text='\u03C0', width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=3, column=4, pady=1)
	button_ln = Button(calc, text="ln", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=2, column=4, pady=1)
	button_abs = Button(calc, text="|x|", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=5, column=4, pady=1)
	button_round = Button(calc, text="≈", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=6, column=4, pady=1)
#column_5---------------------------------------------------------------------------------------------------------------
	button_10 = Button(calc, text="n^0" + chr(69), width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=6, column=5, pady=1)
	button_nPr = Button(calc, text='nPr', width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=3, column=5, pady=1)
	button_nCr= Button(calc, text='nCr', width = 6, height=2, font=('arial',20,'bold'),
					  bg = "#787780", bd = 4).grid(row=4, column=5, pady=1)
	button_gcd = Button(calc, text="gcd" + chr(69), width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=5, column=5, pady=1)
	button_lcm = Button(calc, text="lcm", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=2, column=5, pady=1)
	button_ceil = Button(calc, text='ceil', width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=1, column=5, pady=1)
#column_6---------------------------------------------------------------------------------------------------------------
	button_mod = Button(calc, text="mod", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=1, column=6, pady=1)
	button_log = Button(calc, text="log(​x)", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=2, column=6, pady=1)
	button_floor = Button(calc, text="floor", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=3, column=6, pady=1)
	button_sec = Button(calc, text='sec()', width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=5, column=6, pady=1)
	button_mu = Button(calc, text='μ', width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=6, column=6, pady=1)
	button_csc = Button(calc, text="csc()", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=4, column=6, pady=1)
#column_7---------------------------------------------------------------------------------------------------------------	
	button_sin = Button(calc, text="sin()", width = 8, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=1, column=7, pady=1)
	button_cos = Button(calc, text="cos()", width = 8, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=2, column=7, pady=1)
	button_tan = Button(calc, text="tan()", width = 8, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=3, column=7, pady=1)
	button_cot = Button(calc, text='cot()', width = 8, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=4, column=7, pady=1)
#Menu-------------------------------------------------------------------------------------------------------------------
	menubar = Menu(calc)

	filemenu = Menu(menubar, tearoff = 0)
	menubar.add_cascade(label = "File", menu =filemenu)
	filemenu.add_command(label = "Standart")
	filemenu.add_command(label = "Scientific")
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


	root.configure(menu=menubar)
	root.mainloop()

if __name__ == '__main__':
	main()