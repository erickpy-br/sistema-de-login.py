import customtkinter as ctk
from tkinter import*


class App(ctk.CTk):
     def __init__(self):
           super ().__init__() 
           self.configuracao_da_janela_inicial()
           self.tela_de_login()

   #Configurando a janela principal 
     def configuracao_da_janela_inicial(self):
        self.geometry("700x400")
        self.title("Sistema de Login")
        self.resizable(False,False) 
        ctk.set_appearance_mode("Dark")


     def tela_de_login(self):
        #Trabalhando com imagens 