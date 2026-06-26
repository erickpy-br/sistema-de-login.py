import customtkinter as ctk
from PIL import Image
import os
print("Pasta atual do script:", os.path.dirname(__file__))
print("Arquivos encontrados:", os.listdir(os.path.dirname(__file__)))


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

        self.img = ctk.CTkImage(light_image=Image.open("login-img.png"), 
                                dark_image=Image.open("login-img.png"), 
                                size=(250, 250))
                           
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=1, column=0, padx=10, pady=20)

        self.title = ctk.CTkLabel(self, text="Faça seu loguin ou cadastre-se na plataforma", font=("Century Gotic bold", 14))
        self.title.grid(row=0, column=0, pady=0)


if __name__=="__main__":
     App = App()
     App.mainloop()
