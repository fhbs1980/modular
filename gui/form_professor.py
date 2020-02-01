from tkinter import *
from tkinter import ttk
from entidades.professor import *
from gui.mensagem import apresentaDialogo
from gui.util import *

def professores_incluir(root):
	frame = Frame()
	matriculaLabel = Label(frame, text="Matricula:", underline=0)
	matriculaEntry = Entry(frame, textvariable="")
	matriculaEntry.focus_set()
	nomeLabel = Label(frame, text="Nome:", underline=0)
	nomeEntry = Entry(frame, textvariable="")
	
	def insere():
		matricula = matriculaEntry.get().strip()
		retorno = insere_professor(matricula, nomeEntry.get().title())
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

def professores_consultar(root):
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
	respostaNomeLabel = Label(frame, text="Nome:", underline=0)
	respostaNomeValor = Label(frame, textvariable=nome_consultado)
	
	def consulta():
		matricula = matriculaEntry.get().strip()
		retorno = consulta_professor(matricula)
		if retorno == None:			
			apresentaDialogo('Matrícula não encontrada','Erro')
			matriculaEntry.delete(0,END)			
			matriculaEntry.focus_set()
			respostaMatriculaLabel.grid_remove()
			respostaMatriculaValor.grid_remove()
			respostaNomeLabel.grid_remove()
			respostaNomeValor.grid_remove()
		else:
			matricula_consultada.set(retorno['matricula'])
			nome_consultado.set(retorno['nome'])
			respostaMatriculaLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
			respostaMatriculaValor.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			respostaNomeLabel.grid(row=2, column=0, sticky=W, pady=3,padx=3)
			respostaNomeValor.grid(row=2, column=1, columnspan=3, sticky=EW, pady=3, padx=3)		
			
	consultaButton = Button(frame, text="Consultar", command=consulta)
	consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : configura_enter(a,consulta))	
	
def professores_alterar(root):
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
	respostaNomeLabel = Label(frame, text="Nome:", underline=0)
	respostaNomeValor = Entry(frame, textvariable=nome_consultado)
	
	def consulta():
		matricula = matriculaEntry.get().strip()
		retorno = consulta_professor(matricula)
		if retorno == None:			
			apresentaDialogo('Matrícula não encontrada','Erro')
			matriculaEntry.delete(0,END)			
			matriculaEntry.focus_set()
			respostaMatriculaLabel.grid_remove()
			respostaMatriculaValor.grid_remove()
			respostaNomeLabel.grid_remove()
			respostaNomeValor.grid_remove()
			alteraButton.grid_remove()
			root.bind('<Key>', lambda a : configura_enter(a,consulta))
		else:
			matricula_consultada.set(retorno['matricula'])
			nome_consultado.set(retorno['nome'])
			respostaMatriculaLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
			respostaMatriculaValor.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			respostaNomeLabel.grid(row=2, column=0, sticky=W, pady=3,padx=3)
			respostaNomeValor.grid(row=2, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			alteraButton.grid(row=3, column=3, sticky=EW, pady=3, padx=3)
			consultaButton.grid_remove()
			root.bind('<Key>', lambda a : configura_enter(a,altera))
			
	def altera():
		matricula = matriculaEntry.get().strip()
		retorno = altera_professor(matricula,'nome',respostaNomeValor.get().strip())
		matriculaEntry.delete(0,END)			
		matriculaEntry.focus_set()
		respostaMatriculaLabel.grid_remove()
		respostaMatriculaValor.grid_remove()
		respostaNomeLabel.grid_remove()
		respostaNomeValor.grid_remove()
		alteraButton.grid_remove()
		consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
		root.bind('<Key>', lambda a : configura_enter(a,consulta))
		
	consultaButton = Button(frame, text="Consultar", command=consulta)
	alteraButton = Button(frame, text="Alterar", command=altera)
	consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : configura_enter(a,consulta))

def professores_excluir(root):
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
	respostaNomeLabel = Label(frame, text="Nome:", underline=0)
	respostaNomeValor = Label(frame, textvariable=nome_consultado)
	
	def consulta():
		matricula = matriculaEntry.get().strip()
		retorno = consulta_professor(matricula)
		if retorno == None:			
			apresentaDialogo('Matrícula não encontrada','Erro')
			matriculaEntry.delete(0,END)			
			matriculaEntry.focus_set()
			respostaMatriculaLabel.grid_remove()
			respostaMatriculaValor.grid_remove()
			respostaNomeLabel.grid_remove()
			respostaNomeValor.grid_remove()
			excluiButton.grid_remove()
			root.bind('<Key>', lambda a : configura_enter(a,consulta))
		else:
			matricula_consultada.set(retorno['matricula'])
			nome_consultado.set(retorno['nome'])
			respostaMatriculaLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
			respostaMatriculaValor.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			respostaNomeLabel.grid(row=2, column=0, sticky=W, pady=3,padx=3)
			respostaNomeValor.grid(row=2, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			excluiButton.grid(row=3, column=3, sticky=EW, pady=3, padx=3)
			consultaButton.grid_remove()
			root.bind('<Key>', lambda a : configura_enter(a,exclui))
			
	def exclui():
		matricula = matriculaEntry.get().strip()
		
		conf = apresentaDialogo("Deseja excluir o professor de matrícula " + matricula,"Conf")
		if conf == 'yes':
			retorno = exclui_professor(matricula)
			matriculaEntry.delete(0,END)
			matriculaEntry.focus_set()
			respostaMatriculaLabel.grid_remove()
			respostaMatriculaValor.grid_remove()
			respostaNomeLabel.grid_remove()
			respostaNomeValor.grid_remove()
			excluiButton.grid_remove()
			consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
			root.bind('<Key>', lambda a : configura_enter(a,consulta))
		else:
			matriculaEntry.delete(0,END)			
			matriculaEntry.focus_set()
			respostaMatriculaLabel.grid_remove()
			respostaMatriculaValor.grid_remove()
			respostaNomeLabel.grid_remove()
			respostaNomeValor.grid_remove()
			excluiButton.grid_remove()	
			
	consultaButton = Button(frame, text="Consultar", command=consulta)
	excluiButton = Button(frame, text="Excluir", command=exclui)
	consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : configura_enter(a,consulta))	

def professores_gerar_relacao(root):
	frame = Frame()
	
	relacaoProfessores = gera_relacao_professores()

	tree = ttk.Treeview(frame, columns = (1,2), height = 5, show = "headings")
	tree.pack(side = 'left')

	tree.heading(1, text="Matrícula")
	tree.heading(2, text="Nome")

	tree.column(1, width = 100)
	tree.column(2, width = 100)

	scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
	scroll.pack(side = 'right', fill = 'y')

	tree.configure(yscrollcommand=scroll.set)

	for professor in relacaoProfessores:
		tree.insert('', 'end', values = (professor['matricula'], professor['nome']) )

	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : gera_relacao_professores())
	
	def OnDoubleClick(event):
		print("selected items:")
		for item in tree.selection():
			valor = tree.item(item)['values']
			item_matricula = str(valor[0])
			item_nome = valor[1]
			print(item_matricula + " - " + item_nome)

	tree.bind("<<TreeviewSelect>>", OnDoubleClick)	
