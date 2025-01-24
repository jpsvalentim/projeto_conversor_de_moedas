print("oi")
import customtkinter
from PEGAR_MOEDA import nomes_moedas, conversoes_disponiveis;


#CRIAR E CONFIGURAR JANELA
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


janela = customtkinter.CTk()
janela.geometry("500x500")

dic_conversoes_disponiveis = conversoes_disponiveis()

#CRIAR OS BOTTONS, TEXTOS E OUTROS ELEMENTOS
titulo = customtkinter.CTkLabel(janela, text = "CONVERSOR DE MOEDAS", font=("Arial",30))#isso nao colaca direto na vizualização da janela, apenas em codigo
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem:")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino:")

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set (lista_moedas_destino[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values = list(dic_conversoes_disponiveis.keys()),command=carregar_moedas_destino)
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values =["Selecione uma moeda de origem"])

def converter_moeda():
    print("converter moeda")
botao_converter = customtkinter.CTkButton(janela,text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = nomes_moedas()
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    texto_moeda.pack()


#ORGANIZADOR DE ELEMENTOS NA TELA
titulo.pack(padx=10, pady =10)
texto_moeda_origem.pack(padx=10, pady =10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx =10, pady = 10)
campo_moeda_destino.pack(padx=10)
botao_converter.pack(padx =10, pady=10)

lista_moedas.pack(padx =10, pady=10)

#LOOP 
janela.mainloop()




















