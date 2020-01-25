from tkinter import messagebox

def apresentaDialogo(mensagem, tipo, acao=''):

	if tipo == 'Erro':
		messagebox.showinfo("Erro",mensagem)
	elif tipo == 'Conf':
		pass

