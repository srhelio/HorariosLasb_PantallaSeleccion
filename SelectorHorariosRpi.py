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
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L1")  

def openLab2():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L2")  

def openLab3():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L3")  

def openLab4():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L4")  

def openLab5A():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L5A")  

def openLab5B():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L5B")  

def openLab6A():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L6A")  

def openLab6B():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L6B")  

def openLab7B():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L7B")  

def openLab8A():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L8A")  

def openLab8B():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L8B")  

def openLab9():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L9")  

def openLab10():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L10")  

def openLab11():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L11")  

def openLab12():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L12")  

def openLab14():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L14")  

def openLab15():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L15")  

def openLab16():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/L16")  

def openLabLibre():
        CerrarNavegador()
        webbrowser.open("http://127.0.0.1:paddingx00/horarios/Labslibres")  

def salir(event):
        if event.char == "q":
                exit(0)

root = Tk()
root.attributes('-fullscreen', True)
root.config(bg="#252a2e")
root.title("SELECCIÓN DE HORARIOS DE LABORATORIOS")

paddingx=15
paddingy=120
boton_ancho=7
boton_alto=4

root.bind("<Key>", salir)

# widgets 
label1 = Label(root, text = 'SELECCIÓN DE HORARIOS DE LABORATORIOS', 
                 bg="orange", 
                 fg="black",
                 width=60,
                 height=3,
                 borderwidth=1, 
                 font=('arial', 24, 'bold'),).grid(padx= 20, pady = 80, columnspan=12, rowspan=2)

button1 = Button(root, text = 'Lab. 1', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1", 
                 font=('arial', 22, 'bold'),
                 command=openLab1).grid(row=2, column=4, padx = paddingx, pady = 15)
button2 = Button(root, text = 'Lab. 2',
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1", 
                 font=('arial', 22, 'bold'),
                 command=openLab2).grid(row=2, column=3, padx = paddingx)
button3 = Button(root, text = 'Lab. 3', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1", 
                 font=('arial', 22, 'bold'),
                 command=openLab3).grid(row=2, column=2, padx = paddingx)
button4 = Button(root, text = 'Lab. 4', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1", 
                 font=('arial', 22, 'bold'),
                 command=openLab4).grid(row=2, column=1, padx = paddingx)
button5a = Button(root, text = 'Lab. 5A', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1", 
                 font=('arial', 22, 'bold'),
                 command=openLab5A).grid(row=4, column=1, padx = paddingx, pady = 15)
button5b = Button(root, text = 'Lab. 5B', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1",
                 font=('arial', 22, 'bold'),
                 command=openLab5B).grid(row=4, column=2, padx = paddingx)
button6a = Button(root, text = 'Lab. 6A', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1",
                 font=('arial', 22, 'bold'),
                 command=openLab6A).grid(row=4, column=3, padx = paddingx)
button6b = Button(root, text = 'Lab. 6B', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1",
                 font=('arial', 22, 'bold'),
                 command=openLab6B).grid(row=4, column=4, padx = paddingx)
button7b = Button(root, text = 'Lab. 7B', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1",
                 font=('arial', 22, 'bold'),
                 command=openLab7B).grid(row=4, column=9, padx = paddingx)
button8a = Button(root, text = 'Lab. 8A', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1",
                 font=('arial', 22, 'bold'),
                 command=openLab8A).grid(row=4, column=10, padx = paddingx)
button8b = Button(root, text = 'Lab. 8B', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1",
                 font=('arial', 22, 'bold'),
                 command=openLab8B).grid(row=4, column=11, padx = paddingx)
button9 = Button(root, text = 'Lab. 9', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1",
                 font=('arial', 22, 'bold'),
                 command=openLab9).grid(row=2, column=11, padx = paddingx)
button10 = Button(root, text = 'Lab. 10', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1",
                 font=('arial', 22, 'bold'),
                 command=openLab10).grid(row=2, column=10, padx = paddingx)
button11 = Button(root, text = 'Lab. 11', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1",
                 font=('arial', 22, 'bold'),
                 command=openLab11).grid(row=2, column=9, padx = paddingx)
button12 = Button(root, text = 'Lab. 12', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1",
                 font=('arial', 22, 'bold'),
                 command=openLab12).grid(row=2, column=8, padx = paddingx)
button14 = Button(root, text = 'Lab. 14', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1",
                 font=('arial', 22, 'bold'),
                 command=openLab14).grid(row=3, column=7, padx = paddingx, pady = 15)
button15 = Button(root, text = 'Lab. 15', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1",
                 font=('arial', 22, 'bold'),
                 command=openLab15).grid(row=3, column=6, padx = paddingx)
button16 = Button(root, text = 'Lab. 16', 
                 bg="blue", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1",
                 font=('arial', 22, 'bold'),
                 command=openLab16).grid(row=3, column=5, padx = paddingx)
buttonLibre = Button(root, text = 'LIBRES', 
                 bg="green", 
                 fg="white", 
                 borderwidth=1,
                 width=boton_ancho,
                 height=boton_alto,
                 activebackground="#1c7fe1",
                 font=('arial', 26, 'bold'),
                 command=openLabLibre).grid(row=5, column=6, padx = paddingx)



root.mainloop()