'''
Created on Mar 6, 2015

@author: Henry Hinton, Pavle Jeremic, Eduardo Hirata
'''
#!/usr/bin/python
import Tkinter
from Tkinter import Tk, Frame, BOTH



class GUI(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        self.parent.title("Lothian")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self):
      
        w = 800
        h = 600

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():
  
    root = Tk()
    ex = GUI(root)
    root.mainloop()  


if __name__ == '__main__':
    top=root();
    graph= GUI(Frame, )

    print("Hey there, sweet cheeks.")

