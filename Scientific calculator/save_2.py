from tkinter import*
import math
import parser
import tkinter.messagebox
import sys



def main():

	root = Tk()
	root.title("Scientific calculator")
	root.configure(background="#d3dbd3")
	root.resizable(width = False, height = False)
	root.geometry("480x568+0+0")

	class Calc():
		def __init__(self):
			self.total = 0
			self.current = ''
			self.input_values = True
			self.check_sum = False
			self.op = ''
			self.result = False
#makes the number appier in the entry box-----------------
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
				self.total = float(txtDisplay.get())
				
		def display(self, value):
			textDisplay.delete(0, END)
			textDisplay.insert(0, value)


		def valid_function(self):
			if self.op == "add":
				self.tdotal += self.current
			if self.op == "sub":
				self.total -= self.current
			if self.op == "multi":
				self.total *= self.current
			if self.op == "divide":
				self.total /= self.current
			if self.op == "mod":
				self.total %= self.current
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

#--------------------------------------------------------------



	added_value = Calc()


	textDisplay = Entry(root, font=('arial',20), bg = "#d3dbd3", bd = 12, width = 30, justify=RIGHT, foreground="black")
	textDisplay.grid(row=0, column=0, columnspan = 4, pady=1)
	textDisplay.insert(0,"0")

	numberpad = "789456123"
	i = 0
	buttons = []
	for j in range(2,5):
			for k in range(3):
				buttons.append(Button(root, width=6, height=2, font=('arial',20,'bold'), bd = 4, text = numberpad[i]))
				buttons[i].grid(row=j, column=k, pady = 1)
				buttons[i]["command"] = lambda x=numberpad [i]: added_value.numberEnter(x)
				i +=1

	button_clear = Button(root, text=chr(67), width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#646664", bd = 4).grid(row=1, column=0, pady=1)
	button_clear_All = Button(root, text=chr(67) + chr(69), width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#646664", bd = 4).grid(row=1, column=1, pady=1)

	button_sr = Button(root, text="√", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#646664", bd = 4).grid(row=1, column=2, pady=1)
	button_Add = Button(root, text="+", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#646664", bd = 4).grid(row=1, column=3, pady=1)

	button_Sub = Button(root, text="-", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#646664", bd = 4).grid(row=2, column=3, pady=1)
	button_Multy = Button(root, text="*", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#646664", bd = 4).grid(row=3, column=3, pady=1)
	button_Div = Button(root, text=chr(247), width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#646664", bd = 4).grid(row=4, column=3, pady=1)

	button_zero = Button(root, text="0", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#646664", bd = 4, command = lambda:added_value.numberEnter(0)).grid(row=5, column=0, pady=1)
	button_Dot = Button(root, text=".", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#646664", bd = 4).grid(row=5, column=1, pady=1)
	button_Pm = Button(root, text=chr(177), width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#646664", bd = 4).grid(row=5, column=2, pady=1)
	button_Equal = Button(root, text="=", width = 6, height=2, font=('arial',20,'bold'),
						  bg = "#646664", bd = 4).grid(row=5, column=3, pady=1)
	# Menu

	def Exit_m():
		Exit_m = tkinter.messagebox.askyesno("Scientific rootulator","confirm if you want to exit")
		if Exit_m > 0:
			root.destroy()
			return

	menubar = Menu(root)

	filemenu = Menu(menubar, tearoff = 0)
	menubar.add_cascade(label = "File", menu =filemenu)
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