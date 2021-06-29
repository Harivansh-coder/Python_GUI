from tkinter import *


master = Tk()
master.title("calculator")

screen = Entry(master, width = 35,borderwidth = 5)
screen.grid(row=0, column=0,columnspan = 4,padx = 10,pady = 5)

# number input functions
def number_in(number):
    current_screen = screen.get()
    screen.delete(0,END)
    screen.insert(0,current_screen + number)

# clear and equal button

def clear_screen():
    screen.delete(0,END)

def result():
    current = screen.get()
    if "+" in  current:
        i = current.index("+")
        operand1 = float(current[:i])
        operand2 = float(current[i + 1:len(current)])
        clear_screen()
        screen.insert(0,str(operand1 + operand2))

    elif "-" in current:
        i = current.index("-")
        operand1 = float(current[:i])
        operand2 = float(current[i + 1:len(current)])
        clear_screen()
        screen.insert(0,str(operand1 - operand2))

    elif "/" in current:
        i = current.index("/")
        operand1 = float(current[:i])
        operand2 = float(current[i + 1:len(current)])
        clear_screen()
        screen.insert(0,str(operand1 / operand2))

    else:
        i = current.index("*")
        operand1 = float(current[:i])
        operand2 = float(current[i + 1:len(current)])
        clear_screen()
        screen.insert(0,str(operand1 * operand2))



#number button

Button(master, text ="1",height = 2,width = 5,command = lambda :number_in("1")).grid(row=1, column=0,padx = 10,pady = 5)
Button(master, text ="2",height = 2,width = 5,command = lambda :number_in("2")).grid(row=1, column=1,padx = 10,pady = 5)
Button(master, text ="3",height = 2,width = 5,command = lambda :number_in("3")).grid(row=1, column=2,padx = 10,pady = 5)
Button(master, text ="4",height = 2,width = 5,command = lambda :number_in("4")).grid(row=2, column=0,padx = 10,pady = 5)
Button(master, text ="5",height = 2,width = 5,command = lambda :number_in("5")).grid(row=2, column=1,padx = 10,pady = 5)
Button(master, text ="6",height = 2,width = 5,command = lambda :number_in("6")).grid(row=2, column=2,padx = 10,pady = 5)
Button(master, text ="7",height = 2,width = 5,command = lambda :number_in("7")).grid(row=3, column=0,padx = 10,pady = 5)
Button(master, text ="8",height = 2,width = 5,command = lambda :number_in("8")).grid(row=3, column=1,padx = 10,pady = 5)
Button(master, text ="9",height = 2,width = 5,command = lambda :number_in("9")).grid(row=3, column=2,padx = 10,pady = 5)
Button(master, text ="0",height = 2,width = 5,command = lambda :number_in("0")).grid(row=4, column=1,padx = 10,pady = 5)

# operators button

Button(master, text ="+",height = 2,width = 5,command = lambda :number_in("+")).grid(row=1, column=3,padx = 10,pady = 5)
Button(master, text ="-",height = 2,width = 5,command = lambda :number_in("-")).grid(row=2, column=3,padx = 10,pady = 5)
Button(master, text ="/",height = 2,width = 5,command = lambda :number_in("/")).grid(row=3, column=3,padx = 10,pady = 5)
Button(master, text ="*",height = 2,width = 5,command = lambda :number_in("*")).grid(row=4, column=3,padx = 10,pady = 5)
Button(master, text ="clear",command = clear_screen,height = 2,width = 5).grid(row=4, column=0,padx = 10,pady = 5)
Button(master, text ="=",height = 2,width = 5,command = result).grid(row=4, column=2,padx = 10,pady = 5)


master.mainloop()
