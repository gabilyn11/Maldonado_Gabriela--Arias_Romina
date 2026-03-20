import tkinter
from tkinter import messagebox
import os

clientes=[] #VARIABLE UTILIZADA PARA GUARDAR LOS PEDIDOS DE LOS CLIENTES
total=0 #TOTAL DE TODAS LAS COMPRAS
totalCompra=0#TOTAL DEL CLIENTE
elegidos=[] #SABORES ELEGIDOS
datos=0 #VARIABLE UTILIZADA PARA LUEGO PASAR LA LISTA A UN STR

archivo = open("Ventas.txt", "w") #VARIABLE UTILIZADA PARA ABRIR EL ARCHIVO VENTAS
archivo.close()

def inicio():
    global datos, elegidos, clientes
    datos=0
    elegidos=[]
    clientes=[]
    global totalCompra
    totalCompra=0
    def cambio():
        ventana.destroy()
        venta()

    def venta():
        ventana2=tkinter.Tk()  #VARIABLE DE LA VENTANA 2
        ventana2.geometry(f"{ancho}x{alto}+{x}+{y}")
        ventana2.title("Comprar helado")

        helados=[] #VARIABLE PARA GUARDAR LOS HELADOS
        cantidades=[] #VARIABLE PARA GUARDAR LA CANTIDAD DE SABORES PERMITIDOS POR CADA HELADO
        precios=[] #VARIABLE PARA GUARDAR LOS PRECIOS

        archivo=open("helados.txt","r") #VARABLE PARA ABRIR EL ARCHIVO HELADOS
        linea=archivo.readline()

        tkinter.Label(ventana2, text="🍦 MENÚ DE HELADOS 🍦", font=("Arial", 16, "bold"), fg="#D81B60").pack(pady=20)

        while linea!="":
            hel,cant,prec=linea.split(",")
            cant=int(cant)
            prec=int(prec)

            helados.append(hel)
            cantidades.append(cant)
            precios.append(prec)

            linea=archivo.readline()

        archivo.close()
        contenedorFrames = tkinter.Frame(ventana2) #VARIABLE PARA ORDENAR DESPUÉS TODOS LOS FRAMES
        contenedorFrames.pack()

        frame = tkinter.Frame(contenedorFrames, borderwidth=1, relief="solid") #VARIABLE PARA 1 FRAME
        frame.pack(side="left", padx=20, pady=20)


        opcion=tkinter.IntVar() #VARIABLE PARA GUARDAR COMO NÚMERO ENTERO LA OPCION QUE EL USUARIO ELIJE

        tkinter.Label(frame,text="HELADOS", font=("Arial",12,"bold")).grid(row=0,column=0)

        for i in range(len(helados)):

            etiqueta=tkinter.Label(frame,text=f"{helados[i]}  ${precios[i]}", font=("Arial", 12)) #ETIQUETA PARA IR MOSTRANDO EL MENU GUARDADO EN EL ARCHIVO
            etiqueta.grid(row=i+1,column=0)

            radio=tkinter.Radiobutton(frame,variable=opcion,value=i) #SIRVE PARA QUE EL USUARIO ELIJ UNA OPCION Y LA GUARDE EN SU RESP. VARIABLE
            radio.grid(row=i+1,column=1)


        sabores=["Chocolate","Vainilla","Limón","Frutilla","Dulce de leche","Granizado","Menta"]

        frameSab = tkinter.Frame(contenedorFrames, borderwidth=1, relief="solid") #VARIABLE PARA EL FRAME 2
        frameSab.pack(side="left", padx=20, pady=5)

        tkinter.Label(frameSab,text="SABORES", font=("Arial",12,"bold")).pack()

        variables=[] #LISTA DE VARIABLES DONDE SE VAN A GUARDAR LAS OPCIONES DE SABOR QUE SE ELIJAN

        for s in range(len(sabores)):

            var=tkinter.IntVar()#VARIABLE PARA GUARDAR COMO NÚMERO ENTERO LA OPCION QUE EL USUARIO ELIJE
            variables.append(var)

            check=tkinter.Checkbutton(frameSab,text=sabores[s],variable=var, font=("Arial",12)) #SIRVE PARA QUE EL USUARIO ELIJ UNA OPCION Y LA GUARDE EN SU RESP. VARIABLE
            check.pack(anchor="w")


        def guardarSabores():
            global clientes, totalCompra, datos
            elegidos=[] 

            for i in range(len(sabores)):
                if variables[i].get()==1:
                    elegidos.append(sabores[i])

            bochas=opcion.get()  #vARIABLE QUE GUARDA EL VALOR QUE SE INGRESO EN OPCION

            if len(elegidos)==0:
                messagebox.showerror("Error","Elegí al menos un sabor")
                return

            if len(elegidos)>cantidades[bochas]:
                messagebox.showerror("Error","Elegiste demasiados sabores")
                return

            elegido=opcion.get()  
            datos=",".join(elegidos) 

            clientes.append({
                "helado": helados[elegido],
                "precio": precios[elegido],
                "sabores": ", ".join(elegidos)
            })
            totalCompra+=precios[elegido]
            datos=",".join(elegidos)
            messagebox.showinfo("Carrito","Helado agregado al carrito")

            for var in variables:
                var.set(0)


        contenedorBotones = tkinter.Frame(ventana2) #FRAME PARA LUEGO ORDENAR LOS DEMAS BOTONES
        contenedorBotones.pack(pady=20)

        botonAgregar = tkinter.Button(contenedorBotones, text="Agregar al carrito", command=guardarSabores, bg="#B3E5FC" , font=("Arial",10,"bold")) #BOTON DE AGREGAR AL CARRITO
        botonAgregar.pack(side="left", padx=10)



        def verCarrito():
            global clientes
            ventana2.destroy()

            ventana4=tkinter.Tk() #VENTANA PARA VER EL CARRITO DE COMPRA
            ventana4.geometry(f"{ancho}x{alto}+{x}+{y}")
            ventana4.title("Carrito")

            tkinter.Label(ventana4,text="🍦 CARRITO DE COMPRA 🍦",font=("Arial",16,"bold"), fg="#D81B60").pack(pady=20)
            
            framePedidos = tkinter.Frame(ventana4) #FRAME PARA LUEGO ORDENAR LOS DEMAS FRAMES
            framePedidos.pack()

            def mostrarPedidos():
                global total
                for widget in framePedidos.winfo_children():
                    widget.destroy()

                for r in range(len(clientes)):
                    fila = tkinter.Frame(framePedidos, bd=1, relief="solid", bg="#F5F5F5") #FRAME DONDE SE GUARDA LA INFO DE 1 HELADO
                    fila.pack(pady=5, fill="x", padx=10)
                    info = f"🍦 {clientes[r]['helado']}  |  ${clientes[r]['precio']}  |  {clientes[r]['sabores']}" # INFORMACION DE 1 HELADO
    
                    label = tkinter.Label(
                        fila,
                        text=info,
                        anchor="w",
                        bg="#F5F5F5",
                        font=("Arial", 11)
                    )
                    label.pack(side="left", padx=10, pady=5, expand=True, fill="x")
                    frameBotones = tkinter.Frame(fila, bg="#F5F5F5") #FRAME PARA DESPUES ORDENAR LOS BOTONES
                    frameBotones.pack(side="right", padx=5)
                    botonEditar = tkinter.Button(  #BOTON DE EDITAR LOS SABORES
                        frameBotones,
                        text="✏️",
                        bg="#FFA726",
                        activebackground="#FB8C00",
                        relief="flat",
                        command=lambda r=r: editarPedido(r)
                    )
                    botonEditar.pack(side="left", padx=3)
                    botonBorrar = tkinter.Button( #BOTON DE EDITAR UN HELADO
                        frameBotones,
                        text="🗑",
                        bg="#EF5350",
                        fg="white",
                        activebackground="#D32F2F",
                        relief="flat",
                        command=lambda r=r: borrarPedido(r)
                    )
                    botonBorrar.pack(side="left", padx=3)

            etiquetaTotal = tkinter.Label(  #ETIQUETA DEL TOTAL DE LA COMPRA
                ventana4,
                text=f"Total de la compra: {totalCompra}",
                bg="grey",
                font=("Arial",12)
            )
            etiquetaTotal.pack(fill=tkinter.X)
            def borrarPedido(indice):
                global totalCompra
                totalCompra-=clientes[indice]['precio']
                etiquetaTotal.config(
                    text=f"Total de la compra: {totalCompra}"
                )
                clientes.pop(indice)
                mostrarPedidos()

            def editarPedido(indice):
                global datos
                frameEditar = tkinter.Frame(ventana4, bd=2, relief="ridge", bg="#E3F2FD") #FRAME PARA LUEGO PONER EL FRAME DE EDITAR SABORES
                frameEditar.pack(fill="x", padx=10, pady=10)

                titulo = tkinter.Label(
                    frameEditar,
                    text="✏️ Editar sabores",
                    bg="#E3F2FD",
                    font=("Arial", 12, "bold")
                )
                titulo.pack(pady=5)
                frameChecks = tkinter.Frame(frameEditar, bg="#E3F2FD") #FRAME DONDE APARECEN LOS SABORES
                frameChecks.pack(pady=5)

                variables = []

                for s in range(len(sabores)):
                    var = tkinter.IntVar()
                    variables.append(var)

                    tkinter.Checkbutton(
                        frameChecks,
                        text=sabores[s],
                        variable=var,
                        bg="#E3F2FD"
                    ).pack(anchor="w")
                def confirmar():
                    global datos
                    elegidos = []

                    for i in range(len(variables)):
                        if variables[i].get() == 1:
                            elegidos.append(sabores[i])

                    if len(elegidos) == 0:
                        messagebox.showerror("Error", "Elegí al menos un sabor")
                        return

                    datos = ",".join(elegidos)
                    clientes[indice]["sabores"] = ", ".join(elegidos)

                    frameEditar.destroy()
                    mostrarPedidos()

                def cancelar():
                    frameEditar.destroy()
                frameBotones = tkinter.Frame(frameEditar, bg="#E3F2FD") #FRAME PARA ORDENAR LOS BOTONES
                frameBotones.pack(pady=10)

                tkinter.Button(  #BOTON DE CONFRIMAR
                    frameBotones,
                    text="Guardar",
                    bg="#66BB6A",
                    fg="white",
                    command=confirmar
                ).pack(side="left", padx=5)

                tkinter.Button( #BOTON PARA CANCELAR
                    frameBotones,
                    text="Cancelar",
                    bg="#EF5350",
                    fg="white",
                    command=cancelar
                ).pack(side="left", padx=5)
            
            mostrarPedidos()
            tkinter.Button( #BOTON PARA VOLVER
                ventana4,
                text="Volver",
                command= lambda:[ventana4.destroy(),venta()]
            ,bg="#FFD1DC").pack(pady=10)

            def cambio2():
                global clientes, datos, total
                ventana4.destroy()
                with open("Ventas.txt", "a") as archivoVentas:
                    for e in range(len(clientes)):
                        archivoVentas.write(f"{clientes[e]['helado']},{clientes[e]['precio']},{clientes[e]['sabores']}\n") 
                        total+=clientes[e]['precio']
                archivoVentas.close()
                inicio()

            tkinter.Button( #BOTON PARA FINALIZAR LA COMPRA
                ventana4,
                text="Finalizar compra",
                command=cambio2, bg="#B3E5FC"
            ).pack(pady=10)



        botonCarrito=tkinter.Button(contenedorBotones,text="Ver carrito",command=verCarrito, bg="#FFD1DC", font=("Arial",10,"bold")) #BOTON PARA VER EL CARRITO
        botonCarrito.pack(side="left", padx=10)

        ventana2.mainloop()



    def empleador():
        global total
        ventana.destroy()
        ventana3=tkinter.Tk() #VENTANA 3 PARA LAS VENTAS DEL DIA
        ventana3.geometry(f"{ancho}x{alto}+{x}+{y}")
        ventana3.title("Ventas del día")
        etiquetaVentas=tkinter.Label(ventana3, text="🍦 HISTORIAL DE VENTAS 🍦", font=("Arial", 16, "bold"), fg="#D81B60").pack(pady=20)

        area = tkinter.Text(ventana3, height=15, width=45) #CREA UN CUADRO DE TEXTO
        area.pack(pady=10)

        Ventas="Ventas.txt"

        if os.path.exists(Ventas):
            with open(Ventas, "r") as f:
                area.insert(tkinter.END, f.read())
        else:
            area.insert(tkinter.END, "No hay ventas registradas.")
        
        def cambio3():
                ventana3.destroy()
                inicio()
        

        tkinter.Label(ventana3, text=f"Total: {total}", bg="grey", font=("Arial", 12)).pack(fill=tkinter.X, pady=5) #MUESTRA EL TOTAL DE TODAS LAS VENTAS
        area.config(state="disabled")
        botonVolver = tkinter.Button(ventana3, text="VOLVER AL MENÚ", command=cambio3, bg="#B3E5FC") #BOTON PARA VOLVER A LA PANTALLA PRINCIPAL
        botonVolver.pack(pady=5)


    def contraseña():
        contra=tkinter.Entry(ventana, show="*") #ENTRADA DE TEXTO DONDE SE PONE LA CONTRASEÑA
        contra.pack(pady=10)
        def verificar():
            clave = "1234abcd"
            if contra.get() != clave:
                messagebox.showerror("Error", "Contraseña inválida")
                return
            empleador()
        botonVerif=tkinter.Button(ventana, text="Ingresar",command=verificar) #BOTON PARA INGRESAR LA CONTRASEÑA
        botonVerif.pack(pady=5)

    ventana=tkinter.Tk() #VENTANA DE INICIO
    ancho = 600 #ANCHO DE LA VENTANA
    alto = 700 #ALTO DE LA VENTANA
    x = 468 #UBICACION X DONDE SE VA A UBICAR UNA VEZ QUE SE INICIE LA PANTALLA
    y = 50 #UBICACION Y DONDE SE VA A UBICAR UNA VEZ QUE SE INICIE LA PANTALLA

    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
    ventana.title("Dulce Frío")

    tkinter.Label(ventana, text="🍦 HELADERÍA 🍦", font=("Arial", 22, "bold"),  fg="#D81B60").pack(pady=10) #VARIABLES PARA HACER EL TÍTULO
    tkinter.Label(ventana, text="Dulce Frío", font=("Freestyle Script", 26), fg="#D81B60").pack()

    boton1=tkinter.Button(ventana,text="Empezar a comprar",width=25, bg="#FFD1DC", font=("Arial", 11, "bold"),command=cambio) #BOTÓN PARA EMPEZAR A COMPRAR
    boton1.pack(pady=20)

    boton2=tkinter.Button(ventana,text="Ventas del día", width=25, bg="#B3E5FC", #BOTON PARA VER LAS VENTAS DEL DÍA
              font=("Arial", 11, "bold"),command=contraseña)
    boton2.pack()

    ventana.mainloop()

inicio()