from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap()
root.title('ATM Rea Bank')
root.configure(bg='#e0f5ff')
root.geometry('700x800')
root.resizable(False, False)

# Label for logo Rea Bank
logo_reabank = ImageTk.PhotoImage(Image.open('Img/Logo.jpg'))
img_reabank = Label(image=logo_reabank)
img_reabank.place(x=10, y=10)

# Labels for explanation
explanation_1  = Label(root, text='- Voer een bedrag in tot \N{euro sign}200',
                  font='Arial 9 bold', bg='#e0f5ff', fg='blue')
explanation_2  = Label(root, text='- U kunt de muntselectie aanpassen voor' + 
                       ' een herbereking', font='Arial 9 bold', bg='#e0f5ff', 
                       fg='blue')
explanation_3  = Label(root, text='- Voor een nieuwe berekening, klik op ' + 
                       'nieuw bedrag', font='Arial 9 bold', bg='#e0f5ff', 
                       fg='blue')

explanation_1.place(x=245, y=20)
explanation_2.place(x=245, y=50)
explanation_3.place(x=245, y=80)

# Images coins
photo_2 = ImageTk.PhotoImage(Image.open('Img/2_euro.jpg'))
photo_1 = ImageTk.PhotoImage(Image.open('Img/1_euro.jpg'))
photo_50 = ImageTk.PhotoImage(Image.open('Img/50_euro.jpg'))
photo_20 = ImageTk.PhotoImage(Image.open('Img/20_euro.jpg'))
photo_10 = ImageTk.PhotoImage(Image.open('Img/10_euro.jpg'))
photo_05 = ImageTk.PhotoImage(Image.open('Img/05_euro.jpg'))
photo_02 = ImageTk.PhotoImage(Image.open('Img/02_euro.jpg'))
photo_01 = ImageTk.PhotoImage(Image.open('Img/01_euro.jpg'))

img_2 = Label(image=photo_2, borderwidth=0)
img_1 = Label(image=photo_1, borderwidth=0)
img_50 = Label(image=photo_50, borderwidth=0)
img_20 = Label(image=photo_20, borderwidth=0)
img_10 = Label(image=photo_10, borderwidth=0)
img_05 = Label(image=photo_05, borderwidth=0)
img_02 = Label(image=photo_02, borderwidth=0)
img_01 = Label(image=photo_01, borderwidth=0)

img_2.place(x=10, y=250)
img_1.place(x=10, y=313)
img_50.place(x=7, y=370)
img_20.place(x=10, y=433)
img_10.place(x=13, y=495)
img_05.place(x=12, y=553)
img_02.place(x=12, y=613)
img_01.place(x=12, y=673)

# Labels for coin-scores
score_2  = Label(root, text='0 x', font='Arial 16 bold', bg='#e0f5ff', fg='blue')
score_1  = Label(root, text='0 x', font='Arial 16 bold', bg='#e0f5ff', fg='blue')
score_50 = Label(root, text='0 x', font='Arial 16 bold', bg='#e0f5ff', fg='blue')
score_20 = Label(root, text='0 x', font='Arial 16 bold', bg='#e0f5ff', fg='blue')
score_10 = Label(root, text='0 x', font='Arial 16 bold', bg='#e0f5ff', fg='blue')
score_05  = Label(root, text='0 x', font='Arial 16 bold', bg='#e0f5ff', fg='blue')
score_02  = Label(root, text='0 x', font='Arial 16 bold', bg='#e0f5ff', fg='blue')
score_01  = Label(root, text='0 x', font='Arial 16 bold', bg='#e0f5ff', fg='blue')

score_2.place(x=75, y=260)
score_1.place(x=75, y=320)
score_50.place(x=75, y=380)
score_20.place(x=75, y=440)
score_10.place(x=75, y=500)
score_05.place(x=75, y=560)
score_02.place(x=75, y=620)
score_01.place(x=75, y=680)

# Labels for total coins, remaining amount and validate input
total_coins = Label(root, text='', font='Arial 16 bold',bg='#e0f5ff', fg='blue')
total_coins.place(x=10, y=740)

remaining_amount = Label(root, text='', font='Arial 16 bold',bg='#e0f5ff', 
                         fg='blue')
remaining_amount.place(x=230, y=740)

validate_input = Label(root, text='', font='Arial 16 bold',bg='#e0f5ff', 
                       fg='blue')
validate_input.place(x=400, y=740)

# Checkboxes to select coins + variables

var_2 = IntVar()
var_1 = IntVar()
var_50 = IntVar()
var_20 = IntVar()
var_10 = IntVar()
var_05 = IntVar()
var_02 = IntVar()
var_01 = IntVar()

button_coin_2 = Checkbutton(root, text='2', font='Arial 16 bold', 
                                  bg='gold',  fg='blue', variable=var_2)
button_coin_2.place(x=400, y=140)


button_coin_1 = Checkbutton(root, text='1', font='Arial 16 bold', 
                                  bg='gold',  fg='blue', variable=var_1)
button_coin_1.place(x=400, y=200)


button_coin_50 = Checkbutton(root, text='0,50', font='Arial 16 bold', 
                                   bg='gold',  fg='blue', variable=var_50)
button_coin_50.place(x=400, y=260)


button_coin_20 = Checkbutton(root, text='0,20', font='Arial 16 bold', 
                                   bg='gold',  fg='blue', variable=var_20)
button_coin_20.place(x=400, y=320)


button_coin_10 = Checkbutton(root, text='0,10', font='Arial 16 bold', 
                                   bg='gold',  fg='blue', variable=var_10)
button_coin_10.place(x=400, y=380)


button_coin_05 = Checkbutton(root, text='0,05', font='Arial 16 bold', 
                                   bg='gold',  fg='blue', variable=var_05)
button_coin_05.place(x=400, y=440)


button_coin_02 = Checkbutton(root, text='0,02', font='Arial 16 bold', 
                                   bg='gold',  fg='blue', variable=var_02)
button_coin_02.place(x=400, y=500)


button_coin_01 = Checkbutton(root, text='0,01', font='Arial 16 bold', 
                                   bg='gold',  fg='blue', variable=var_01)
button_coin_01.place(x=400, y=560)

# Select all coins by start app

button_coin_2.select()
button_coin_1.select()
button_coin_50.select()
button_coin_20.select()
button_coin_10.select()
button_coin_05.select()
button_coin_02.select()
button_coin_01.select()

###############################################################################

# Function to delete all selected coins

def delete_all():

    button_coin_2.deselect()
    button_coin_1.deselect()
    button_coin_50.deselect()
    button_coin_20.deselect()
    button_coin_10.deselect()
    button_coin_05.deselect()
    button_coin_02.deselect()
    button_coin_01.deselect()

# Function to calculate total number 2 euro coins

def coins_2():
    global rest
    global total_2

    total_2 = (rest - rest % 2) / 2
    total_2 = int(total_2)

    score_2.config(text=str(total_2) + ' x')

    rest = round(rest - (total_2 * 2), 2)

# Function to calculate total number 1 euro coins

def coins_1():
    global rest
    global total_1

    total_1 = (rest - rest % 1) / 1
    total_1= int(total_1)

    score_1.config(text=str(total_1) + ' x')

    rest = round(rest - (total_1 * 1), 2)

# Function to calculate total number 50 eurocent coins

def coins_50():
    global rest
    global total_50

    total_50 = (rest - rest % 0.5) / 0.5
    total_50 = int(total_50)

    score_50.config(text=str(total_50) + ' x')

    rest = round(rest - (total_50 * 0.5), 2)

# Function to calculate total number 20 eurocent coins 
# (everything x100 because modulus < 0.5 gives a deviation)

def coins_20():
    global rest
    global total_20

    total_20 = ((100 * rest) - (100 * rest) % 20) / 20
    total_20 = int(total_20)

    score_20.config(text=str(total_20) + ' x')

    rest = round(rest - (total_20 * 0.2), 2)

# Function to calculate total number 10 eurocent coins 
# (everything x100 because modulus < 0.5 gives a deviation)

def coins_10():
    global rest
    global total_10

    total_10 = ((100 * rest) - (100 * rest) % 10) / 10
    total_10 = int(total_10)

    score_10.config(text=str(total_10) + ' x')

    rest = round(rest - (total_10 * 0.1), 2)

# Function to calculate total number 5 eurocent coins 
# (everything x100 because modulus < 0.5 gives a deviation)

def coins_05():
    global rest
    global total_05

    total_05 = ((100 * rest) - (100 * rest) % 5) / 5
    total_05 = int(total_05)

    score_05.config(text=str(total_05) + ' x')

    rest = round(rest - (total_05 * 0.05), 2)

# Function to calculate total number 2 eurocent coins 
# (everything x100 because modulus < 0.5 gives a deviation)

def coins_02():
    global rest
    global total_02

    total_02 = ((100 * rest) - (100 * rest) % 2) / 2
    total_02 = int(total_02)

    score_02.config(text=str(total_02) + ' x')

    rest = round(rest - (total_02 * 0.02), 2)

# Function to calculate total number 1 eurocent coins 
# (everything x100 because modulus < 0.5 gives a deviation)

def coins_01():
    global rest
    global total_01

    total_01 = ((100 * rest) - (100 * rest) % 1) / 1
    total_01 = int(total_01)

    score_01.config(text=str(total_01) + ' x')

    rest = round(rest - (total_01 * 0.01), 2)

# Function for the calculation of all coin numbers, the total number of coins 
# and any remaining amount

def calculation():

    global rest
    rest = input_amount.get()

    try:                                            # Check if input is a number
        rest = float(rest.replace(",", "."))        # replace . by ,

        # Check restrictions money amount (200 euro)
        if rest > 200:                              
            validate_input.config(text='Betaal met pin')

        else:

            # Determine which coins are included in the calculation 
            if var_2.get() == 1: coins_2()
            if var_1.get() == 1: coins_1()
            if var_50.get() == 1: coins_50()
            if var_20.get() == 1: coins_20()
            if var_10.get() == 1: coins_10()
            if var_05.get() == 1: coins_05()
            if var_02.get() == 1: coins_02()
            if var_01.get() == 1: coins_01()

            # Remove deselected coins from the calculation when recalculating
            if var_2.get() == 0:
                global total_2
                total_2 = 0
                score_2.config(text=str(total_2) + ' x')
            if var_1.get() == 0:
                global total_1
                total_1 = 0
                score_1.config(text=str(total_1) + ' x')
            if var_50.get() == 0:
                global total_50
                total_50 = 0
                score_50.config(text=str(total_50) + ' x')
            if var_20.get() == 0:
                global total_20
                total_20 = 0
                score_20.config(text=str(total_20) + ' x')
            if var_10.get() == 0:
                global total_10
                total_10 = 0
                score_10.config(text=str(total_10) + ' x')
            if var_05.get() == 0:
                global total_05
                total_05 = 0
                score_05.config(text=str(total_05) + ' x')
            if var_02.get() == 0:
                global total_02
                total_02 = 0
                score_02.config(text=str(total_02) + ' x')
            if var_01.get() == 0:
                global total_01
                total_01 = 0
                score_01.config(text=str(total_01) + ' x')

            # Calculation total coins 
            total = total_2 + total_1 + total_50 + total_20 + total_10 \
                    + total_05 + total_02 + total_01
            total_coins.config(text='Totaal: ' + str(total))

            # Adjust labels and buttons
            remaining_amount.config(text='Rest \N{euro sign}' + 
                                    '{:.2f}'.format(rest).replace(".", ",")) 
            input_amount.config(state=DISABLED)
            button_calculate.config(text="Herbereken")
            validate_input.config(text='')

    except ValueError:
        validate_input.config(text='Ongeldige invoer')

# Function to enter a new amount (button = new amount)

def reset():

    # Reset all calculated numbers to 0

    rest = 0
    remaining_amount.config(text='')

    total = 0
    total_coins.config(text='')

    total_2 = 0
    score_2.config(text=str(total_2) + ' x')

    total_1 = 0
    score_1.config(text=str(total_1) + ' x')

    total_50 = 0
    score_50.config(text=str(total_50) + ' x')

    total_20 = 0
    score_20.config(text=str(total_20) + ' x')

    total_10 = 0
    score_10.config(text=str(total_10) + ' x')

    total_05 = 0
    score_05.config(text=str(total_05) + ' x')

    total_02 = 0
    score_02.config(text=str(total_05) + ' x')

    total_01 = 0
    score_01.config(text=str(total_05) + ' x')

    # Reselect all currencies just like opening the application
    button_coin_2.select()
    button_coin_1.select()
    button_coin_50.select()
    button_coin_20.select()
    button_coin_10.select()
    button_coin_05.select()
    button_coin_02.select()
    button_coin_01.select()

    # Adjust labels and buttons
    input_amount.config(state=NORMAL)
    input_amount.delete(0, END)
    button_calculate.config(text="Bereken")
    validate_input.config(text='')

###############################################################################

# Input field for entering amount

input_amount = Entry(root, width=5, font='Arial 16 bold', justify='center', 
                      fg='blue')
input_amount.place(x=10, y=150)

# Button for clearing coins selection

button_deselect = Button(root, text='wis selectie', font='Arial 10', bg='gold',  
                       fg='blue', command=delete_all)
button_deselect.place(x=400, y=620)

# Button to start calculation or recalculation

button_calculate = Button(root, text='Bereken', font='Arial 16 bold', bg='gold',  
                           fg='blue', bd='5', relief=RAISED, command=calculation)
button_calculate.place(x=120, y=140)

# New amount input button

button_new = Button(root, text='Nieuw Bedrag', font='Arial 12 bold', bg='gold',  
                      fg='blue', bd='4', relief=RAISED, command=reset)
button_new.place(x=400, y=665)

root.mainloop()

