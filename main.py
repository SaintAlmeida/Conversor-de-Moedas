import customtkinter as ctk

#Criando a Janela
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')
janela = ctk.CTk()
janela.geometry('500x500')

#Criar Botões
titulo = ctk.CTkLabel(janela, text = 'Conversor de Moedas', font=('arial',20))
texto_moeda_origem = ctk.CTkLabel(janela, text = 'Selecione a Moeda de Origem')
texto_moeda_destino = ctk.CTkLabel(janela, text = 'Selecione a Moeda de Destino')

campo_moeda_origem = ctk.CTkOptionMenu(janela, values = ['USD','BRL','EUR','BTC'])
campo_moeda_destino = ctk.CTkOptionMenu(janela, values = ['USD','BRL','EUR','BTC'])

def converter_moeda():
    print('Converter Moeda')
botao_converter = ctk.CTkButton(janela, text='Converter', command=converter_moeda)

lista_moedas = ctk.CTkScrollableFrame(janela)

moedas_disponiveis = ['R$ -  Real Brasileiro','BTC -  Bitcoin','R$ -  Dolár Americano']
for moeda in moedas_disponiveis:
    texto_moeda = ctk.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()




#Colocar Elementos na Janela
titulo.pack(padx=10,pady=10 )
texto_moeda_origem.pack(padx=10,pady=3)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10,pady=3)
campo_moeda_destino.pack(padx=10)
botao_converter.pack(padx=10,pady=10)
lista_moedas.pack(padx=10,pady=10)

#rodar a janela
janela.mainloop()