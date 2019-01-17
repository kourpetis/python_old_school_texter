
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
    messagereadGUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w, top, root
    root.destroy()
    w = None

# read sensors data each second
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


def read_file():
        global currentIndex, lines
        file_ = open("message_file.txt")
        
        # create list of lines
        #lines = file_.read().split('\n')
        lines = file_.readlines()
        file_.close()
        print(lines)
        
        # split every line in columns
        #lines = [l.split(',') for l in lines]
        
        if len(lines) > 0:
                top.Text1.delete('1.0', "end")
                top.Text1.insert("end", lines[-1])
                currentIndex = len(lines) - 1

def read_next_line():
        global currentIndex, lines
        try:
                lineCount = len(lines)
        except:
                lineCount = 0
        if lineCount > 0:
                if currentIndex == lineCount-1:
                        currentIndex = 0
                else :
                        currentIndex+=1
                
                top.Text1.delete('1.0', "end")
                top.Text1.insert("end", lines[currentIndex])

def read_previous_line():
        global currentIndex, lines
        try:
                lineCount = len(lines)
        except:
                lineCount = 0

        if lineCount > 0:
                if currentIndex == 0:
                        currentIndex = lineCount -1
                else :
                        currentIndex-=1
                
                top.Text1.delete('1.0', "end")
                top.Text1.insert("end", lines[currentIndex])

def move_down():
        top.Text1.see("end")
        
def move_up():
        top.Text1.see("1.0")

# open read message screen
def open_main_screen():
        close_window()
        os.system('python3 gui_ver2.py')
        
# close root window
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

        top.geometry("600x450+555+125")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.05, rely=0.067, relheight=0.9, relwidth=10.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=555)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.002, rely=0.049, height=41, width=84)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Compass_Value''')
        self.Label1.configure(width=84)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.018, rely=0.049, height=41, width=84)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Sensor_1''')
        self.Label2.configure(width=84)

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.033, rely=0.025, height=61, width=54)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Sensor_2''')
        self.Label3.configure(width=54)

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.048, rely=0.049, height=41, width=44)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Sensor_3''')
        self.Label4.configure(width=44)

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.062, rely=0.049, height=41, width=44)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Sensor_4''')
        self.Label5.configure(width=44)

        self.Text1 = tk.Text(self.Frame1)
        self.Text1.place(relx=0.003, rely=0.173, relheight=0.306, relwidth=0.067)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=404)
        self.Text1.configure(wrap='word')

        self.Button8 = tk.Button(self.Frame1)
        self.Button8.place(relx=0.007, rely=0.642, height=39, width=64)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''PREVIOUS
MESSAGE''')
        self.Button8.configure(command=lambda: read_previous_line())

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.02, rely=0.543, height=24, width=58)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''PAGE UP''')
        self.Button2.configure(command=lambda: move_up())


        self.Button9 = tk.Button(self.Frame1)
        self.Button9.place(relx=0.02, rely=0.642, height=34, width=56)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''ENTER''')
        self.Button9.configure(width=56)

        self.Button10 = tk.Button(self.Frame1)
        self.Button10.place(relx=0.033, rely=0.642, height=39, width=62)
        self.Button10.configure(activebackground="#ececec")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="#d9d9d9")
        self.Button10.configure(disabledforeground="#a3a3a3")
        self.Button10.configure(foreground="#000000")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(pady="0")
        self.Button10.configure(text='''NEXT
MESSAGE''')
        self.Button10.configure(command=lambda: read_next_line())

        self.Button12 = tk.Button(self.Frame1)
        self.Button12.place(relx=0.02, rely=0.765, height=39, width=54)
        self.Button12.configure(activebackground="#ececec")
        self.Button12.configure(activeforeground="#000000")
        self.Button12.configure(background="#d9d9d9")
        self.Button12.configure(disabledforeground="#a3a3a3")
        self.Button12.configure(foreground="#000000")
        self.Button12.configure(highlightbackground="#d9d9d9")
        self.Button12.configure(highlightcolor="black")
        self.Button12.configure(pady="0")
        self.Button12.configure(text='''PAGE
  DOWN''')
        self.Button12.configure(command=lambda: move_down())

        self.Button14 = tk.Button(self.Frame1)
        self.Button14.place(relx=0.007, rely=0.84, height=24, width=41)
        self.Button14.configure(activebackground="#ececec")
        self.Button14.configure(activeforeground="#000000")
        self.Button14.configure(background="#d9d9d9")
        self.Button14.configure(disabledforeground="#a3a3a3")
        self.Button14.configure(foreground="#000000")
        self.Button14.configure(highlightbackground="#d9d9d9")
        self.Button14.configure(highlightcolor="black")
        self.Button14.configure(pady="0")
        self.Button14.configure(text='''BACK''')
        self.Button14.configure(command=lambda: open_main_screen())

        self.Button16 = tk.Button(self.Frame1)
        self.Button16.place(relx=0.033, rely=0.84, height=24, width=45)
        self.Button16.configure(activebackground="#ececec")
        self.Button16.configure(activeforeground="#000000")
        self.Button16.configure(background="#d9d9d9")
        self.Button16.configure(disabledforeground="#a3a3a3")
        self.Button16.configure(foreground="#000000")
        self.Button16.configure(highlightbackground="#d9d9d9")
        self.Button16.configure(highlightcolor="black")
        self.Button16.configure(pady="0")
        self.Button16.configure(text='''WRITE''')
        self.Button16.configure(command=lambda: open_main_screen())

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.052, rely=0.519, height=24, width=107)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''USER 1 MESSAGES''')
        self.Button4.configure(command=lambda: read_file())

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.052, rely=0.617, height=24, width=107)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''USER 2 MESSAGES''')

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.052, rely=0.716, height=24, width=107)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''USER 3 MESSAGES''')

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.052, rely=0.815, height=24, width=107)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''USER 4 MESSAGES''')

vp_start_gui()





