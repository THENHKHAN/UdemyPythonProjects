
import time ,random
import pyautogui ,tkinter as tk  # import tkinter library


def screenShot():
    time.sleep(3) # this will wait 5sec (delay time)
    imgName = int(round(time.time()*100))#another way to generate random number
    nameOfImg = f"{imgName}_pic.png"
    img = pyautogui.screenshot() # this will take the current opening whole screen ScreenShot.
    img.save(f"./SS_Collections/tkInker{nameOfImg}")  # path wher you wanna save the SS.



def creatingWindow ():
    # create main window (container)
    window = tk.Tk()
    window.title('Made By - NHKHAN')
    frame = tk.Frame(window) # It can be defined as a container to which, another widget can be added and organized.
    window.geometry("400x200")
    #set window color
    window.configure(bg='grey')
    frame.pack()#It organizes the widgets in blocks before placing in the parent widget.
    
    btn1 = tk.Button(frame,text = "Take Screenshot",command=screenShot)# calling above function
    btn1.pack(side=tk.LEFT)
    closeBtn = tk.Button(frame,text = "Quit",command=quit)
    closeBtn.pack(side=tk.LEFT)
    window.mainloop()

creatingWindow ()









#--> how to take screenshot from a Tkinter application
#  Note that the name of the module in Python 2.x is ‘Tkinter’ and in Python 3.x it is ‘tkinter’.
'''
There are two main methods used which the user needs to remember while creating the Python application with GUI.

1-> Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1): To create a main window, tkinter offers a method ‘Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)’. To change the name of the window, you can change the className to the desired one. The basic code used to create the main window of the application is:
m=tkinter.Tk() where m is the name of the main window object

2-> mainloop(): There is a method known by the name mainloop() is used when your application is ready to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.
'''