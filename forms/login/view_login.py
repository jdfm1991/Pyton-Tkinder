import tkinter as tk 
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.login.design_login import DesignLogin
from forms.master.view_master import MastelPanel
from forms.register.view_register import Register
from persistence.models import AuthUser
from persistence.repository.auth_login  import AuthUserRp
import util.encryp as en

class login(DesignLogin):
    
    #Metodo de inicializacion
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
           messagebox.showerror(message="Clave Errada", title="Mensaje") 
           
    
   