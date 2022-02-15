import tkinter as Infinity
import datetime
import sys
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *

time = datetime.datetime.now()

# Define root of app
root = Infinity.Tk()

root.iconbitmap("infinityx.ico")

# Specify a variable for the askquestion() method as well as title
appTitleValue = 'InfinityX 1.59.63.2 Virtual Machine'
global appTitle;
appTitle = appTitleValue

root.title(appTitle)

#root.configure(bg = "white", fg = "black")

you = False
me = True

root.geometry("520x430") # Change to 730x520 when app is advanced

# Specify a frame to keep buttons
frame = Frame(root)

frame.pack()

root.resizable(False
             , False)
# Specify a variable with the import to use it instead if typing 'messagebox'
global impMessagebox;
impMessagebox = messagebox

getStartedFrame = Frame(root)

def about():
    impMessagebox.showinfo('About InfinityX*', 'InfinityX is a new version of Infinity. Last version o-\nf Infinity: 89.97.81.9 . So sorry how many version Inf-\ninity can hold. Newer versions hold more versions.')
    return

def getSecrets():
    if time.year < 2072:
        if sys.platform.startswith('win32'):
            impMessagebox.showinfo('Secret\'s', 'Secrets are shown in 2072')
        else:
            impMessagebox.showinfo('Secret\'s', 'Sorry, You don\'t have access to secrets. Win32 only has.', icon = "warning")
    else:
        noAccess = Label(root, text = 'We Did not give you access to secrets. Connect to \n InfinityX Server and add the \'InfinityX version 1.23.3-\n2.1\' ser-\nver and done!')
        noAccess.pack()


# This function is to close app
def endApp():
    confirmEnd = impMessagebox.askquestion (
        appTitle, 'This process will close the program. Are you sure to continue?')
    choice = confirmEnd.upper()
    if (choice == "YES"):
        root.destroy()
    elif (choice == "NO"):
        pass

def valProgress():
    global newWindow;
    newWindow = Toplevel(root)
 
    newWindow.title(appTitle + "- Validate Progress")

    newWindow.iconbitmap("infinityx.ico")
    newWindow.resizable(False, False)
    newWindow.geometry("520x430")
 
    Infinity.Label(newWindow,
          text = "Validate Progress.", fg = "red").pack()
    global progress;
    progress = Progressbar(newWindow, orient = HORIZONTAL,
              length = 100, mode = 'determinate')
    startI = Button(newWindow, text = 'Start', command = bar).pack(pady = 10)
    progress.pack(pady = 10)


def bar():
    import time

    #done.pack_forget()
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    progVal = progress['value']
    if progVal == 100:
        global done;
        done = Infinity.Label(newWindow, text = "Done!", fg = "green")
        done.pack()
        secr.pack_forget()
        newWindow.destroy()

def helpC():
    xHelp = messagebox.askquestion('InfinityX Help', 'Sorry, InfinityX Help has no members joined. DO you want to join?', icon = "warning")
    if xHelp.upper() == "YES":
        impMessagebox.showinfo('InfinityX Help', 'You joined! But you need something else to join the server.', icon = "error")
    else:
        pass

def getStartedFunc():
    frame.destroy()
    welcome.destroy()
    getStartedFrame.pack()
    return

def editor():
    return

optionsGetStartedDisabled  = 0
# Creating Menubar
menubar = Menu(root)

asWeKnow = "Line 56 is not working proper"
# Adding Options Menu and commands
options = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Options', menu = options)
#options.entryconfig(1, state=DISABLED)
options.add_command(label ='Get Started', command = getStartedFunc)
options.add_separator()
options.add_command(label ='Open...', command = None)
options.add_command(label ='Save', command = None)
options.add_command(label ='Editor', command = editor)
options.add_command(label ='Secrets..', command = getSecrets)
secr = options.add_command(label ='Validate Secrets..', command = valProgress)
options.add_separator()
options.add_command(label ='Exit', command = endApp)
  
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='InfinityX Help', command = helpC)
help_.add_separator()
help_.add_command(label ='About InfinityX', 
                  command = about)
  
root.config(menu = menubar)

# Help variables get no value
def noVarName():
    # Define variaables no name
    pass

# Welcome! 
def welcomeFunc(root):
    welcome = Label(root, text="Welcome to InfinityX Virtual Machine! OK no time to talk about this let\'s get started.")
    return welcome

welcome = welcomeFunc(root)
welcome.pack()

getStarted = Infinity.Button(frame, text ='Get started to InfinityX', bg = "orange", fg = "white", command = getStartedFunc, borderwidth=1  )
getStarted.pack()

endProgram = Button(root, text = 'Close Virtual Machine',
                command = endApp)


packDestroyButtonNow = endProgram.pack(side = 'bottom')
packDestroyButtonNow

# Get started content
welcomeGS = Label(getStartedFrame, text = "Welcome!")  
welcomeGS.pack()

pswFrame = Infinity.Frame(root)
def nextStep():
    flname["state"] = "disabled"
    pswFrame.pack()
    global pswInput;
    pswInput = Infinity.Entry(pswFrame, borderwidth=1)
    pswInput.pack()
    pswInput.insert(0, "ABCDFGHIJKLMNOP")
    Infinity.Button(pswFrame, text = "Next ->", bg = "#40F10D", borderwidth=1, command = done).pack()

flnLab = Label(getStartedFrame, text = "Full Name:")
flnLab.pack()
flname = Infinity.Entry(getStartedFrame)
flname.insert(0, "Full Name")
flname.pack()
Infinity.Button(getStartedFrame, text = "Next ->", bg = "#40F10D", borderwidth=1, command = nextStep).pack()
Infinity.Label(getStartedFrame, text = "Warning: DO NOT PRESS F7 unless you completed entering the forms and complete password.", fg = "red").pack()

def callback(event):
    flnameVal = flname.get()
    impMessagebox.showinfo(appTitle, 'Welcome ' + flnameVal + '!')
    return

def done():
    pswInput["state"] = "disabled"
    Infinity.Label(pswFrame, text = "To really confirm, Press F7 to Setup.", fg = "green").pack()
    root.bind('<F7>', callback)

# Copyright 2022 by Samuel Santhosh

# Run the app
runAppNow = root.mainloop()
runAppNow
