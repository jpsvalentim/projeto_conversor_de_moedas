print("oi")
import customtkinter

#CRIAR E CONFIGURAR JANELA
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


janela = customtkinter.CTk()
janela.geometry("500x500")

#CRIAR OS BOTTONS, TEXTOS E OUTROS ELEMENTOS
titulo = customtkinter.CTkLabel(janela, text = "Conversor de Moedas")#isso nao colaca direto na vizualização da janela, apenas em codigo
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem:")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino:")

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD","BRL","EUR","BTC"])
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values =["USD","BRL","EUR","BTC"])
def converter_moeda():
    print("converter moeda")
botao_converter = customtkinter.CTkButton(janela,text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

#ORGANIZADOR DE ELEMENTOS NA TELA
titulo.pack(padx=10, pady =10)
texto_moeda_origem.pack(padx=10, pady =10)
campo_moeda_origem.pack(padx=10, pady=10)
texto_moeda_destino.pack(padx =10, pady = 10)
campo_moeda_destino.pack(padx=10, pady=10)
botao_converter.pack(padx =10, pady=10)

lista_moedas.pack(padx =10, pady=10)

#LOOP 
janela.mainloop()




















