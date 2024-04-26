from tkinter import *

raiz= Tk()
MiFrame=Frame(raiz)
MiFrame.pack()


#---------------------declaración de variables---------------------

numeroPantalla=StringVar()
operacion=""
resultado=0
signo=""



#-----------------------------primera fila -----------------------
pantalla= Entry(MiFrame, textvariable=numeroPantalla)
pantalla.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="white", justify="right")

#-----------------------------funciones--------------------------------------------

def pulsarBoton(num):

    global operacion

    if operacion!="":
        numeroPantalla.set(num)
        operacion=""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)


def borrar():
    global resultado
    global num

    numeroPantalla.set(" ")
    resultado=0
    num=0

def suma(num):
    global operacion
    global resultado
    global signo

    operacion="suma"
    signo="suma"
    resultado+= int(num)
    numeroPantalla.set(resultado)

def resta(num):

    global operacion
    global resultado
    global signo


    operacion ="resta"
    signo="resta"
    if resultado==0:
        resultado += int(num)
    else:
        resultado-=int(num)
    numeroPantalla.set(resultado)


def mult(num):

    global operacion
    global resultado
    global signo

    if resultado==0:
        resultado +=int(num)
    else:
        resultado*=int(num)
    operacion= "mult"
    signo="mult"
    numeroPantalla.set(resultado)

def div(num):
    global operacion
    global resultado
    global signo


    operacion = "div"
    signo = "div"
    if resultado==0:
        resultado += int(num)
    else:
        resultado //= int(num)
    numeroPantalla.set(resultado)

def elResultado():

    global resultado

    if signo=="suma":
        numeroPantalla.set(resultado+int(numeroPantalla.get()))
    elif signo=="resta":
        numeroPantalla.set(resultado - int(numeroPantalla.get()))
    elif signo =="mult":
        numeroPantalla.set(resultado * int(numeroPantalla.get()))
    elif signo =="div":
        numeroPantalla.set(resultado // int(numeroPantalla.get()))
    resultado=0


#------------------------------primera fila-----------------------------------------

boton7=Button(MiFrame, text="7", width=3, command=lambda:pulsarBoton("7"))
boton7.grid(row=1, column=0, padx=10, pady=10)

boton8=Button(MiFrame, text="8", width=3, command=lambda:pulsarBoton("8"))
boton8.grid(row=1, column=1, padx=10, pady=10)

boton9=Button(MiFrame, text="9", width=3,command=lambda:pulsarBoton("9") )
boton9.grid(row=1, column=2, padx=10, pady=10)

botonMult=Button(MiFrame, text="x", width=3, command=lambda:mult(numeroPantalla.get()) )
botonMult.grid(row=1, column=3, padx=10, pady=10)

#-------------------------------------segunda fila-------------------------------
boton4=Button(MiFrame, text="4", width=3, command=lambda:pulsarBoton("4"))
boton4.grid(row=2, column=2, padx=10, pady=10)

boton5=Button(MiFrame, text="5", width=3, command=lambda:pulsarBoton("5"))
boton5.grid(row=2, column=1, padx=10, pady=10)

boton6=Button(MiFrame, text="6", width=3,command=lambda:pulsarBoton("6") )
boton6.grid(row=2, column=0, padx=10, pady=10)

botonDiv=Button(MiFrame, text="/", width=3, command=lambda:div(numeroPantalla.get()))
botonDiv.grid(row=2, column=3, padx=10, pady=10)

#---------------------------------tercera fila---------------------------------

boton1=Button(MiFrame, text="1", width=3,command=lambda:pulsarBoton("1") )
boton1.grid(row=3, column=2, padx=10, pady=10)

boton2=Button(MiFrame, text="2", width=3, command=lambda:pulsarBoton("2"))
boton2.grid(row=3, column=1, padx=10, pady=10)

boton3=Button(MiFrame, text="3", width=3,command=lambda:pulsarBoton("3") )
boton3.grid(row=3, column=0, padx=10, pady=10)

botonSum=Button(MiFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=3, column=3, padx=10, pady=10)

#------------------------------------cuarta fila--------------------------------

boton0=Button(MiFrame, text="0", width=3, command=lambda:pulsarBoton("0"))
boton0.grid(row=4, column=1, padx=10, pady=10)

botonRest=Button(MiFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4, column=3, padx=10, pady=10)

#-----------------------------------quinta fila-------------------------------------

botonIgual=Button(MiFrame, text="=", width=3, command=lambda:elResultado())
botonIgual.grid(row=5, column=3, padx=10, pady=10)

botonIgual=Button(MiFrame, text="bt", width=3,command=borrar)
botonIgual.grid(row=5, column=2, padx=10, pady=10)

botonComa=Button(MiFrame, text=",", width=3, command=lambda:pulsarBoton(","))
botonComa.grid(row=5, column=1, padx=10, pady=10)



raiz.mainloop()
