from tkinter import *

janela = Tk()
janela.title('Aprovador de empréstimo')
janela.geometry("550x350")
janela.resizable(width=False, height=False)
texto_bv = Label(janela, text='Bem vindo ao aprovador de empréstimo ! ')
texto_bv.pack()

#variaveis :
prestacao = ''
valor = DoubleVar()
anos = IntVar()
salario = DoubleVar()


#definição:
def gerar():
    prestacao = valor.get() / (anos.get() * 12)
    minimo = salario.get() * 30 / 100
    if prestacao <= minimo:
        texto_bv['text'] = f"Empréstimo concedido! seus dados são aceitos para o empréstimo.\n A sua prestação será de R$ {prestacao:.2f} mensais"
        texto_bv['fg'] = 'green'
        
    else:
        texto_bv['text'] = f"Empréstimo negado! seus dados não são aceitos para o empréstimo, \n ele não pode execeder 30% do seu salário R$ {salario.get()}"
        texto_bv['fg'] = 'red'
       
    
   
   
#captação:
texto_valor_casa = Label(janela,text= 'Digite o valor da casa : ')
texto_valor_casa.pack()
texto_caixa_valor = Entry(janela, bd =2, width = 20, textvariable=valor, justify='center')
texto_caixa_valor.pack()

texto_valor_anos = Label(janela,text= 'Digite em quantos anos deseja pagar  : ')
texto_valor_anos.pack()
texto_caixa_anos = Entry(janela, bd =2, width = 20, textvariable=anos, justify='center')
texto_caixa_anos.pack()

texto_valor_salario = Label(janela,text= 'Digite o seu salário  : ')
texto_valor_salario.pack()
texto_caixa_salario = Entry(janela, bd =2, width = 20, textvariable=salario, justify='center')
texto_caixa_salario.pack()

texto_bv = Label(janela, text=' A prestação mensal, não pode exceder \n 30% do salário ou então o \n empréstimo será negado.')
texto_bv.pack()


botao_gerar = Button(janela, text='Gerar', command=gerar)
botao_gerar.pack(pady=10)







janela.mainloop()