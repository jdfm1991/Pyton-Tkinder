from forms.register.design_register import DesignRegister
from persistence.repository.auth_login  import AuthUserRp
from persistence.models import AuthUser
from tkinter import ttk, messagebox
import util.encryp as en
import tkinter as tk 

class Register(DesignRegister):
    #Metodo de inicializacion
    def __init__(self):
        self.AuthRep = AuthUserRp()
        super().__init__()
        
    def register(self):
           if (self.isConfirmPassw()):
               user = AuthUser()
               user.userBD = self.user.get()
               #user.passw = self.passw.get()
               user_db: AuthUser = self.AuthRep.getUserByName(self.user.get())
               reg = self.isUserReg(user_db)
               if (reg == True):
                   user.passw = en.encrypted(self.passw.get())
                   self.AuthRep.insertUser(user)
                   messagebox.showinfo(message="Registro Exitoso", title="Mensaje")
                   self.windows.destroy()
                   
    def isConfirmPassw(self):
        status : bool = True
        if (self.passw.get() != self.confirm.get()):
            status = False
            messagebox.showerror(message="las contraseñas no coinciden", title="mensaje")
            self.passw.delete(0, tk.END)
            self.confirm.delete(0,tk.END)
        return status
            
    def isUserReg(self, user: AuthUser):
        status : bool = True
        if (user != None):
            status = False
            messagebox.showerror(message="Usuario ya existe", title="mensaje")
        return status