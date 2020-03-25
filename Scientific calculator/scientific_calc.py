from tkinter import*
import math
import parser
import tkinter.messagebox
import sys

import main_calc

def main():
	root = Tk()
	root.title("Scientific Calculator")
	root.configure(background="#d3dbd3")
	root.resizable(width = False, height = False)
	root.geometry("1022x568+0+0")
	calc = Frame(root)
	calc.grid()


	class Calc():
		def __init__(self):
			self.total = 0
			self.current = ''
			self.input_values = True
			self.check_sum = False
			self.op = ''
			self.result = False

		def sec(self):
			sec = 1 / float()

		def numberEnter(self,num):
			self.result = False
			firstnum = textDisplay.get()
			secondnum = str(num)
			if self.input_values:
				self.current = secondnum
				self.input_values = False
			else:
				if secondnum == '.':
					if secondnum in firstnum:
						return
				self.current = firstnum + secondnum
			self.display(self.current)

		def sum_of_total(self):
			self.result = True
			self.current = float(self.current)
			if self.check_sum == True:
				self.valid_function()
			else:
				self.total = float(textDisplay.get())

		def display(self, value):
			textDisplay.delete(0, END)
			textDisplay.insert(0, value)


		def valid_function(self):
			if self.op == "add":
				self.total += self.current
			if self.op == "sub":
				self.total -= self.current
			if self.op == "multi":
				self.total *= self.current
			if self.op == "divide":
				self.total /= self.current
			if self.op == "mod":
				self.total %= self.current
			if self.op == "percent":
				self.total = 100/(self.total + self.current)
			self.input_values = True
			self.check_sum = False
			self.display(self.total)


		def opration(self, op):
			self.current = float(self.current)
			if self.check_sum:
				self.valid_function()
			elif not self.result:
				self.total = self.current
				self.input_values = True
			self.check_sum = True
			self.op = op
			self.result = False

		def pi(self):
			self.result = False
			self.current = math.pi
			self.display(self.current)

		def tau(self):
			self.result = False
			self.current = math.tau
			self.display(self.current)

		def e(self):
			self.result = False
			self.current = math.e
			self.display(self.current)

		def phi(self):
			self.result = False
			self.current = float(1.61803398874989484820)
			self.display(self.current)

		def walles(self):
			self.result = False
			self.current = walles = float(2.09455148154232659148)
			self.display(self.current)

		def laplace(self):
			self.result = False
			self.current = laplace = float(0.66274341934918158097)
			self.display(self.current)

		def sec(self):
			self.result = False
			self.current = sec = 1/math.cos(math.radians(float(textDisplay.get())))
			self.display(self.current)

		def sin(self):
			self.result = False
			self.current = math.sin(math.radians(float(textDisplay.get())))
			self.display(self.current)

		def csc(self):
			self.result = False
			self.current = csc = 1/math.sin(math.radians(float(textDisplay.get())))
			self.display(self.current)

		def cos(self):
			self.result = False
			self.current =math.cos(math.radians(float(textDisplay.get())))
			self.display(self.current)

		def tan(self):
			self.result = False
			self.current = math.tan(math.radians(float(textDisplay.get())))
			self.display(self.current)

		def cot(self):
			self.result = False
			self.current = math.cot(math.radians(float(textDisplay.get())))
			self.display(self.current)

		def mathsPM(self):
			self.result = False
			self.current = -(float(textDisplay.get()))
			self.display(self.current)

		def squared(self):
			self.result = False
			self.current = math.sqrt(float(textDisplay.get()))
			self.display(self.current)

		def ceil(self):
			self.result = False
			self.current = math.ceil(float(textDisplay.get()))
			self.display(self.current)

		def floor(self):
			self.result = False
			self.current = math.floor(float(textDisplay.get()))
			self.display(self.current)	

		def log(self):
			self.result = False
			self.current = math.lgamma(float(textDisplay.get()))
			self.display(self.current)

	added_value = Calc()



	textDisplay = Entry(calc, font=('arial',20), bg = "#d3dbd3", bd = 12, width = 30, justify=RIGHT, foreground="black")
	textDisplay.grid(row=0, column=0, columnspan = 8, pady=1)
	textDisplay.insert(0,"0")
	numberpad = "789456123"
	i = 0
	buttons = []
	for j in range(2,5):
		for k in range(3):
			buttons.append(Button(calc, width=6, height=2, font=('arial',20,'bold'), bd = 4, text = numberpad[i]))
			buttons[i].grid(row=j, column = k, pady = 1)
			buttons[i]["command"] = lambda x = numberpad [i]: added_value.numberEnter(x)
			i +=1
	def Exit_m():
		Exit_m = tkinter.messagebox.askyesno("Scientific Calculator","confirm if you want to exit")
		if Exit_m > 0:
			root.destroy()
			return
#column_0---------------------------------------------------------------------------------------------------------------
	button_clear = Button(calc, text=chr(67), width = 6, height=2, font=('arial',20,'bold'),
					  	  bg = "#68706c", bd = 4).grid(row=1, column=0, pady=1)
	button_zero = Button(calc, text="0", width = 6, height=2, font=('arial',20,'bold'),
						  bd = 4, command = lambda:added_value.numberEnter(0)).grid(row=5, column=0, pady=1)
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
						  bg = "#68706c", bd = 4, command = added_value.mathsPM).grid(row=5, column=2, pady=1)
	button_sr = Button(calc, text="√", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4, command = added_value.squared).grid(row=1, column=2, pady=1)
	button_max = Button(calc, text="max", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4).grid(row=6, column=2, pady=1)
#column_3---------------------------------------------------------------------------------------------------------------
	button_Add = Button(calc, text="+", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4, command = lambda: added_value.opration("add")).grid(row=1, column=3, pady=1)
	button_Sub = Button(calc, text="-", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4, command = lambda: added_value.opration("sub")).grid(row=4, column=3, pady=1)
	button_Multy = Button(calc, text="*", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4, command = lambda: added_value.opration("multi")).grid(row=3, column=3, pady=1)
	button_Div = Button(calc, text=chr(247), width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4, command = lambda: added_value.opration("divide")).grid(row=2, column=3, pady=1)
	button_Equal = Button(calc, text="=", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#68706c", bd = 4, command = added_value.sum_of_total).grid(row=6, column=3, pady=1)
	button_power = Button(calc, text='x²', width = 6, height=2, font=('arial',20,'bold'),
					  bg = "#68706c", bd = 4).grid(row=5, column=3, pady=1)
#column_4---------------------------------------------------------------------------------------------------------------
	button_factorial = Button(calc, text="!", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=1, column=4, pady=1)
	button_e = Button(calc, text="e", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4, command = added_value.e).grid(row=4, column=4, pady=1)
	button_pi = Button(calc, text='\u03C0', width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4, command = added_value.pi).grid(row=3, column=4, pady=1)
	button_ln = Button(calc, text="ln", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=2, column=4, pady=1)
	button_abs = Button(calc, text="|x|", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=5, column=4, pady=1)
	button_round = Button(calc, text="≈", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=6, column=4, pady=1)
#column_5---------------------------------------------------------------------------------------------------------------
	button_10 = Button(calc, text="n^10" + chr(69), width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=6, column=5, pady=1)
	button_nPr = Button(calc, text='nPr', width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=3, column=5, pady=1)
	button_nCr= Button(calc, text='nCr', width = 6, height=2, font=('arial',20,'bold'),
					  bg = "#787780", bd = 4).grid(row=4, column=5, pady=1)
	button_gcd = Button(calc, text="gcd" + chr(69), width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=5, column=5, pady=1)
	button_2pi = Button(calc, text="2"+'\u03C0', width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4,command = added_value.tau).grid(row=2, column=5, pady=1)
	button_ceil = Button(calc, text='ceil', width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4, command = added_value.ceil).grid(row=1, column=5, pady=1)
#column_6---------------------------------------------------------------------------------------------------------------
	button_mod = Button(calc, text="mod", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4).grid(row=1, column=6, pady=1)
	button_log = Button(calc, text="log(​x)", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4, command = added_value.log).grid(row=2, column=6, pady=1)
	button_floor = Button(calc, text="floor", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4, command = added_value.floor).grid(row=3, column=6, pady=1)
	button_sec = Button(calc, text='sec()', width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4, command = added_value.sec).grid(row=5, column=6, pady=1)
	button_phi = Button(calc, text='Φ', width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4, command = added_value.phi).grid(row=6, column=6, pady=1)
	button_csc = Button(calc, text="csc()", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4, command = added_value.csc).grid(row=4, column=6, pady=1)
#column_7---------------------------------------------------------------------------------------------------------------	
	button_sin = Button(calc, text="sin()", width = 8, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4, command = added_value.sin).grid(row=1, column=7, pady=1)
	button_cos = Button(calc, text="cos()", width = 8, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4, command = added_value.cos).grid(row=2, column=7, pady=1)
	button_tan = Button(calc, text="tan()", width = 8, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4, command = added_value.tan).grid(row=3, column=7, pady=1)
	button_cot = Button(calc, text='cot()', width = 8, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4, command = added_value.cot).grid(row=4, column=7, pady=1)
	button_walles = Button(calc, text="W", width = 8, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4, command = added_value.walles).grid(row=5, column=7, pady=1)
	button_laplace = Button(calc, text='ℒ', width = 8, height=2, font=('arial',20,'bold'),
						  bg = "#787780", bd = 4, command = added_value.laplace).grid(row=6, column=7, pady=1)
#modules-------------------------------------------------------------------------------------------------------------
	def Scientific():
		root.destroy()	
		scientific_calc.main()
		return
	def Standart():
		root.destroy()
		main_calc.main()
		return
#Menu-------------------------------------------------------------------------------------------------------------------
	menubar = Menu(calc)
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
	root.configure(menu=menubar)
	root.mainloop()
if __name__ == '__main__':
	main()