from tkinter import *
from entidades.aluno import *


def alunos_incluir():
	frame = Frame()
	matriculaLabel = Label(frame, text="Matricula:", underline=0)
	matriculaEntry = Entry(frame, textvariable="")
	matriculaEntry.focus_set()
	
	nomeLabel = Label(frame, text="Nome:", underline=0)
	nomeEntry = Entry(frame, textvariable="")
	
	def insere():
		retorno = insere_aluno(matriculaEntry.get(), nomeEntry.get())
	
	
	okButton = Button(frame, text="Inserir", command=insere)
	cancelButton = Button(frame, text="Cancelar", command=frame.quit)
	matriculaLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
	matriculaEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	nomeLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
	nomeEntry.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	okButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
	cancelButton.grid(row=3, column=3, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
