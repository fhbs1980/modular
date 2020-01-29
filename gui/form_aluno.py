from tkinter import *
from entidades.aluno import *
from gui.mensagem import apresentaDialogo
from gui.util import *

def alunos_incluir(root):
	frame = Frame()
	matriculaLabel = Label(frame, text="Matricula:", underline=0)
	matriculaEntry = Entry(frame, textvariable="")
	matriculaEntry.focus_set()
	
	nomeLabel = Label(frame, text="Nome:", underline=0)
	nomeEntry = Entry(frame, textvariable="")
	
	def insere():
		
		matricula = matriculaEntry.get().strip()
		retorno = insere_aluno(matricula, nomeEntry.get().title())
		if retorno == 1:
			apresentaDialogo('Matrícula já cadastrada','Erro')
		elif retorno == 2:
			apresentaDialogo('Favor preencher os campos','Erro')
		
		matriculaEntry.delete(0,END)
		nomeEntry.delete(0,END)
		matriculaEntry.focus_set()
		
	
	
	okButton = Button(frame, text="Inserir", command=insere)
	matriculaLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
	matriculaEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	nomeLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
	nomeEntry.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	okButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : configura_enter(a, insere))    # parametro de ponteiro para função

def alunos_consultar(root):
	frame = Frame()
	matriculaLabel = Label(frame, text="Matricula:", underline=0)
	matriculaEntry = Entry(frame, textvariable="")
	matriculaEntry.focus_set()
	
	textoLabelRespostaMatricula = StringVar()
	textoValorRespostaMatricula = StringVar()
	textoLabelRespostaNome = StringVar()
	textoValorRespostaNome = StringVar()
	
	textoLabelRespostaMatricula.set("")
	textoValorRespostaMatricula.set("")
	textoLabelRespostaNome.set("")
	textoValorRespostaNome.set("")
	
	def consulta():
		
		matricula = matriculaEntry.get().strip()
		retorno = consulta_aluno(matricula)
		if retorno == None:
			textoLabelRespostaMatricula.set("")
			textoValorRespostaMatricula.set("")
			textoLabelRespostaNome.set("")
			textoValorRespostaNome.set("")
			
			apresentaDialogo('Matrícula não encontrada','Erro')
			matriculaEntry.delete(0,END)			
			matriculaEntry.focus_set()
		else:
			textoLabelRespostaMatricula.set("Matricula:")
			textoValorRespostaMatricula.set(retorno['matricula'])
			textoLabelRespostaNome.set("Nome:")
			textoValorRespostaNome.set(retorno['nome'])
	
	consultaButton = Button(frame, text="Consultar", command=consulta)
	matriculaLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
	matriculaEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
	
	respostaMatriculaLabel = Label(frame, textvariable=textoLabelRespostaMatricula, underline=0)
	respostaMatriculaValor = Label(frame, textvariable=textoValorRespostaMatricula)
	respostaMatriculaLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
	respostaMatriculaValor.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	
	respostaNomeLabel = Label(frame, textvariable=textoLabelRespostaNome, underline=0)
	respostaNomeValor = Label(frame, textvariable=textoValorRespostaNome)
	respostaNomeLabel.grid(row=2, column=0, sticky=W, pady=3,padx=3)
	respostaNomeValor.grid(row=2, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : configura_enter(a,consulta))
	
def alunos_alterar(root):
	frame = Frame()
	matriculaLabel = Label(frame, text="Matricula:", underline=0)
	matriculaEntry = Entry(frame, textvariable="")
	matriculaEntry.focus_set()
	
	matricula_consultada = StringVar()
	nome_consultado = StringVar()
	
	
	matriculaLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
	matriculaEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	
	
	respostaMatriculaLabel = Label(frame, text="Matricula:", underline=0)
	respostaMatriculaValor = Label(frame, textvariable=matricula_consultada)
#	respostaMatriculaLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
#	respostaMatriculaValor.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	
	respostaNomeLabel = Label(frame, text="Nome:", underline=0)
	respostaNomeValor = Entry(frame, textvariable=nome_consultado)
#	respostaNomeLabel.grid(row=2, column=0, sticky=W, pady=3,padx=3)
#	respostaNomeValor.grid(row=2, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	
	def consulta():
		
		matricula = matriculaEntry.get().strip()
		retorno = consulta_aluno(matricula)
		if retorno == None:			
			apresentaDialogo('Matrícula não encontrada','Erro')
			matriculaEntry.delete(0,END)			
			matriculaEntry.focus_set()
			respostaMatriculaLabel.grid_remove()
			respostaMatriculaValor.grid_remove()
			respostaNomeLabel.grid_remove()
			respostaNomeValor.grid_remove()
			alteraButton.grid_remove()
		else:
			matricula_consultada.set(retorno['matricula'])
			nome_consultado.set(retorno['nome'])
#			respostaMatriculaLabel = Label(frame, text="Matricula:", underline=0)
#			respostaMatriculaValor = Label(frame, textvariable=matricula_consultada)
			respostaMatriculaLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
			respostaMatriculaValor.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
#			respostaNomeLabel = Label(frame, text="Nome:", underline=0)
#			respostaNomeValor = Entry(frame, textvariable=nome_consultado)
			respostaNomeLabel.grid(row=2, column=0, sticky=W, pady=3,padx=3)
			respostaNomeValor.grid(row=2, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			alteraButton.grid(row=3, column=3, sticky=EW, pady=3, padx=3)
	
	consultaButton = Button(frame, text="Consultar", command=consulta)
	alteraButton = Button(frame, text="Alterar", command=consulta)
	consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)

	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : configura_enter(a,consulta))
