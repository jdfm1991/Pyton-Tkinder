import customtkinter as ctk
import tkinter as tk 
from tkinter import ttk, PhotoImage
from customtkinter import CTk, CTkFrame
from tkinter.font import BOLD
import util.generic as utl

class DesignLogin:
    
    #Metodo para verifica usuario
    def verify(self):
       pass
         
    #Metodo para Crear usuario usuario
    def create(self):
        pass
    
    # funcion para crear ventana    
    def __init__(self):
        #configuracion inicial de Ventana de login
        self.windows = ctk.CTk()
        self.windows.title('Inicio de Sesion')
        self.windows.geometry('600x450')
        self.windows.config(bg='#fcfcfc')
        self.windows.resizable(width=0, height=0)
        utl.center_windows(self.windows,600,450)
        
        #llamada de logo
        logo = utl.read_img("./img/logo.png", (200, 200))
        
        
        #frame logo (lateral Izquierdo de la pantalla)
        frame_logo = tk.Frame(self.windows, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3B4F70')
        frame_logo.pack(side='left',expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#3B4F70')
        label.place(x=0, y=0, relwidth=1, relheight=1)
        #end frame logo
        
        #frame form (lateral Izquierdo de la pantallas)
        frame_form = tk.Frame(self.windows, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side='right', expand=tk.YES, fill=tk.BOTH)
        #end frame form
        
        #frame form title
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side='top', fill=tk.X)
        title = tk.Label(frame_form_top, text='Inicio de Sesion', font=('Times', 30), fg='#666a88', bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        #end frame form title
        
        #frame form foot
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)
        #end frame form foot
        
        #frame form body (contenido de la aplicacion)
        
        #frame form user
        user_tag = tk.Label(frame_form_fill, text='Usuario', font=('Times', 14),  fg='#666a88', bg='#fcfcfc', anchor='w')
        user_tag.pack(fill=tk.X, padx=20, pady=5)
        self.user = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.user.pack(fill=tk.X, padx=20, pady=10)
        #end frame form user
        
        #frame form pass
        pass_tag = tk.Label(frame_form_fill, text='Contraseña', font=('Times', 14),  fg='#666a88', bg='#fcfcfc', anchor='w')
        pass_tag.pack(fill=tk.X, padx=20, pady=5)
        self.passw = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.passw.pack(fill=tk.X, padx=20, pady=10)
        self.passw.config(show='*')
        #end frame form pass
        
        #frame form buttom
        start = tk.Button(frame_form_fill, text='Iniciar sesion', font=('Times', 15, BOLD), bg='#3B4F70', bd=0, fg='#fff', command=self.verify)
        start.pack(fill=tk.X, padx=20, pady=20)
        start.bind("<Return>", (lambda event : self.verify()))
        
        start = tk.Button(frame_form_fill, text='Registrar usuario', font=('Times', 15, BOLD), bg='#fcfcfc', bd=0, fg='#3B4F70', command=self.create)
        start.pack(fill=tk.X, padx=20, pady=20)
        start.bind("<Return>", (lambda event : self.create()))
        #end frame form buttom
        
        #end frame form body (contenido de la aplicacion)
        
        #Funcion para crear ventana grafica
        self.windows.mainloop()
        