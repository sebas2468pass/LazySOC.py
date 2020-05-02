"""
    Title:             LazySOC.py
    Description:       The purpose of this tool is automating everyday mundane tasks of a SOC analyst. 
    Author:           sebas
    Version:           0.0.1
    Creation date:     May 02 2020
               
    Changes :
        Version 0.0.1 : Created the GUI

    Features to add : 
        
    How to install : 
        - Install Python 3
        - open cmd or terminal, run this command : pip install python-certifi-win32, greynoise, Django==3.0.5, OTXv2
        - Download LazySOC.py to your computer and run it.
"""

import tkinter as tk
import tkinter.scrolledtext as tkst

class mainGUI:
    
    def __init__(self, GUI):
        
        versionNumber = "0.0.1"
        startGUI.title("LazySOC Tool " + versionNumber)
        startGUI.resizable(False, False)
        mainWindow = tk.Canvas(GUI, width = 1000, height = 775, relief = 'raised')
        mainWindow.pack()

        leftFrame = tk.Frame(GUI, width = 370, height = 725, relief = 'raised', borderwidth = 3)
        leftFrame.place(x=10, y=40, anchor="nw")
        
        ipurlseparatorFrame =tk.Frame(GUI, width = 335, height = 3, relief = 'sunken', borderwidth = 2)
        ipurlseparatorFrame.place(x=25, y=132, anchor="nw")
        
        titleFrame = tk.Label(GUI, text='LazySOC Tool ' + versionNumber)
        titleFrame.config(font=('helvetica', 14))
        mainWindow.create_window(200, 25, window=titleFrame)
        
        urlLabel = tk.Label(GUI, text="Enter URL:")
        urlLabel.config(font=('helvetica', 10))
        mainWindow.create_window(200, 60, window=urlLabel)
        
        urlInputbox = tk.Entry(GUI, width = 40)
        mainWindow.create_window(200, 80, window=urlInputbox)
        
        outputBox = tkst.ScrolledText(GUI)
        outputBox.config(state='disabled')
        mainWindow.create_window(685, 402, width=600, height=725, window=outputBox)
        
        ipLabel = tk.Label(GUI, text="Enter IP Address :")
        ipLabel.config(font=('helvetica', 10))
        mainWindow.create_window(200, 150, window=ipLabel)
        
        ipInputbox = tk.Entry (GUI, width = 40)
        mainWindow.create_window(200, 170, window=ipInputbox)
        
        emailLabel = tk.Label(GUI, text="Enter email Headers :")
        emailLabel.config(font=('helvetica', 10))
        mainWindow.create_window(195, 270, window=emailLabel)
        
        emailInputbox = tk.Entry (GUI, width = 40)
        mainWindow.create_window(200, 290, window=emailInputbox)
        
        urlemailseparatorFrame =tk.Frame(GUI, width = 335, height = 3, relief = 'sunken', borderwidth = 2)
        urlemailseparatorFrame.place(x=25, y=255, anchor="nw")
        
        
startGUI = tk.Tk()
mainGUI(startGUI)
startGUI.mainloop()

        
      
        
"""

"""