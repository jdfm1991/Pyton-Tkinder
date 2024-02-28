import tkinter as tk 
import customtkinter as ctk
from tkinter import ttk
from customtkinter import *
from tkinter.font import BOLD
import util.generic as utl

class DesignRegister:
    
   #Metodo para Registar usuario
    def register(self):
       pass
         
    # funcion para crear ventana    
    def __init__(self):
        #configuracion inicial de Ventana de login
        self.windows = ctk.CTkToplevel()
        self.windows.title('Registar Usuario')
        self.windows.config(bg='#fcfcfc')
        self.windows.resizable(width=0, height=0)
        utl.center_windows(self.windows,600,480)
        
        #llamada de logo
        logo = utl.read_img("./img/logo.png", (200, 200))
        
        #frame logo (lateral Izquierdo de la pantalla)
        frame_logo = tk.Frame(self.windows, bd=0, width=200, relief=tk.SOLID, padx=10, pady=10, bg='#6A3B70')
        frame_logo.pack(side='left',expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#6A3B70')
        label.place(x=0, y=0, relwidth=1, relheight=1)
        #end frame logo
        
        #frame form (lateral Izquierdo de la pantallas)
        frame_form = tk.Frame(self.windows, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side='right', expand=tk.YES, fill=tk.BOTH)
        #end frame form
        
        #frame form title
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side='top', fill=tk.X)
        title = tk.Label(frame_form_top, text='Registro de usuario', font=('Times', 30), fg='#666a88', bg='#fcfcfc', pady=50)
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
        
        confirm_tag = tk.Label(frame_form_fill, text='Confimar Contraseña', font=('Times', 14),  fg='#666a88', bg='#fcfcfc', anchor='w')
        confirm_tag.pack(fill=tk.X, padx=20, pady=5)
        self.confirm = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.confirm.pack(fill=tk.X, padx=20, pady=10)
        self.confirm.config(show='*')
        #end frame form pass
        
        #frame form buttom      
        start = tk.Button(frame_form_fill, text='Registrar', font=('Times', 15, BOLD), bg='#fcfcfc', bd=0, fg='#6A3B70', command=self.register)
        start.pack(fill=tk.X, padx=20, pady=20)
        start.bind("<Return>", (lambda event : self.register()))
        #end frame form buttom
        
        #end frame form body (contenido de la aplicacion)
        
        #Funcion para crear ventana grafica
        self.windows.mainloop()
        