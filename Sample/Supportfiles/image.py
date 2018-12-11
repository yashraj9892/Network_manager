from tkinter import *
import time

class fade:
    def __init__(self,root):
        self.root =root;
        self.frame =Frame(root)
        self.frame.pack()
        self.fade_away()
        
    def fade_away(self):
        alpha = self.root.attributes("-alpha")
        if alpha > 0:
            alpha -= .04
            self.root.attributes("-alpha", alpha)
            self.frame.after(100, self.fade_away)
        else:
            self.root.destroy()

def intro():
    root = Tk()
    root.overrideredirect(1)
    width = root.winfo_screenwidth()
    height= root.winfo_screenheight()
    canvas = Canvas(root,width =width,height=height,background="BLACK")
    canvas.pack()
    intro = PhotoImage(file = "Supportfiles/images/speedometer3.png")
    canvas.create_image(width/2,height/2,anchor =CENTER,image=intro)                    
    fade(root)
    root.mainloop()



