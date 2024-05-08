import tkinter
import tkinter.messagebox
from typing import Tuple
import customtkinter
import constantes as const

class telaPrincipal(customtkinter.CTk):

    _larguraTela = 0
    _alturaTela  = 0
    _padxPadrao  = 30 

    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.resizable(False,False)
        self.geometry("800x600")
        self.title("Boot HS Consórcios - " + const.VERSAO)
        self.iconbitmap('arquivos\web_tasks_clipboard_icon_262490.ico')
        self.build()

    def build(self):
        self._larguraTela = self.winfo_screenwidth()
        self._alturaTela  = self.winfo_screenheight()
            
        frame = customtkinter.CTkFrame(master= self,
                                       width= self._larguraTela,
                                       height= self._alturaTela)
        frame.pack(anchor = 'center')
        
        tabview = customtkinter.CTkTabview(master=frame,
                                           width= self._larguraTela,
                                           height= self._alturaTela) 
        tabview.pack(anchor = 'center')

        tabview.add("Processo")  
        tabview.add("Informações") 

        tabview.set("Processo")  

        labelLogin = customtkinter.CTkLabel(
            master = tabview.tab("Processo"),
            text= 'Login do site')

        labelLogin.pack(padx = self._padxPadrao,pady = 0,anchor= 'sw')

        campoLogin = customtkinter.CTkEntry(
            tabview.tab("Processo"))

        campoLogin.pack(padx = self._padxPadrao,pady = 0,anchor= 'sw')

        labelSenha = customtkinter.CTkLabel(
            master = tabview.tab("Processo"))

        labelSenha.pack(padx = self._padxPadrao,pady = 0,anchor= 'sw')

        campoSenha = customtkinter.CTkEntry(
            tabview.tab("Processo"))

        campoSenha.pack(padx = self._padxPadrao,pady = 0,anchor= 'sw')

        button = customtkinter.CTkButton(
            master= tabview.tab("Processo"),
            text= 'Salvar informações')

        button.pack(padx = self._padxPadrao,pady = 5,anchor= 'sw')