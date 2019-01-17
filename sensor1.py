
import tkinter as tk
import threading
import os

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, top
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    top = Toplevel1 (root)
    read_sensor_data()
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
def read_sensor_data():
	
        threading.Timer(1.0, read_sensor_data).start()
        file = open("sensor_1.txt", 'r') 
        #txt = file.read()
        lineList = file.readlines()
        file.close()
        top.Label2.config(text = lineList[-1])
        
        file = open("sensor_2.txt", 'r') 
        #txt = file.read()
        lineList = file.readlines()
        file.close()
        top.Label3.config(text = lineList[-1])
        
        file = open("sensor_3.txt", 'r') 
        #txt = file.read()
        lineList = file.readlines()
        file.close()
        top.Label4.config(text = lineList[-1])
        
        file = open("sensor_4.txt", 'r') 
        #txt = file.read()
        lineList = file.readlines()
        file.close()
        top.Label5.config(text = lineList[-1])
        
        file = open("compass.txt", 'r') 
        #txt = file.read()
        lineList = file.readlines()
        file.close()
        top.Label1.config(text = lineList[-1])
  
def open_chart_sensor1():
	close_window()
	os.system('python3 sensor1.py')
	
	
def open_chart_sensor2():
	close_window()
	os.system('python3 sensor2.py')
	
def open_chart_sensor3():
	close_window()
	os.system('python3 sensor3.py')
	
def open_chart_sensor4():
	close_window()
	os.system('python3 sensor4.py')     
# open write/main message screen
def open_main_screen():
        close_window()
        os.system('python3 gui_ver2.py')
# open read message screen
def open_reading_screen():
        close_window()
        os.system('python3 messageread.py')
        
def open_sensor_reading():
        close_window()
        os.system('python3 onescreentorule.py')
def close_window(): 
        root.destroy()
class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 

        top.geometry("600x450+650+150")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.033, rely=0.022, relheight=0.922
                , relwidth=0.892)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=535)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.0, rely=0.024, height=41, width=114)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Compass Values''')
        self.Label1.configure(width=114)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.243, rely=0.217, height=91, width=194)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Sensor_2 values''')
        self.Label2.configure(width=194)

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.374, rely=0.024, height=41, width=164)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Sensor_1''')
        self.Label3.configure(width=164)

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.206, rely=0.024, height=41, width=114)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Sensor_2''')
        self.Label4.configure(width=114)

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.579, rely=0.0, height=51, width=154)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Sensor_4''')
        self.Label5.configure(width=154)


        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.206, rely=0.578, height=24, width=26)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''UP''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.187, rely=0.675, height=24, width=47)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''ENTER''')
        self.Button2.configure(width=47)

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.056, rely=0.675, height=24, width=36)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''LEFT''')
        self.Button3.configure(command=lambda: open_sensor_reading())

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.318, rely=0.675, height=24, width=45)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''RIGHT''')
        self.Button4.configure(command=lambda: open_chart_sensor2())

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.187, rely=0.771, height=24, width=48)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''DOWN''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.037, rely=0.867, height=24, width=41)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''BACK''')
        self.Button6.configure(command=lambda: open_main_screen())

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.168, rely=0.867, height=24, width=70)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''READ''')
        self.Button7.configure(width=70)
        self.Button7.configure(command=lambda: open_reading_screen())

        self.Button8 = tk.Button(self.Frame1)
        self.Button8.place(relx=0.336, rely=0.867, height=24, width=45)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''WRITE''')
        self.Button8.configure(command=lambda: open_main_screen())

        self.Button9 = tk.Button(self.Frame1)
        self.Button9.place(relx=0.579, rely=0.602, height=24, width=105)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''CHART SENSOR 1''')
        self.Button9.configure(command=lambda: open_chart_sensor1())

        self.Button10 = tk.Button(self.Frame1)
        self.Button10.place(relx=0.579, rely=0.699, height=24, width=105)
        self.Button10.configure(activebackground="#ececec")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="#d9d9d9")
        self.Button10.configure(disabledforeground="#a3a3a3")
        self.Button10.configure(foreground="#000000")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(pady="0")
        self.Button10.configure(text='''CHART SENSOR 2''')
        self.Button10.configure(command=lambda: open_chart_sensor2())

        self.Button11 = tk.Button(self.Frame1)
        self.Button11.place(relx=0.579, rely=0.795, height=24, width=105)
        self.Button11.configure(activebackground="#ececec")
        self.Button11.configure(activeforeground="#000000")
        self.Button11.configure(background="#d9d9d9")
        self.Button11.configure(disabledforeground="#a3a3a3")
        self.Button11.configure(foreground="#000000")
        self.Button11.configure(highlightbackground="#d9d9d9")
        self.Button11.configure(highlightcolor="black")
        self.Button11.configure(pady="0")
        self.Button11.configure(text='''CHART SENSOR 3''')
        self.Button11.configure(command=lambda: open_chart_sensor3())

        self.Button12 = tk.Button(self.Frame1)
        self.Button12.place(relx=0.579, rely=0.892, height=24, width=105)
        self.Button12.configure(activebackground="#ececec")
        self.Button12.configure(activeforeground="#000000")
        self.Button12.configure(background="#d9d9d9")
        self.Button12.configure(disabledforeground="#a3a3a3")
        self.Button12.configure(foreground="#000000")
        self.Button12.configure(highlightbackground="#d9d9d9")
        self.Button12.configure(highlightcolor="black")
        self.Button12.configure(pady="0")
        self.Button12.configure(text='''CHART SENSOR 4''')
        self.Button12.configure(command=lambda: open_chart_sensor4())


vp_start_gui()






