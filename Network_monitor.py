import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import threading
from Supportfiles import image as img
from Supportfiles import Data_used as DU
from Supportfiles import Login as l
from Supportfiles import internet_speed as Is
import sys
import signal,os

default_text={'Rollno or ID' : 'Rollno or ID', '*********' : '*********','http://172.31.1.6:8090' : 'http://172.31.1.6:8090'}
memory ={0:"KB",1:'MB',2:'GB',3:'TB'}
speed  ={0:"KBps",1:'MBps',2:'GBps',3:'TBps'}


## important to stop thread
## https://www.g-loaded.eu/2016/11/24/how-to-terminate-running-python-threads-using-signals/


class MainGUI:

    def __init__(self,master):
        self.root = master
        self.frame = Frame(master)##for speed of internet
        self.frame.pack(fill=(BOTH))
        self.initializer()
        self.set_frame()
        
    def initializer(self):
        self.image = PhotoImage(file='Supportfiles/images/speedometer3.png')
        self.root.tk.call('wm', 'iconphoto', root._w, self.image)
        self.previous=''
        ## variable declaration
        try:
                with open("Supportfiles/support","rb") as f:
                       self.previous =f.readline().decode('utf-8')
        except:
                pass
        print(self.previous)
        self.current_speed_up = IntVar()
        self.current_speed_down = IntVar()
        self.current_data_sent = IntVar()
        self.current_data_received = IntVar()
        self.current_data_total = IntVar()
        self.speed_m_up = 0
        self.speed_m_down = 0
        self.consump_up=0
        self.consump_down=0
        self.consump_total=0
        self.button_work = StringVar()
        self.consumption_up = StringVar()
        self.consumption_down = StringVar()
        self.consumption_total = StringVar()
        self.speed_meter_up = StringVar()
        self.speed_meter_down = StringVar()
        ## variable inti
        self.speed_meter_up.set("KBps")
        self.speed_meter_down.set("KBps")
        self.a=[0,0,0,0,0,0]
        try:
                 with open("Supportfiles/data","r") as f:
                    k=0
                    for i in f:
                        i="".join(str(x) for x in i)
                        i.strip('\n')
                        self.a[k]=int(i.split('-')[0])
                        k+=1
                        self.a[k]=(int(i.split('-')[1]))
                        k+=1
                        print(self.a)
                    try:
                        
                        self.current_data_received.set(self.a[0])
                        self.consump_down=self.a[1]
                        self.consumption_down.set(memory[self.a[1]])
                        self.current_data_sent.set(self.a[2])
                        self.consump_up=self.a[3]
                        self.consumption_up.set(memory[self.a[3]])
                        self.current_data_total.set(self.a[4])
                        self.consump_total=self.a[5]
                        self.consumption_total.set(memory[self.a[5]])
                    except: 
                        self.consumption_down.set("KB")
                        self.consumption_total.set("KB")
                        self.consumption_up.set("KB")
                        self.current_data_sent.set(0)
                        self.current_data_received.set(0)
                        self.current_data_total.set(0)
               
        except: 
                self.consumption_down.set("KB")
                self.consumption_total.set("KB")
                self.consumption_up.set("KB")
                self.current_data_sent.set(0)
                self.current_data_received.set(0)
                self.current_data_total.set(0)
        self.button_work.set("Login")
        self.current_speed_up.set(0)
        self.current_speed_down.set(0)
        ## floating window
   
        
    def set_frame(self):

        ##speedometer
        self.label_speed =ttk.Label(self.frame,text="Internet speed",font="Helvetica 18 bold")
        self.current_speed_label_up = ttk.Label(self.frame,textvariable=self.current_speed_up,font="Helvetica 14 ")
        self.current_speed_label_down = ttk.Label(self.frame,textvariable=self.current_speed_down,font="Helvetica 14 ")
        self.uplabel = ttk.Label(self.frame,text="up : ",font="Helvetica 14 bold")
        self.downlabel = ttk.Label(self.frame,text="down : ",font="Helvetica 14 bold")
        self.current_speed_text_label1 = ttk.Label(self.frame, textvariable=self.speed_meter_up, font="Helvetica 14 ")
        self.current_speed_text_label2 = ttk.Label(self.frame, textvariable=self.speed_meter_down, font="Helvetica 14 ")
        ## speed
        self.label_speed.grid(column=0,columnspan=6,row=0,rowspan=2,sticky=(W))
        ## up/sent
        self.uplabel.grid(column=0,row=2,sticky=(W))
        self.current_speed_label_up.grid(column=1,row=2, sticky=(W))
        self.current_speed_text_label1.grid(column=2,row=2,sticky=(W))
        ## down/received
        self.downlabel.grid(column=3,row=2,sticky=(W))
        self.current_speed_label_down.grid(column=4,row=2, sticky=(W))
        self.current_speed_text_label2.grid(column=5,row=2,sticky=(W))
        self.empty_label_1= ttk.Label(self.frame,text="     ",font="Helvetica 14 bold")
        self.empty_label_1.grid(row=3)
        ## data consumption
        self.label_data =ttk.Label(self.frame,text="Data Consumption",font="Helvetica 18 bold")
        self.current_sent_data = ttk.Label(self.frame,textvariable=self.current_data_sent,font="Helvetica 14 ")
        self.current_received_data = ttk.Label(self.frame,textvariable=self.current_data_received,font="Helvetica 14")
        self.total = ttk.Label(self.frame,textvariable=self.current_data_total,font="Helvetica 14 ")
        self.uplabel = ttk.Label(self.frame,text="up : ",font="Helvetica 14 bold")
        self.downlabel = ttk.Label(self.frame,text="down : ",font="Helvetica 14 bold")
        self.tlabel = ttk.Label(self.frame,text="Total : ",font="Helvetica 14 bold")
        self.current_text_label1 = ttk.Label(self.frame,textvariable=self.consumption_up, font="Helvetica 14 ")
        self.current_text_label2 = ttk.Label(self.frame,textvariable=self.consumption_down, font="Helvetica 14 ")
        self.current_text_label3 = ttk.Label(self.frame,textvariable=self.consumption_total, font="Helvetica 14 ")
        ## data
        self.label_data.grid(column=0,row=4,columnspan=6,rowspan=2,sticky=(W))
        ## up/sent
        self.uplabel.grid(column=0,row=6,sticky=(W))
        self.current_sent_data.grid(column=1,row=6,sticky=(W))
        self.current_text_label1.grid(column=2,row=6,sticky=(W))
        ##received/down
        self.downlabel.grid(column=3,row=6,sticky=(W))
        self.current_received_data.grid(column=4,row=6,sticky=(W))
        self.current_text_label2.grid(column=5,row=6,sticky=(W))
        ##total
        self.tlabel.grid(row=7,column=0,sticky=(W))
        self.total.grid(row=7,column=1,sticky=(W))
        self.current_text_label3.grid(row=7,column=2,sticky=(W))
        self.empty_label_1= ttk.Label(self.frame,text="     ",font="Helvetica 14 bold")
        self.empty_label_1.grid(row=8)
        self.reset_button =Button(self.frame, text= "Reset",width=6)
        self.reset_button.bind('<Button-1>',self.reset)
        self.reset_button.grid(row=7,column=3,sticky=W)
        ## login
        self.label_1 = Label(self.frame,text="Name",font="Helvetica 14 bold")
        self.label_2 = Label(self.frame,text="Password",font="Helvetica 14 bold")
        self.entry_1 = Entry(self.frame)
        self.entry_1.insert(0,"Rollno or ID")
        self.entry_1.config(fg="grey")
        self.entry_1.bind('<FocusIn>',  self.on_entry_click)
        self.entry_1.bind('<FocusOut>',  lambda event, a = "Rollno or ID" : self.on_focusout(event, a))
        self.entry_2 = Entry(self.frame,show='*')
        self.entry_2.insert(0,"*********")
        self.entry_2.config(fg="grey")
        self.entry_2.bind('<FocusIn>',  self.on_entry_click )
        self.entry_2.bind('<FocusOut>',  lambda event, a = "*********" : self.on_focusout(event, a))
        self.label_1.grid(row=9, sticky=W)
        self.label_2.grid(row=10, sticky=W)
        self.entry_1.grid(row=9,columnspan=2,column=1)
        self.entry_2.grid(row=10,columnspan=2,column=1)
        self.site_1 = Label(self.frame,text="Enter the site ",font="Helvetica 14 bold")
        self.entry_3 = Entry(self.frame)
        self.entry_3.insert(0,"http://172.31.1.6:8090")
        self.entry_3.config(fg="grey")
        self.entry_3.bind('<FocusIn>',  self.on_entry_click)
        self.entry_3.bind('<FocusOut>',  lambda event, a = "http://172.31.1.6:8090" : self.on_focusout(event, a))
        self.site_1.grid(row=11,sticky=W)
        self.entry_3.grid(row=11,columnspan=2,column=1)
        self.p=BooleanVar()
        self.p.set(False)
        self.check =Checkbutton(self.frame, text = "remember this site",font="Helvetica 12 ",variable = self.p).grid(row=11,columnspan=2,column=4)
        self.button =Button(self.frame, textvariable =self.button_work)
        self.button.bind('<Button-1>',self.login)
        self.button.grid(row=12,sticky=W)
        self.forcebutton =Button(self.frame, text="Force Logout")
        self.forcebutton.bind('<Button-1>',self.force_logout)
        self.forcebutton.grid(row=12,column=1,sticky=W)
        self.root.grid_columnconfigure(0,weight=1)
        print(self.previous)
        if self.previous is not '':
                self.entry_3.delete(0,"end")
                self.entry_3.insert(0,self.previous)
                self.entry_3.config(fg='black')
                self.p.set(True)
        print(self.previous)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) ## for close button ## to close all threads sys.exit()
        self.data_value = threading.Thread(target=self.get_data_value, args=())
        self.speed_value = threading.Thread(target=self.get_current_speed, args=())
        self.data_value.start()
        self.speed_value.start()

        

        
    def reset(self,event):   
        f = open("Supportfiles/data","wb")
        f.close()
        self.a=[0,0,0,0,0,0]
        self.current_data_received.set(self.a[0])
        self.consump_down=self.a[1]
        self.consumption_down.set(memory[self.a[1]])
        self.current_data_sent.set(self.a[2])
        self.consump_up=self.a[3]
        self.consumption_up.set(memory[self.a[3]])
        self.current_data_total.set(self.a[4])
        self.consump_total=self.a[5]
        self.consumption_total.set(memory[self.a[5]])

    def get_data_value(self):
        alpha,beta,gamma= DU.main()
        time.sleep(1)
        while True:
                x,y,z = DU.main()
                self.current_data_sent.set(round(x-alpha+self.a[2],2))
                self.current_data_received.set(round(y-beta+self.a[0],2))
                self.current_data_total.set(round(z-gamma+self.a[4],2))
                c,d,e = self.consump_up,self.consump_down,self.consump_total
                while(d!=0):
                        self.current_data_received.set(round(self.current_data_received.get()/1024.,2))
                        d=d-1
                while(c!=0):
                        self.current_data_sent.set(round(self.current_data_sent.get()/1024.,2))
                        c=c-1
                while(e!=0):
                        self.current_data_total.set(round(self.current_data_total.get()/1024.,2))
                        e=e-1;

                if(self.current_data_received.get()>1024):
                        self.current_data_received.set(round(self.current_data_received.get()/1024.,2))
                        self.consumption_down.set(memory[self.consump_down+1])
                        self.consump_down=self.consump_down+1             
                if(self.current_data_sent.get()>1024 ):
                        self.current_data_sent.set(round(self.current_data_sent.get()/1024.,2))
                        self.consumption_up.set( memory[self.consump_up+1])
                        self.consump_up=self.consump_up+1
                if(self.current_data_total.get()>1024):
                        self.current_data_total.set(round(self.current_data_total.get()/1024.,2))
                        self.consumption_total.set( memory[self.consump_total+1])
                        self.consump_total=self.consump_total+1
                time.sleep(1.5)
        
    def get_current_speed(self):
        while True:
                value =Is.speed()
##                print(not self.shutdown_flag2.is_set())
                speed_upload = value[0]
                speed_download = value[1]
                self.current_speed_up.set(speed_upload)
                self.current_speed_down.set(speed_download)
                d,c = self.speed_m_down,self.speed_m_up
                while(d!=0):
                        self.current_speed_down.set(round(self.current_speed_down.get()/1024.,2))
                        d=d-1
                while(c!=0):
                        self.current_speed_up.set(round(self.current_speed_up.get()/1024.,2))
                        c=c-1
                if(self.current_speed_up.get()>1024):
                        self.current_speed_up.set(round(self.current_speed_up.get()/1024.,2))
                        self.speed_meter_up.set( speed[self.speed_m_up+1])
                        self.speed_m_up=self.speed_m_up+1
                        
                elif(self.current_speed_up.get()<10 and self.speed_m_up>0):
                        self.current_speed_up.set(round(self.current_speed_up.get()*1024.,2))
                        self.speed_meter_up.set( speed[self.speed_m_up-1])
                        self.speed_m_up=self.speed_m_up-1                        
                if(self.current_speed_down.get()>1024):
                        self.current_speed_down.set(round(self.current_speed_down.get()/1024.,2))
                        self.speed_meter_down.set( speed[self.speed_m_down+1])
                        self.speed_m_down=self.speed_m_down+1
                        
                elif(self.current_speed_down.get()<10 and self.speed_m_down>0):
                        self.current_speed_down.set(round(self.current_speed_down.get()*1024.,2))
                        self.speed_meter_down.set( speed[self.speed_m_down-1])
                        self.speed_m_down=self.speed_m_down-1

    def force_logout(self,event):
        self.result = l.main("Logout",self.entry_1.get(),self.entry_2.get(),self.entry_3.get())
        if(self.result == "Logged out Successfully!!"):
             self.button_work.set("Login")
             messagebox.showinfo(title ="result",message=("Successfully logged out !!"))
        else: 
             messagebox.showinfo(title ="result",message=(self.result))
        
    def on_closing(self):
        if(self.button_work.get()=="Logout"):
            self.result = l.main("Logout",self.entry_1.get(),self.entry_2.get(),self.entry_3.get())
        f = open("Supportfiles/data","wb")
        c,d,e = self.consump_up,self.consump_down,self.consump_total
        while(d!=0):
            self.current_data_received.set(round(self.current_data_received.get()*1024.,2))
            d=d-1
        while(c!=0):
            self.current_data_sent.set(round(self.current_data_sent.get()*1024.,2))
            c=c-1
        while(e!=0):
            self.current_data_total.set(round(self.current_data_total.get()*1024.,2))
            e=e-1
        f.write(bytes(str(self.current_data_received.get()).encode('utf-8')+"-".encode('utf-8')+str(self.consump_down).encode('utf-8')+"\n".encode('utf-8')+str(self.current_data_sent.get()).encode('utf-8')+"-".encode('utf-8')+str(self.consump_up).encode('utf-8')+"\n".encode('utf-8')+str(self.current_data_total.get()).encode('utf-8')+"-".encode('utf-8')+str(self.consump_total).encode('utf-8')))
        f.close()
        os.kill(os.getpid(), signal.SIGTERM)
                     
    def login(self,event):
        self.result = l.main(self.button_work.get(),self.entry_1.get(),self.entry_2.get(),self.entry_3.get())
        print(self.result)
        if(self.entry_3.get() is not self.previous):
                if(self.p.get() is True):
                        self.previous=self.entry_3.get()
                        f= open("supportfiles/support",'wb')
                        f.write(bytes(self.previous,'utf-8'))
                        f.close()
        if(self.result == "Logged in"):
             self.button_work.set("Logout")
             messagebox.showinfo(title ="result",message=("Successfully logged in !!"))
        elif(self.result == "Logged out Successfully!!"):
             self.button_work.set("Login")
             messagebox.showinfo(title ="result",message=("Successfully logged out !!"))
        else: 
             messagebox.showinfo(title ="result",message=(self.result))
        
    def on_entry_click(self, event):

         if event.widget.config('fg') [4] == 'grey':
              event.widget.delete(0, "end" ) # delete all the text in the entry
              event.widget.insert(0, '') #Insert blank for user input
              event.widget.config(fg = 'black')
              
    def on_focusout(self, event, a):

        if event.widget.get() == '':
                event.widget.insert(0, default_text[a])
                event.widget.config(fg = 'grey')




if __name__=="__main__":

    img.intro()
    Is.start()
    root =Tk()
    root.wm_title("Network Monitor")
    root.call("wm", "attributes", ".", "-alpha", "0.95") # Window Opacity 0.0-1.0
    x =int(2*root.winfo_screenwidth()/3)
    y =int(root.winfo_screenheight()/3)
##    root.config(bg='#a1dbcd')
    root.geometry('520x310+{0}+{1}'.format(x,y))
    root.resizable(0,0)
    start_GUI = MainGUI(root)
    root.mainloop()

        
