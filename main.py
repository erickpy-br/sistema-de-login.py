import customtkinter as ctk


class App(ctk.CTk):
     def __init__(self):
           super ().__init__() 
           self.configuracao_da_janela_inicial()

   #Configurando a janela principal 
     def configuracao_da_janela_inicial(self):
        self.geometry("700x400")
        self.title("Sistema de Login")
        self.resizable(False,False) 



if __name__=="__main__":
    app = App()
    app.mainloop()  