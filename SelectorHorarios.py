from tkinter import *
import webbrowser

#from tkinter import ttk
import os 
browserExe= "chrome.exe" 
#browserExe = "chromium" 
#os.system("pkill " +browserExe)
os.system("taskkill /IM " +browserExe)

def CerrarNavegador():
        browserExe= "chrome.exe" 
        os.system("taskkill /IM " +browserExe) 

def openLab1():
        webbrowser.open("http://127.0.0.1:3000/horarios/L1")  

def openLab2():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L2")  

def openLab3():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L3")  

def openLab4():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L4")  

def openLab5A():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L5A")  

def openLab5B():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L5B")  

def openLab6A():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L6A")  

def openLab6B():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L6B")  

def openLab7B():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L7B")  

def openLab8A():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L8A")  

def openLab8B():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L8B")  

def openLab9():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L9")  

def openLab10():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L10")  

def openLab11():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L11")  

def openLab12():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L12")  

def openLab14():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L14")  

def openLab15():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L15")  

def openLab16():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/L16")  

def openLabLibre():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:3000/horarios/Labslibres")  

def salir(event):
        if event.char == "q":
                exit(0)

root = Tk()
root.attributes('-fullscreen', True)
root.config(bg="#252a2e")
root.title("SELECCIÓN DE HORARIOS DE LABORATORIOS")



root.bind("<Key>", salir)

# widgets 
label1 = Label(root, text = 'SELECCIÓN DE HORARIOS DE LABORATORIOS', 
                 bg="orange", 
                 fg="black",
                 width=40,
                 height=3,
                 borderwidth=1, 
                 font=('arial', 26, 'bold'),).grid(columnspan=10, rowspan=2)

button1 = Button(root, text = 'Lab. 1', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1", 
                 font=('arial', 18, 'bold'),
                 command=openLab1).grid(row=2, column=0, padx = 20, pady = 150)
button2 = Button(root, text = 'Lab. 2',
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1", 
                 font=('arial', 18, 'bold'),
                 command=openLab2).grid(row=2, column=1, padx = 20)
button3 = Button(root, text = 'Lab. 3', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1", 
                 font=('arial', 18, 'bold'),
                 command=openLab3).grid(row=2, column=2, padx = 20)
button4 = Button(root, text = 'Lab. 4', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1", 
                 font=('arial', 18, 'bold'),
                 command=openLab4).grid(row=2, column=3, padx = 20)
button5a = Button(root, text = 'Lab. 5A', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1", 
                 font=('arial', 18, 'bold'),
                 command=openLab5A).grid(row=2, column=4, padx = 20)
button5b = Button(root, text = 'Lab. 5B', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1",
                 font=('arial', 18, 'bold'),
                 command=openLab5B).grid(row=2, column=5, padx = 20)
button6a = Button(root, text = 'Lab. 6A', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1",
                 font=('arial', 18, 'bold'),
                 command=openLab6A).grid(row=2, column=6, padx = 20)
button6b = Button(root, text = 'Lab. 6B', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1",
                 font=('arial', 18, 'bold'),
                 command=openLab6B).grid(row=2, column=7, padx = 20)
button7b = Button(root, text = 'Lab. 7B', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1",
                 font=('arial', 18, 'bold'),
                 command=openLab7B).grid(row=2, column=8, padx = 20)
button8a = Button(root, text = 'Lab. 8A', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1",
                 font=('arial', 18, 'bold'),
                 command=openLab8A).grid(row=2, column=9, padx = 20)
button8b = Button(root, text = 'Lab. 8B', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1",
                 font=('arial', 18, 'bold'),
                 command=openLab8B).grid(row=3, column=0, padx = 20)
button9 = Button(root, text = 'Lab. 9', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1",
                 font=('arial', 18, 'bold'),
                 command=openLab9).grid(row=3, column=1, padx = 20)
button10 = Button(root, text = 'Lab. 10', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1",
                 font=('arial', 18, 'bold'),
                 command=openLab10).grid(row=3, column=2, padx = 20)
button11 = Button(root, text = 'Lab. 11', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1",
                 font=('arial', 18, 'bold'),
                 command=openLab11).grid(row=3, column=3, padx = 20)
button12 = Button(root, text = 'Lab. 12', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1",
                 font=('arial', 18, 'bold'),
                 command=openLab12).grid(row=3, column=4, padx = 20)
button14 = Button(root, text = 'Lab. 14', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1",
                 font=('arial', 18, 'bold'),
                 command=openLab14).grid(row=3, column=5, padx = 20)
button15 = Button(root, text = 'Lab. 15', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1",
                 font=('arial', 18, 'bold'),
                 command=openLab15).grid(row=3, column=6, padx = 20)
button16 = Button(root, text = 'Lab. 16', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1",
                 font=('arial', 18, 'bold'),
                 command=openLab16).grid(row=3, column=7, padx = 20)
buttonLibre = Button(root, text = 'LIBRES', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=7,
                 height=4,
                 activebackground="#1c7fe1",
                 font=('arial', 18, 'bold'),
                 command=openLabLibre).grid(row=3, column=9, padx = 20)



root.mainloop()





'''
if __name__ == '__main__':
    kivySaludo().run()
'''