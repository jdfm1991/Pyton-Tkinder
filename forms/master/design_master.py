import customtkinter as ctk
import tkinter as tk 
from tkinter import ttk, PhotoImage
from customtkinter import CTk, CTkFrame, CTkButton
from tkinter.font import BOLD
import util.generic as utl

opt = ""

class DesignMaster(tk.Frame):
    
    def options(variable, entry):
        result = variable + entry
        return result
    
    # funcion para crear ventana    
    def __init__(self,*args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
                
        self.frame_opt1 = ctk.CTkButton(master=self, text="opcion 1", command=lambda:self.options(opt, "opcion 1"))
        self.frame_opt1.grid(column=0, row=0, sticky="NSEW")
        self.frame_opt2 = ctk.CTkButton(master=self, text="opcion 2", command=lambda:self.options(opt, "opcion 2"))
        self.frame_opt2.grid(column=1, row=0, sticky="NSEW")
        self.frame_opt3 = ctk.CTkButton(master=self, text="opcion 3", command=lambda:self.options(opt, "opcion 3"))
        self.frame_opt3.grid(column=2, row=0, sticky="NSEW")
        self.frame_opt4 = ctk.CTkButton(master=self, text="opcion 4", command=lambda:self.options(opt, "opcion 4"))
        self.frame_opt4.grid(column=0, row=1, sticky="NSEW")
        self.frame_opt5 = ctk.CTkButton(master=self, text="opcion 5", command=lambda:self.options(opt, "opcion 5"))
        self.frame_opt5.grid(column=1, row=1, sticky="NSEW")
        self.frame_opt6 = ctk.CTkButton(master=self, text="opcion 6", command=lambda:self.options(opt, "opcion 6"))
        self.frame_opt6.grid(column=2, row=1, sticky="NSEW")
        self.frame_opt7 = ctk.CTkButton(master=self, text="opcion 7", command=lambda:self.options(opt, "opcion 7"))
        self.frame_opt7.grid(column=0, row=2, sticky="NSEW")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
    