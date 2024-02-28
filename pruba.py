import tkinter as tk
import customtkinter as ctk


def insert_number(variable, entry):
    result = variable + entry
    return result


conjunt = ""


class MainWindow(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.config(bg="blue")
        ctk.CTkButton(self, text="1", command=lambda: insert_number(conjunt, "1")).grid(
            column=0, row=0, sticky="NSEW")
        ctk.CTkButton(self, text="2", command=lambda: insert_number(conjunt, "2")).grid(
            column=1, row=0, sticky="NSEW")
        ctk.CTkButton(self, text="3", command=lambda: insert_number(conjunt, "3")).grid(
            column=2, row=0, sticky="NSEW")
        ctk.CTkButton(self, text="4", command=lambda: insert_number(conjunt, "4")).grid(
            column=0, row=1, sticky="NSEW")
        ctk.CTkButton(self, text="5", command=lambda: insert_number(conjunt, "5")).grid(
            column=1, row=1, sticky="NSEW")
        ctk.CTkButton(self, text="6", command=lambda: insert_number(conjunt, "6")).grid(
            column=2, row=1, sticky="NSEW")
        ctk.CTkButton(self, text="7", command=lambda: insert_number(conjunt, "7")).grid(
            column=0, row=2, sticky="NSEW")
        ctk.CTkButton(self, text="8", command=lambda: insert_number(conjunt, "8")).grid(
            column=1, row=2, sticky="NSEW")
        ctk.CTkButton(self, text="9", command=lambda: insert_number(conjunt, "9")).grid(
            column=2, row=2, sticky="NSEW")
        ctk.CTkButton(self, text="0",  command=lambda: insert_number(conjunt, "0")).grid(
            column=1, row=3, sticky="NSEW")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)


def main():
    root = ctk.CTk()
    root.title("Calculadora")

    buttons_frame = MainWindow(root)
    buttons_frame.grid(row=0, column=0, sticky="NSEW")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)


    root.mainloop()


if __name__ == "__main__":
    main()