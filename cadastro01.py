import tkinter as tk 
from tkinter import ttk 
import datetime

lista_tipos =["Galão","Saco","Metro","Caixa","Unidade"]

janela = tk.Tk()



# titulo da janela

janela.title('Cadastro de Materiais')
#Descrição do material
label_descricao = tk.Label(text="Descrição do Material")
label_descricao.grid(row=1, column=0, padx=20, sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, sticky='nswe', columnspan=4)

label_tipo_unidade = tk.Label(text="Entre com a unidade de medida")
label_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
#Tipo do material
comboboox_tipo = ttk.Combobox(values=lista_tipos)
comboboox_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)
#Quantidade
label_quantidade = tk.Label(text="Entre com a Quantidade")
label_quantidade.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

label_quantidade = tk.Entry()
label_quantidade.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_criar_codigo = tk.Button(text="Criar Código")
botao_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

janela.mainloop()
