import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
from customtkinter import CTk, CTkFrame, CTkButton
from tkinter.font import BOLD
import util.generic as utl
from forms.master.design_master import DesignMaster

class MastelPanel(DesignMaster):
    
    
    
    def majorscreen(self):
        #configuracion inicial de Ventana de login
        self.windows = ctk.CTk()        
        self.windows.title('Master Panel')
        w, h = self.windows.winfo_screenwidth(), self.windows.winfo_screenheight()
        self.windows.geometry("%dx%d+0+0" % (w, h))
        self.windows.config(bg='#fcfcfc')
        self.windows.resizable(width=0, height=0)
        self.windows.columnconfigure(1, weight=1)
        self.windows.rowconfigure(1, weight=1)
        
        self.major = DesignMaster(self.windows)
        self.major.grid(row=0, column=0, sticky="NSEW")
        
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        
        
        self.windows.mainloop()
        