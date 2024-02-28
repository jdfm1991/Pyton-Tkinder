import tkinter as tk 
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.design_master import DesignMaster

class MastelPanel(DesignMaster):
    
    #Metodo de inicializacion
    def __init__(self):
        super().__init__()
    
    def screenhome(self):
        self.page.select([self.frame_home])
    
    def getfile(self, event):
        self.current_item = self.data_view.focus()
        if not self.current_item:
            return
        self.data = self.data_view.item()
        self.name_erase = self.data['values'][0]
                
    def screendata(self):
        self.page.select([self.frame_data])
        self.frame_data.columnconfigure(0, weight=1)
        self.frame_data.columnconfigure(1, weight=1)
        self.frame_data.rowconfigure(2, weight=1)
        self.view_d.columnconfigure(0, weight=1)
        self.view_d.rowconfigure(0, weight=1)
        
    def screensetting(self):
        self.page.select([self.frame_conf])
        self.frame_conf.columnconfigure(0, weight=1)
        self.frame_conf.columnconfigure(1, weight=1)
        self.frame_conf.columnconfigure(2, weight=1)
        self.frame_conf.rowconfigure(2, weight=1)
        self.view_c.columnconfigure(0, weight=1)
        self.view_c.rowconfigure(0, weight=1)
        
              
    
    def sidebar(self):
        if self.menu is True:
            for i in range(50,170,10):
                self.frame_menu.config(width= i)
                self.frame_init.config(width= i)
                self.frame_menu.update()
                self.click_init =self.btn_clos.grid_forget()
                if self.click_init is None:
                     self.btn_init.grid(column=0, row=0, padx =10, pady=10)
                     self.btn_init.grid_propagate(0)
                     self.btn_init.config(width=i)
                     self.screenhome()
            self.menu = False
        else:
            for i in range(170,50,-10):
                self.frame_menu.config(width= i)
                self.frame_init.config(width= i)
                self.frame_menu.update()
                self.click_init =self.btn_init.grid_forget()
                if self.click_init is None:
                    self.btn_clos.grid(column=0, row=0, padx =10, pady=10)
                    self.btn_clos.grid_propagate(0)
                    self.btn_clos.config(width=i)
                    self.screenhome()
            self.menu = True
        

    
    ''' #Metodo de inicializacion
    def __init__(self):
        self.AuthRep = AuthUserRp()
        super().__init__()
    
    #Metodo para verifica usuario
    def verify(self):
        user_db: AuthUser = self.AuthRep.getUserByName(self.user.get())
        if (self.isUSer(user_db)):
              self.isPass(self.passw.get(),user_db)
              
    #Metodo para Crear usuario usuario
    def create(self):
        Register().mainloop()
            
    #Metodo de verificacion de usuario
    def isUSer(self, user:AuthUser):
        status : bool = True
        if (user == None):
            status = False
            messagebox.showerror(message="usuario no registrado", title="Mensaje")
        return status
    
    #Metodo de verificacion de clave
    def isPass(self, passw:str, user:AuthUser):
        b_passw = en.decrypt(user.passw)
        if (passw == b_passw):
            self.windows.destroy()
            MastelPanel()
        else:
           messagebox.showerror(message="Clave Errada", title="Mensaje") '''
           
    
   