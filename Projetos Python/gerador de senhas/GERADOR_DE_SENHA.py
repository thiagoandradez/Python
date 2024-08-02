import pyperclip
import tkinter as tk
import random

#Catálogo:
MA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
MN = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NU = ['1','2','3','4','5','6','7','8','9','0']
SI = ['!', '@', '#', '$', '%', '?', '&', '*', '^', '.', ',', '~', '=', '+', '-']


senha_final = ''
qtd_caracteres = ''

#INTERFACE 

janela = tk.Tk()
#titulo da janela:
janela.title('Gerador de Senhas')

#tamanho da janela :
janela.geometry("550x300")
janela.resizable(width=False, height=False)

#texto de boas vindas :
texto_bv = tk.Label(janela, text='Bem vindo ao gerador de senhas ! ')
texto_bv.pack()

#Lógica 

def gerarSenha():
    
    qtd_caracteres_local = 0
    try:
        qtd_caracteres_local = int(qtd_caracteres.get())
    except:
        texto_senha_final['text'] = 'Digite um número positivo válido'
        texto_senha_final['fg'] = 'red'
        return

    if qtd_caracteres_local <= 4:
        texto_senha_final['text'] = 'Digite um número maior que 4'
        texto_senha_final['fg'] = 'red'
        return

    escolhas = []
    if maiuscula.get():
        escolhas.extend(MA)
    if minuscula.get():
        escolhas.extend(MN)
    if numero.get():
        escolhas.extend(NU)
    if especial.get():
        escolhas.extend(SI)

    global senha_final
    senha_final = ''.join(random.choices(escolhas, k=qtd_caracteres_local))

    texto_senha_final['text'] = f"Senha gerada: {senha_final}"
    texto_senha_final['fg'] = 'green'

def copiarSenha():
    pyperclip.copy(senha_final)


global senha_final1 
 

#senha final:
texto_senha_final = tk.Label(janela, text ='Senha gerada =')
texto_senha_final.pack()

qtd_caracteres = tk.StringVar()
maiuscula = tk.BooleanVar()
minuscula = tk.BooleanVar()
numero = tk.BooleanVar()
especial = tk.BooleanVar()

#caixa de texto:
texto_quantidade = tk.Label(janela,text= 'Qtnd de caracteres')
texto_quantidade.pack()
texto_caixa = tk.Entry(janela, bd =2, width = 20, textvariable=qtd_caracteres, justify='center')
texto_caixa.pack()

#checkbox :
checkbutton_maiuscula = tk.Checkbutton(janela, text="Maiúscula", variable=maiuscula, onvalue=True, offvalue=False)
checkbutton_maiuscula.pack()

checkbutton_minuscula = tk.Checkbutton(janela, text="Minúscula", variable=minuscula, onvalue=True, offvalue=False)
checkbutton_minuscula.pack()

checkbutton_numero = tk.Checkbutton(janela, text="Número", variable=numero, onvalue=True, offvalue=False)
checkbutton_numero.pack()

checkbutton_especial = tk.Checkbutton(janela, text="Especiais", variable=especial, onvalue=True, offvalue=False)
checkbutton_especial.pack()

#botoes :

botao_copiar = tk.Button(janela, text='Copiar Senha', command=copiarSenha)
botao_copiar.pack(pady=10)

botao_gerar = tk.Button(janela, text='Gerar Senha', command=gerarSenha)
botao_gerar.pack(pady=10)

janela.mainloop()