from tkinter import *
from tkinter import messagebox, Toplevel
import pyqrcode
import png
import os


qr_app = Tk()
qr_app.geometry('570x400')
qr_app.title("My Qr Code Generator App")
qr_app.configure(bg='blue')
qr_app.iconbitmap('Qrcode.ico')


# Functions
def Quit_root():
    res = messagebox.askokcancel(
        'Notification', "Are you sure you want to quit?")
    if res == True:
        qr_app.destroy()
    else:
        pass


def clear_id_name():
    Qr_Id_entrybox.delete(0, 'end')
    Qr_message_entrybox.delete(0, 'end')
    Qr_name_entrybox.delete(0, 'end')
    Qr_Notification_message_Label.configure(text='')


def Generate_Qr():
    qr_name = Qr_name_entrybox.get()
    qr_id = Qr_Id_entrybox.get()
    qr_message = Qr_message_entrybox.get()
    message_qr = 'Name: ' + qr_name + '\nId: ' + qr_id + '\nMessage: ' + qr_message
    # print(message_qr)
    url = pyqrcode.create(message_qr)
    PP = r'C:\Users\HP\OneDrive\Desktop\QR1'
    cc = '{}\{}{}.png'.format(PP, qr_id, qr_name)
    ll = os.listdir(PP)
    if "{}{}.png".format(qr_id, qr_name) in ll:
        messagebox.showinfo("Notification", "PLease choose another id or name")
    else:
        url.png(cc, scale=6)
        mm = "Qr Code save as: "+qr_id+qr_name+'.png'
        Qr_Notification_message_Label.configure(text=mm)
        res = messagebox.askyesno(
            "Notification", "Qr code is generated and if you want to see it then Yes: ")
        if(res == True):
            top = Toplevel()
            top.geometry('400x400')
            top.configure(bg="white")
            ing = PhotoImage(file=cc)
            label1 = Label(top, image=ing, bg='white')
            label1.place(x=10, y=10)


# labels
Qr_Id_Label = Label(master=qr_app, text="Enter your ID: ",
                    bg='powder blue', fg='red', width=20, height=2, font=('times', 12, 'italic bold'))
Qr_Id_Label.place(x=10, y=20)

Qr_name_Label = Label(master=qr_app, text="Enter your name: ",
                      bg='powder blue', fg='red', width=20, height=2, font=('times', 12, 'italic bold'))
Qr_name_Label.place(x=10, y=80)

Qr_message_Label = Label(master=qr_app, text="Enter your message: ",
                         bg='powder blue', fg='red', width=20, height=2, font=('times', 12, 'italic bold'))
Qr_message_Label.place(x=10, y=140)

Qr_Notification_Label = Label(master=qr_app, text="Notification: ",
                              bg='powder blue', fg='red', width=10, height=2, font=('times', 15, 'bold underline'))
Qr_Notification_Label.place(x=10, y=350)

Qr_Notification_message_Label = Label(master=qr_app, text="",
                                      bg='powder blue', fg='red', width=30, height=2, font=('times', 15, 'bold underline'))
Qr_Notification_message_Label.place(x=200, y=350)

# Entry boxes
Qr_Id_entrybox = Entry(master=qr_app, width=25, bd=5,
                       bg="pink", font=('times', 17, 'italic bold'))
Qr_Id_entrybox.place(x=250, y=20)

Qr_name_entrybox = Entry(master=qr_app, width=25, bd=5,
                         bg="pink", font=('times', 17, 'italic bold'))
Qr_name_entrybox.place(x=250, y=80)

Qr_message_entrybox = Entry(master=qr_app, width=25, bd=5,
                            bg="pink", font=('times', 17, 'italic bold'))
Qr_message_entrybox.place(x=250, y=140)

# Button logos
Generate_Qrimage = PhotoImage(file='qr-code.png')
Generate_Qrimage = Generate_Qrimage.subsample(20, 20)

clear_Qrimage = PhotoImage(file='eraser.png')
clear_Qrimage = clear_Qrimage.subsample(20, 20)

quit_Qrimage = PhotoImage(file='x-button.png')
quit_Qrimage = quit_Qrimage.subsample(20, 20)


# Buttons
Generate_Qrimage_button = Button(master=qr_app, text="Generate", width=100, font=(
    'times', 10, 'bold'), bd=10, activebackground='blue', command=Generate_Qr, bg='powder blue', image=Generate_Qrimage, compound=RIGHT)
Generate_Qrimage_button.place(x=10, y=250)

clear_id_name_button = Button(master=qr_app, text="Clear", width=100, font=(
    'times', 10, 'bold'), bd=10, activebackground='blue', bg='powder blue', image=clear_Qrimage, compound=RIGHT, command=clear_id_name)
clear_id_name_button.place(x=210, y=250)

quit_Qrimage_button = Button(master=qr_app, text="Quit", width=100, font=(
    'times', 10, 'bold'), bd=10, activebackground='blue', bg='powder blue', image=quit_Qrimage, compound=RIGHT, command=Quit_root)
quit_Qrimage_button.place(x=410, y=250)


# Hover effects
def Generate_Qrimage_buttonEnter(e):
    Generate_Qrimage_button['bg'] = 'purple2'


def Generate_Qrimage_buttonLeave(e):
    Generate_Qrimage_button['bg'] = 'powder blue'


def clear_id_name_buttonEnter(e):
    clear_id_name_button['bg'] = 'purple2'


def clear_id_name_buttonLeave(e):
    clear_id_name_button['bg'] = 'powder blue'


def quit_Qrimage_buttonEnter(e):
    quit_Qrimage_button['bg'] = 'purple2'


def quit_Qrimage_buttonLeave(e):
    quit_Qrimage_button['bg'] = 'powder blue'


Generate_Qrimage_button.bind('<Enter>', Generate_Qrimage_buttonEnter)
Generate_Qrimage_button.bind('<Leave>', Generate_Qrimage_buttonLeave)

clear_id_name_button.bind('<Enter>', clear_id_name_buttonEnter)
clear_id_name_button.bind('<Leave>', clear_id_name_buttonLeave)

quit_Qrimage_button.bind('<Enter>', quit_Qrimage_buttonEnter)
quit_Qrimage_button.bind('<Leave>', quit_Qrimage_buttonLeave)


qr_app.mainloop()
