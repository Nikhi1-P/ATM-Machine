from tkinter import *
from tkinter import messagebox

password = '1430'
new_window = ''
balance = 250000

def shortcut(event):
    if event.state == 12 and event.keysym == "Return":
        pass_check()





def pass_check():
    global password
    if my_password.get() == password:
        my_password.set('')
        label2.config(text='')
        new_window = Toplevel(root)
        new_window.title("New Window")
        new_window.geometry('350x500')
        new_window.resizable(0,0)
        new_window.config(background='black')

        option_label = Label(new_window, text = "Choose Any of the Option:", font = ('Times New Roman', 20), bg='black', fg='white')
        option_label.pack(pady = 10)

        with_btn = Button(new_window, text='Withdraw', font=('Times New Roman', 16), relief='raised', borderwidth=5, width = 20, command=withdraw_page)
        with_btn.pack(pady = 10)

        dep_btn = Button(new_window, text='Deposit', font=('Times New Roman', 16), relief='raised', borderwidth=5, width = 20, command=deposit_page)
        dep_btn.pack(pady = 10)

        bal_btn = Button(new_window, text='Balance Check', font=('Times New Roman', 16), relief='raised', borderwidth=5, width = 20, command=balance_check_page)
        bal_btn.pack(pady = 10)

        pin_btn = Button(new_window, text='Pin Change', font=('Times New Roman', 16), relief='raised', borderwidth=5, width = 20, command=pass_change_page)
        pin_btn.pack(pady = 10)

        exit_btn = Button(new_window, text='Exit', font=('Times New Roman', 16), relief='raised', borderwidth=5, width = 20, command=lambda : new_window.destroy())
        exit_btn.pack(pady = 10)

    else:
        label2.config(text='Incorrect Password')
    entry1.delete(0, END)





def withdraw_page():

    withdraw_window = Toplevel(root)
    withdraw_window.title("Withdraw Portal")
    withdraw_window.geometry('350x450')
    withdraw_window.config(background='black')

    button_frame = Frame(withdraw_window, background='black')
    button_frame.pack(fill='x',expand=True)

    def withdraw(amount):
        global balance
        balance -= amount
        messagebox.showinfo('Success', f'Withdraw was Succesful and balance left is: {balance}')
        withdraw_window.destroy()


    one_hundred_btn = Button(button_frame, text='100', command=lambda : withdraw(100), relief='raised', borderwidth=3, width=20, height=5)
    one_hundred_btn.grid(row=0, column=0, padx=5, pady=15)

    two_hundred_btn = Button(button_frame, text='200', command=lambda: withdraw(200), relief='raised', borderwidth=3,
                         width=20, height=5)
    two_hundred_btn.grid(row=0, column=1, padx=32, pady=5,)

    five_hundred_btn = Button(button_frame, text='500', command=lambda: withdraw(500), relief='raised', borderwidth=3,
                             width=20, height=5)
    five_hundred_btn.grid(row=1, column=0, padx=5, pady=15)

    two_thousand_btn = Button(button_frame, text='2000', command=lambda: withdraw(2000), relief='raised', borderwidth=3,
                             width=20, height=5)
    two_thousand_btn.grid(row=1, column=1, padx=32, pady=5)

    other_amt_lbl =Label(withdraw_window, text="Enter other amount: ", font=('Times New Roman',16))
    other_amt_lbl.pack(pady=(0,5))

    cash = IntVar()
    other_amount = Entry(withdraw_window, font=('Times New Roman', 20), textvariable=cash)
    other_amount.pack(ipady=7, pady=(15,35))

    def other_amount_fun(_):
        global balance
        balance -= cash.get()
        cash.set(0)
        messagebox.showinfo('Success', f'Withdraw was Succesful and balance left is: {balance}')
        withdraw_window.destroy()


    other_amount.bind('<Return>', other_amount_fun)





def deposit_page():
    deposit_window = Toplevel(root)
    deposit_window.title('Deposit Portal')
    deposit_window.geometry('350x350')
    deposit_window.config(bg='black')
    deposit_window_lbl = Label(deposit_window, text='Enter the Amount: ', font=('Times New Roman',20), background='black',foreground='white')
    deposit_window_lbl.pack(pady = 15)


    deposit_amount = StringVar()
    deposit_window_entry = Entry(deposit_window, font=('Times New Roman',16), textvariable=deposit_amount)
    deposit_window_entry.pack(ipady = 7)
    deposit_window_entry.focus_set()


    def deposit_add():
        global balance
        balance += int(deposit_amount.get())
        deposit_amount.set('')
        messagebox.showinfo('Success', f'Deposit was Succesful and balance left is: {balance}')
        deposit_window.destroy()

    deposit_amount_btn = Button(deposit_window, text='Enter', font=('Times New Roman',16),command = deposit_add)
    deposit_amount_btn.pack(pady = 15)



def balance_check_page():
    messagebox.showinfo('Success', f'The Available Balance is {balance}')






def pass_change_page():
    global password


    def new_pass():
        global password

        def btn_enter():
            global password
            password = my_new_pass
            new_pass_window.destroy()

        if my_pass.get() == int(password):
            new_pass_window = Toplevel(root)
            new_pass_window.title('New_window')
            new_pass_window.geometry('350x350')
            new_pass_window.config(background='black')
            new_pass_window_lbl = Label(new_pass_window, text='Enter the New Password Here', font=('Times New Roman',16))
            new_pass_window_lbl.pack(pady=10)
            my_new_pass = StringVar()
            new_pass_window_entry = Entry(new_pass_window, font=('Times New Roman', 16), textvariable=my_new_pass)
            new_pass_window_entry.pack(ipady=7)
            
            new_pass_window_btn = Button(new_pass_window, text='Enter', font=('Times New Roman',16), relief='raised', command=btn_enter)
            new_pass_window_btn.pack(pady=10)
        else:
            messagebox.showerror('Error','Wrong Password, please try again')

    pass_change_window = Toplevel(root)
    pass_change_window.title('Password Change Request')
    pass_change_window.geometry('350x350')
    pass_change_window.config(background='black')
    pass_change_window_lbl = Label(pass_change_window, text='Please Enter your Password', font=('Times New Roman',16))
    pass_change_window_lbl.pack(pady = 10)
    my_pass = IntVar()
    pass_change_window_entry = Entry(pass_change_window, font=('Times New Roman', 16), textvariable=my_pass)
    pass_change_window_entry.pack(ipady = 7)
    pass_change_page_btn = Button(pass_change_window, text='Enter', font=('Times New Roman', 16), relief='raised', borderwidth=5, command = new_pass)
    pass_change_page_btn.pack(pady = 10)










root = Tk()

root.title("ATM Machine")

root.geometry("350x500")

root.config(background='black')

label1 = Label(root, text='Welcome to Bank of Florida', font=('Times New Roman', 20), background='black', foreground='white')
label1.pack(pady = 50)


pass1 = Label(root, text="Enter the password", width=15, height = 1, font = ('Times New Roman',20), background='black', foreground='white')
pass1.pack(pady = 10)

my_password = StringVar()
entry1 = Entry(root, width=30, textvariable=my_password)
entry1.focus_set()
entry1.pack(ipady = 5)

def handle_focus_in(_):
    entry1.configure(fg='black', show = '*')

entry1.bind('<FocusIn>', handle_focus_in)

root.bind('<KeyPress>', shortcut)

btn1 = Button(text='Enter', width=5, font=('Times New Roman', 16), command=pass_check, relief='raised', borderwidth=5)
btn1.pack(pady = 30)

label2 = Label(root, text="", width=15, height = 1, font = ('Times New Roman',20), background='black', foreground='white')
label2.pack()

root.mainloop()