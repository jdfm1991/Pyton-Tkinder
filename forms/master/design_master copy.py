import customtkinter as ctk
import tkinter as tk 
from tkinter import ttk, PhotoImage
from customtkinter import CTk, CTkFrame, CTkButton
from tkinter.font import BOLD
import util.generic as utl

class DesignMaster:
    
    #Metodo de llamada de vistas de pantallas
    def screenhome(self):
        pass
    
    def screendata(self):
         pass
     
    def screensetting(self):
         pass
    #Metodo para posicion de menu
    def sidebar(self):
        pass
    # funcion para crear ventana    
    def __init__(self):
        super().__init__()
        
        #configuracion inicial de Ventana de login
        self.windows = ctk.CTk()        
        self.windows.title('Master Panel')
        w, h = self.windows.winfo_screenwidth(), self.windows.winfo_screenheight()
        self.windows.geometry("%dx%d+0+0" % (w, h))
        self.windows.config(bg='#fcfcfc')
        self.windows.resizable(width=0, height=0)
        self.windows.columnconfigure(1, weight=1)
        self.windows.rowconfigure(1, weight=1)
        
        #Declaracion de variable de control (inicio)
        self.menu = True
        #Declaracion de variable de control (inicio)
        
        #Declaracion de variable que guardan las imagenas del sistemas (inicio)
        self.img_major = tk.PhotoImage(file ='./img/inicio.png')
        self.img_menu = tk.PhotoImage(file ='./img/menu.png')
        self.img_data = tk.PhotoImage(file ='./img/datos.png')
        self.img_load = tk.PhotoImage(file ='./img/escribir.png')
        self.img_upda = tk.PhotoImage(file ='./img/actualizar.png')
        self.img_sear = tk.PhotoImage(file ='./img/buscar.png')
        self.img_conf = tk.PhotoImage(file ='./img/configuracion.png')
        
        self.logo = utl.read_img("./img/logo.png", (200, 200))
        
        self.img_one = tk.PhotoImage(file ='./img/imagen_uno.png')
        self.img_two = tk.PhotoImage(file ='./img/imagen_dos.png')
        self.img_day = tk.PhotoImage(file ='./img/dia.png')
        self.img_nig = tk.PhotoImage(file ='./img/noche.png')
        #Declaracion de variable que guardan las imagenas del sistemas (Fin)
        
        #Creacion de Frame del Diseño visual (inicio)
        
        #frame que guarda el boton de inicio (inicio)
        self.frame_init = tk.Frame(self.windows, bg='black', width=50, height=45)
        self.frame_init.grid_propagate(0)
        self.frame_init.grid(column=0, row = 0, sticky='nsew')
        #frame que guarda el boton de inicio (fin)
        
        #frame que guarda las opciones del menu (inicio)
        self.frame_menu = tk.Frame(self.windows, bg='black', width = 50)
        self.frame_menu.grid_propagate(0)
        self.frame_menu.grid(column=0, row = 1, sticky='nsew')
        #frame que guarda las opciones del menu (fin)
        
         #frame que guarda las opciones del menu (inicio)
        self.frame_top = tk.Frame(self.windows,bg='black', height = 50)
        self.frame_top.grid(column = 1, row = 0, sticky='nsew')
        #frame que guarda las opciones del menu (fin)
        
       
        
        #frame que guarda el cuerpo de la aplicacion (inicio)
        self.frame_major = tk.Frame(self.windows, bg='black')
        self.frame_major.grid(column=1, row=1, sticky='nsew')
        self.frame_major.columnconfigure(0, weight=1)
        self.frame_major.rowconfigure(0, weight=1)
        #frame que guarda el cuerpo de la aplicacion (fin)
        
        #Creacion de Frame del Diseño visual (fin)
        
        #Creacion botones contenidos en el frame de inicio (inicio)
        self.btn_init = tk.Button(self.frame_init, image= self.img_major, bg='black',activebackground='black', bd=0, command= self.sidebar)
        self.btn_init.grid(column=0, row=0, padx=5, pady=10)
        self.btn_clos = tk.Button(self.frame_init, image= self.img_menu, bg='black',activebackground='black', bd=0, command= self.sidebar)
        self.btn_clos.grid(column=0, row=0, padx=5, pady=10)
        #Creacion botones contenidos en el frame de inicio (fin)
        
        #Creacion de las paginas del sistema y sus respativos frame
        self.page = ttk.Notebook(self.frame_major , style= 'TNotebook') #style = 'TNotebook'
        self.page.grid(column=0,row=0, sticky='nsew')
        
        #Vista de pantalla de inicio (inicio)
        self.title_home = tk.Label(self.frame_top, text= 'Pantalla inical de la aplicacion', bg='black', fg= 'DarkOrchid1', font= ('time', 15, 'bold'))
        self.title_home.pack(expand=1)
  
  
        self.frame_home = tk.Frame(self.page, bg='DarkOrchid1')
        self.label_home_t = tk.Label(self.frame_home, text="esto es home",  bg='DarkOrchid1', fg= 'white', font= ('Freehand521 BT', 20, 'bold'))
        self.label_home_t.pack(expand=1)
        self.label_home_i = tk.Label(self.frame_home, image=self.logo,  bg='DarkOrchid1')
        self.label_home_i.pack(expand=1)
        #Vista de pantalla de inicio (fin)
        
        #Vista de pantalla de Datos (inicio)
        self.frame_data = tk.Frame(self.page, bg='white')
        #utl.center_windows(self.frame_data,w,h)
        self.page.add(self.frame_data)
        
        self.label_data =tk.Label(self.frame_data, text= 'Datos Registrados', bg= 'white', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold'))
        self.label_data.grid(column =0, row=0)
        
        self.data_view = tk.Frame(self.frame_data, bg= 'gray90')
        self.data_view.grid(columnspan=3, row=2, sticky='nsew')
        self.view_d = ttk.Treeview(self.data_view)
        self.view_d.grid(column=0, row=0, sticky='nsew')
        self.data_sx = ttk.Scrollbar(self.data_view, orient='horizontal', command=self.view_d.xview)
        self.data_sx.grid(column=0, row = 1, sticky='ew')
        self.data_sy = ttk.Scrollbar(self.data_view, orient='vertical', command=self.view_d.yview)
        self.data_sy.grid(column = 1, row = 0, sticky='ns')
        #creacion de vista en pantalla(inicio)
        
        #creacion de vista en pantalla(fin)
        #Vista de pantalla de Datos (fin)
        
        #Vista de pantalla de Configutacion (inicio)
        self.frame_conf = tk.Frame(self.page, bg='white')
        self.page.add(self.frame_conf)
        
        self.label_conf = tk.Label(self.frame_conf, text="Configuracion", bg='white', fg= 'DarkOrchid1', font= ('Comic Sans MS', 12, 'bold'))
        self.label_conf.grid(column =0, row=0)
        
        self.conf_view =tk.Label(self.frame_conf, bg= 'gray90') 
        self.conf_view.grid(columnspan=4, row=2, sticky='nsew')
        self.view_c = ttk.Treeview(self.conf_view)
        self.view_c.grid(column=0, row=0, sticky='nsew')
        self.conf_sx = ttk.Scrollbar(self.conf_view, orient='horizontal', command=self.view_c.xview)
        self.conf_sx.grid(column=0, row = 1, sticky='ew')
        self.conf_sy = ttk.Scrollbar(self.conf_view, orient='vertical', command=self.view_c.yview)
        self.conf_sy.grid(column = 1, row = 0, sticky='ns')   
               
        #Vista de pantalla de Configutacion (fin)
        
        
        #Creacion de etiquetas y botones del menu
        self.btn_data = tk.Button(self.frame_menu, image=self.img_data,bg='black', activebackground='black', bd=0, command=self.screendata)
        self.btn_data.grid(column=0, row=1, pady=20,padx=10)
        self.label_data =tk.Label(self.frame_menu, text= 'Informacion', bg= 'black', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold'))
        self.label_data.grid(column=1, row=1, pady=20, padx=2)
        
        self.btn_sett = tk.Button(self.frame_menu, image=self.img_conf,bg='black', activebackground='black', bd=0, command=self.screensetting)
        self.btn_sett.grid(column=0, row=2, pady=20,padx=10)
        self.label_data =tk.Label(self.frame_menu, text= 'Configuracion', bg= 'black', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold'))
        self.label_data.grid(column=1, row=2, pady=20, padx=2)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        self.windows.mainloop()