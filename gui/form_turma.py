from tkinter import *
from tkinter import ttk
from entidades.turma import *
from gui.mensagem import apresentaDialogo
from gui.util import *

def turmas_incluir(root):
	frame = Frame()
	codigoLabel = Label(frame, text="Código:", underline=0)
	codigoEntry = Entry(frame, textvariable="")
	codigoEntry.focus_set()
	
	def insere():
		codigo = codigoEntry.get().strip()
		retorno = insere_turma(codigo.upper())
		if retorno == 1:
			apresentaDialogo('Turma já cadastrada','Erro')
		elif retorno == 2:
			apresentaDialogo('Favor preencher os campos','Erro')
		codigoEntry.delete(0,END)
		codigoEntry.focus_set()

	okButton = Button(frame, text="Inserir", command=insere)
	codigoLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
	codigoEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	okButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : configura_enter(a, insere))    # parametro de ponteiro para função

def turmas_consultar(root):
	frame = Frame()
	codigoLabel = Label(frame, text="Código:", underline=0)
	codigoEntry = Entry(frame, textvariable="")
	codigoEntry.focus_set()
	codigo_consultado = StringVar()
	codigoLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
	codigoEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	respostaCodigoLabel = Label(frame, text="Código:", underline=0)
	respostaCodigoValor = Label(frame, textvariable=codigo_consultado)
	
	def consulta():
		codigo = codigoEntry.get().strip()
		retorno = consulta_turma(codigo)
		if retorno == None:			
			apresentaDialogo('Turma não encontrada','Erro')
			codigoEntry.delete(0,END)			
			codigoEntry.focus_set()
			respostaCodigoLabel.grid_remove()
			respostaCodigoValor.grid_remove()
		else:
			codigo_consultado.set(retorno['codigo'])
			respostaCodigoLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
			respostaCodigoValor.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			
	consultaButton = Button(frame, text="Consultar", command=consulta)
	consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : configura_enter(a,consulta))	

def turmas_excluir(root):
	frame = Frame()
	codigoLabel = Label(frame, text="Codigo:", underline=0)
	codigoEntry = Entry(frame, textvariable="")
	codigoEntry.focus_set()
	codigo_consultado = StringVar()
	codigoLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
	codigoEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	respostaCodigoLabel = Label(frame, text="Codigo:", underline=0)
	respostaCodigoValor = Label(frame, textvariable=codigo_consultado)
	
	def consulta():
		codigo = codigoEntry.get().strip()
		retorno = consulta_turma(codigo)
		if retorno == None:			
			apresentaDialogo('Turma não encontrada','Erro')
			codigoEntry.delete(0,END)			
			codigoEntry.focus_set()
			respostaCodigoLabel.grid_remove()
			respostaCodigoValor.grid_remove()
			excluiButton.grid_remove()
			root.bind('<Key>', lambda a : configura_enter(a,consulta))
		else:
			codigo_consultado.set(retorno['codigo'])
			respostaCodigoLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
			respostaCodigoValor.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			excluiButton.grid(row=3, column=3, sticky=EW, pady=3, padx=3)
			consultaButton.grid_remove()
			root.bind('<Key>', lambda a : configura_enter(a,exclui))
			
	def exclui():
		codigo = codigoEntry.get().strip()
		
		conf = apresentaDialogo("Deseja excluir a turma " + codigo,"Conf")
		if conf == 'yes':
			retorno = exclui_turma(codigo)
			codigoEntry.delete(0,END)
			codigoEntry.focus_set()
			respostaCodigoLabel.grid_remove()
			respostaCodigoValor.grid_remove()
			excluiButton.grid_remove()
			consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
			root.bind('<Key>', lambda a : configura_enter(a,consulta))
		else:
			codigoEntry.delete(0,END)			
			codigoEntry.focus_set()
			respostaCodigoLabel.grid_remove()
			respostaCodigoValor.grid_remove()
			excluiButton.grid_remove()	
			
	consultaButton = Button(frame, text="Consultar", command=consulta)
	excluiButton = Button(frame, text="Excluir", command=exclui)
	consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : configura_enter(a,consulta))	

def turmas_gerar_relacao(root):
	frame = Frame()
	
	relacaoTurmas = gera_relacao_turmas()

	tree = ttk.Treeview(frame, columns = (1), height = 5, show = "headings")
	tree.pack(side = 'left')

	tree.heading(1, text="Código")

	tree.column(1, width = 100)

	scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
	scroll.pack(side = 'right', fill = 'y')

	tree.configure(yscrollcommand=scroll.set)

	for turma in relacaoTurmas:
		tree.insert('', 'end', values = (turma['codigo']) )

	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : gera_relacao_turmas())
	
	def OnDoubleClick(event):
		print("selected items:")
		for item in tree.selection():
			valor = tree.item(item)['values']
			item_codigo = str(valor[0])
			print(item_codigo)

	tree.bind("<<TreeviewSelect>>", OnDoubleClick)	

