'''
Created on Apr 4, 2016

@author: AS017303
'''
from Tkinter import *

class Application():
    def __init__(self):
        self.mainframe = Tk()
        
        #screenWidth,screenHeight=self.mainframe.winfo_screenwidth(),self.mainframe.winfo_screenheight()
        screenWidth = 1350
        screenHeight = 680
            
        self.mainframe.geometry("%dx%d+0+0" % (screenWidth, screenHeight))

    def start(self):
        self.mainframe.mainloop()