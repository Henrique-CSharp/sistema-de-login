# import tkinter
#
# window = tkinter.Tk()
# window.geometry('500x500')
#
# def acessar():
#     print("Fazer login")
#
# texto = tkinter.Label(text="LOGIN")
# texto.pack(padx=10, pady=10)
#
# button = tkinter.Button(window, text="login", command=acessar)
# button.pack(padx=10, pady=10)
#
#
#
# window.mainloop()

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.geometry('500x500')

def acessar():
     print("Fazer login")

texto = customtkinter.CTkLabel(window, text="LOGIN")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(window, placeholder_text="Digite seu e-mail")
email.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(window, placeholder_text="Digite sua senha", show="*")
email.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(window, text="Lembrar senha")
checkbox.pack(padx=5, pady=5)

button = customtkinter.CTkButton(window,text="login", command=acessar)
button.pack(padx=10, pady=10)

window.mainloop()