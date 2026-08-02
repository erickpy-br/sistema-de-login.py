import customtkinter as ctk
from PIL import Image
import os

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
                                size=(280, 280))
                           
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=1, column=0, padx=10,)
        

        #titulo da plataforma
        self.title = ctk.CTkLabel(self, text="Faça seu loguin ou cadastre-se\n na plataforma para acessar\n nossos serviços", font=("Century Gotic bold", 14))
        self.title.grid(row=0, column=0, pady=10, padx=10)

        #criando a frame do formulario de login

        self.frame_login = ctk.CTkFrame(self, width=350, height=350)
        self.frame_login.place(x=350, y=10)   

        #colocando widgets dentro do frame
        self.lb_title = ctk.CTkLabel(self.frame_login, text="Faça o seu login", 
        font=("Century Gothic bold", 22))
        self.lb_title.grid(row=0, column=0, padx=10,pady=10)

        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, 
        placeholder_text='Seu nome de usuário..', 
        font=("Century Gothic bold", 16), corner_radius=15)
        self.username_login_entry.grid(row=1, column=0, pady=10, padx=10)


        self.senha_login_entry = ctk.CTkEntry(self.frame_login, width=300, 
        placeholder_text='Seu nome de usuário..', 
        font=("Century Gothic bold", 16), corner_radius=15, show='*')
        self.senha_login_entry.grid(row=2, column=0, pady=10, padx=10)

        self.ver_senha = ctk.CTkCheckBox(self.frame_login, 
        text ="Clique para ver a senha", 
        font=("Century Gothic bold", 16), corner_radius=20)
        self.ver_senha.grid(row=3, column=0, pady=10, padx=10)

        self.btn_login = ctk.CTkButton(self.frame_login, width=300, 
        text = 'Fazer Login', 
        font=("Century Gothic bold", 16), corner_radius=15)
        self.btn_login.grid(row=4, column=0, pady=10, padx=10)


       
        self.sap = ctk.CTkLabel(self.frame_login, 
        text= "Se não tem conta, clique aqui para se cadastrar.",
        font=("Century Gothic", 10))
        self.sap.grid(row=5, column=0, pady=10, padx=10)

        self.btn_cadastro = ctk.CTkButton(self.frame_login, width=300, fg_color= 'green', 
        text = 'Fazer Cadastro', 
        font=("Century Gothic bold", 16), corner_radius=15, command = self.tela_de_cadastro)
        self.btn_cadastro.grid(row=4, column=0, pady=10, padx=10)


     def tela_de_cadastro(self):
         #Remover o formulário de login
         self.frame_login.place_forget()









                                                                                                                      

      
      














if __name__=="__main__":
     app = App()
     app.mainloop()
