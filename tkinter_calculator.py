'''tkinter Calculator app '''

# Using Entry widget to create first gui application...


#importing module creating window
from tkinter import *
root = Tk ()
root.title ('Calculator')
root.configure (bg = 'black')

#global variables
var_num1 = 0
opr = None


#defining the number function
def button_click (x) :
    init_txt = inp_field.get ()
    inp_txt = str (init_txt) + str (x)
    inp_field.delete (0, END)
    inp_field.insert (0, inp_txt)
    return


#defining the clear function
def button_clear () :
    inp_field.delete (0, END)
    return


#defining the operator functions
        
def button_add () :
    global var_num1, opr
    var_num1 = inp_field.get ()
    opr = '+'
    inp_field.delete (0, END)
    return

def button_subt () :
    global var_num1, opr
    var_num1 = inp_field.get ()
    opr = '-'
    inp_field.delete (0, END)
    return

def button_mult () :
    global var_num1, opr
    var_num1 = inp_field.get ()
    opr = '*'
    inp_field.delete (0, END)
    return

def button_div () :
    global var_num1, opr
    var_num1 = inp_field.get ()
    opr = '/'
    inp_field.delete (0, END)
    return


#defining the equal function
def button_equal () :
    var_num2 = inp_field.get ()
    inp_field.delete (0, END)
    
    try :
        if opr == '+' :
            ans = int (var_num1) + int (var_num2)
        if opr == '-' :
            ans = int (var_num1) - int (var_num2)
        if opr == '*' :
            ans = int (var_num1) * int (var_num2)
        if opr == '/' :
            ans = int (var_num1) / int (var_num2)
    except :
        ans = 'Invalid input !!'
        
    inp_field.insert (0, ans)
    return
    
#defining quit command
def calc_close () :
    root.destroy ()
    return


#defining the widgets
inp_field = Entry (root, width = 35, borderwidth = 5)

button_1 = Button (root, text = '1', command = lambda : button_click (1), padx = 40, pady = 20)
button_2 = Button (root, text = '2', command = lambda : button_click (2), padx = 40, pady = 20)
button_3 = Button (root, text = '3', command = lambda : button_click (3), padx = 40, pady = 20)

button_4 = Button (root, text = '4', command = lambda : button_click (4), padx = 40, pady = 20)
button_5 = Button (root, text = '5', command = lambda : button_click (5), padx = 40, pady = 20)
button_6 = Button (root, text = '6', command = lambda : button_click (6), padx = 40, pady = 20)

button_7 = Button (root, text = '7', command = lambda : button_click (7), padx = 40, pady = 20)
button_8 = Button (root, text = '8', command = lambda : button_click (8), padx = 40, pady = 20)
button_9 = Button (root, text = '9', command = lambda : button_click (9), padx = 40, pady = 20)

button_0 = Button (root, text = '0', command = lambda : button_click (0), padx = 40, pady = 20)
button_add = Button (root, text = '+', command = button_add, padx = 39, pady = 20)
button_subtract = Button (root, text = '-', command = button_subt, padx = 40, pady = 20)

button_equal = Button (root, text = '=', command = button_equal, padx = 39, pady = 20)
button_multiply = Button (root, text = '*', command = button_mult, padx = 42, pady = 20)
button_divide = Button (root, text = '/', command = button_div, padx = 43, pady = 20)

button_clear = Button (root, text = 'Clear', command = button_clear, padx = 79, pady = 20)
button_quit = Button (root, text = 'Quit', command = calc_close, padx = 32, pady = 20)


#displaying them on the screen
inp_field.grid (row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
button_1.grid (row = 3, column = 0)
button_2.grid (row = 3, column = 1)
button_3.grid (row = 3, column = 2)

button_4.grid (row = 2, column = 0)
button_5.grid (row = 2, column = 1)
button_6.grid (row = 2, column = 2)

button_7.grid (row = 1, column = 0)
button_8.grid (row = 1, column = 1)
button_9.grid (row = 1, column = 2)

button_0.grid (row = 4, column = 1)
button_add.grid (row = 4, column = 0)
button_subtract.grid (row = 4, column = 2)

button_equal.grid (row = 5, column = 2)
button_multiply.grid (row = 5, column = 0)
button_divide.grid (row = 5, column = 1)

button_quit.grid (row = 6, column = 0)
button_clear.grid (row = 6, column = 1, columnspan = 2)


#the event loop
root.mainloop ()
