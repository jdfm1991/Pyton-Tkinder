from db.connectionDB import ConnectionDB
import customtkinter as ctk
import tkinter as tk 
from tkinter import *
from customtkinter import CTk, CTkFrame
from tkinter.font import BOLD
import util.generic as utl


class MastelPanel():
    #Contructor que se encargar de mostrar la ventana de la aplicacion
    def __init__(self):
        #creacion de objeto que guarda las clases para el dineño de la ventata
        self.windows = ctk.CTk()
        self.menu = tk.Menu()
        
        #Creacion variable de control
        self.menu2 = True
        self.color = True
        
        #Varible de uso tabla de base de datos
        self.id = StringVar()
        self.pname = StringVar()
        self.bid  = StringVar()
        self.ref = StringVar()
        self.detail = StringVar()
        self.unit = StringVar()
        self.priceu1 = StringVar()
        self.priceu2 = StringVar()
        self.priceu3 = StringVar()
        self.pimage = StringVar()
        
        #variable de busqueda
        self.search = StringVar()
        self.searchup = StringVar()
        
        #Creacion de objeto de conexcion
        self.dbconect = ConnectionDB()
        
        #inicio de creacion de diseño grafico de la aplicacion (menu principal)

        #frame logo (lateral Izquierdo de la pantalla)
        frame_logo = tk.Frame(self.windows, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3B4F70')
        frame_logo.pack(side='left',expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#3B4F70')
        label.place(x=0, y=0, relwidth=1, relheight=1)
        #end frame logo
        
        
        #Creacion del cintillo para las opciones del menu principal (inicio)
        self.menu_start = tk.Menu(self.menu, tearoff=0)
        self.menu_files = tk.Menu(self.menu, tearoff=0)
        self.menu_transactions = tk.Menu(self.menu, tearoff=0)
        self.menu_reports = tk.Menu(self.menu, tearoff=1)
        
        #Creacion de la opciones en cascade del menu desplegable
        self.menu.add_cascade(label="Inicio", menu= self.menu_start)
        self.menu.add_cascade(label="Archivo", menu= self.menu_files)
        self.menu.add_cascade(label="Transacciones", menu= self.menu_transactions)
        self.menu.add_cascade(label="Reportes", menu= self.menu_reports)
        
        #Creacion de la sub opciones del  menu
        #sub opciones del menu Inicio
        self.menu_start.add_command(label="Salir", command=self.windows.quit)
        
        #sub opciones del menu Archivo
        self.menu_files.add_command(label="opcion 1")
        self.menu_files.add_command(label="opcion 2")
        
        #sub opciones del menu Transacciones
        self.menu_transactions.add_command(label="opcion 1")
        self.menu_transactions.add_command(label="opcion 2")
        
        #sub opciones del menu Transacciones > mas (Sub Cascada)
        self.menu_plus = tk.Menu(self.menu_transactions, tearoff=0)
        self.menu_plus.add_command(label="opcion 1")
        self.menu_plus.add_command(label="opcion 2")
        self.menu_plus.add_command(label="opcion 3", state=tk.DISABLED)
        
        #sub opciones del menu mas a la opcion de Transacciones (Sub Cascada)
        self.menu_transactions.add_cascade(label="Mas", menu=self.menu_plus)
        
        #sub opciones del menu Reportes
        self.menu_reports.add_command(label="opcion 1")
        self.menu_reports.add_command(label="opcion 2")
        #Creacion del cintillo para las opciones del menu principal (Fin)
        
        self.windows.title('Master Panel')
        w, h = self.windows.winfo_screenwidth(), self.windows.winfo_screenheight()
        self.windows.geometry("%dx%d+0+0" % (w, h))
        self.windows.config(bg='#fcfcfc', menu=self.menu)
        self.windows.resizable(width=0, height=0)
        
        logo = utl.read_img("./img/logo.png", (200, 200))
        
        label = tk.Label(self.windows, image=logo, bg='#3B4F70')
        label.place(x=0, y=0, relwidth=1, relheight=1)
        self.windows.mainloop()