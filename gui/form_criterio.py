from tkinter import *
from tkinter import ttk
from entidades.criterio_aprovacao import *
from gui.mensagem import apresentaDialogo
from gui.util import *

def criterios_incluir(root):
	frame = Frame()
	codigoLabel = Label(frame, text="Código:", underline=0)
	codigoEntry = Entry(frame, textvariable="")
	codigoEntry.focus_set()
	formulaLabel = Label(frame, text="Fórmula:", underline=0)
	formulaEntry = Entry(frame, textvariable="")
	
	def insere():
		codigo = codigoEntry.get().strip()
		retorno = insere_criterio(codigo, formulaEntry.get().title())
		if retorno == 1:
			apresentaDialogo('Critério com código já cadastrada','Erro')
		elif retorno == 2:
			apresentaDialogo('Favor preencher os campos','Erro')
		codigoEntry.delete(0,END)
		formulaEntry.delete(0,END)
		codigoEntry.focus_set()

	okButton = Button(frame, text="Inserir", command=insere)
	codigoLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
	codigoEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	formulaLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
	formulaEntry.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	okButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : configura_enter(a, insere))    # parametro de ponteiro para função

def criterios_consultar(root):
	frame = Frame()
	codigoLabel = Label(frame, text="Código:", underline=0)
	codigoEntry = Entry(frame, textvariable="")
	codigoEntry.focus_set()
	codigo_consultado = StringVar()
	formula_consultada = StringVar()
	codigoLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
	codigoEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	respostaCodigoLabel = Label(frame, text="Código:", underline=0)
	respostaCodigoValor = Label(frame, textvariable=codigo_consultado)
	respostaFormulaLabel = Label(frame, text="Fórmula:", underline=0)
	respostaFormulaValor = Label(frame, textvariable=formula_consultada)
	
	def consulta():
		codigo = codigoEntry.get().strip()
		retorno = consulta_criterio(codigo)
		if retorno == None:			
			apresentaDialogo('Critério com código não encontrada','Erro')
			codigoEntry.delete(0,END)			
			codigoEntry.focus_set()
			respostaCodigoLabel.grid_remove()
			respostaCodigoValor.grid_remove()
			respostaFormulaLabel.grid_remove()
			respostaFormulaValor.grid_remove()
		else:
			codigo_consultado.set(retorno['codigo'])
			formula_consultada.set(retorno['formula'])
			respostaCodigoLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
			respostaCodigoValor.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			respostaFormulaLabel.grid(row=2, column=0, sticky=W, pady=3,padx=3)
			respostaFormulaValor.grid(row=2, column=1, columnspan=3, sticky=EW, pady=3, padx=3)		
			
	consultaButton = Button(frame, text="Consultar", command=consulta)
	consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : configura_enter(a,consulta))	
	
def criterios_alterar(root):
	frame = Frame()
	codigoLabel = Label(frame, text="Matricula:", underline=0)
	codigoEntry = Entry(frame, textvariable="")
	codigoEntry.focus_set()
	codigo_consultado = StringVar()
	formula_consultada = StringVar()
	codigoLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
	codigoEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	respostaCodigoLabel = Label(frame, text="Código:", underline=0)
	respostaCodigoValor = Label(frame, textvariable=codigo_consultado)
	respostaFormulaLabel = Label(frame, text="Fórmula:", underline=0)
	respostaFormulaValor = Entry(frame, textvariable=formula_consultada)
	
	def consulta():
		codigo = codigoEntry.get().strip()
		retorno = consulta_criterio(codigo)
		if retorno == None:			
			apresentaDialogo('Código não encontrado','Erro')
			codigoEntry.delete(0,END)			
			codigoEntry.focus_set()
			respostaCodigoLabel.grid_remove()
			respostaCodigoValor.grid_remove()
			respostaFormulaLabel.grid_remove()
			respostaFormulaValor.grid_remove()
			alteraButton.grid_remove()
			root.bind('<Key>', lambda a : configura_enter(a,consulta))
		else:
			codigo_consultado.set(retorno['codigo'])
			formula_consultada.set(retorno['formula'])
			respostaCodigoLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
			respostaCodigoValor.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			respostaFormulaLabel.grid(row=2, column=0, sticky=W, pady=3,padx=3)
			respostaFormulaValor.grid(row=2, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			alteraButton.grid(row=3, column=3, sticky=EW, pady=3, padx=3)
			consultaButton.grid_remove()
			root.bind('<Key>', lambda a : configura_enter(a,altera))
			
	def altera():
		codigo = codigoEntry.get().strip()
		retorno = altera_criterio(codigo,'formula',respostaFormulaValor.get().strip())
		codigoEntry.delete(0,END)			
		codigoEntry.focus_set()
		respostaCodigoLabel.grid_remove()
		respostaCodigoValor.grid_remove()
		respostaFormulaLabel.grid_remove()
		respostaFormulaValor.grid_remove()
		alteraButton.grid_remove()
		consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
		root.bind('<Key>', lambda a : configura_enter(a,consulta))
		
	consultaButton = Button(frame, text="Consultar", command=consulta)
	alteraButton = Button(frame, text="Alterar", command=altera)
	consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : configura_enter(a,consulta))

def criterios_excluir(root):
	frame = Frame()
	codigoLabel = Label(frame, text="Codigo:", underline=0)
	codigoEntry = Entry(frame, textvariable="")
	codigoEntry.focus_set()
	codigo_consultado = StringVar()
	formula_consultada = StringVar()
	codigoLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
	codigoEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	respostaCodigoLabel = Label(frame, text="Codigo:", underline=0)
	respostaCodigoValor = Label(frame, textvariable=codigo_consultado)
	respostaFormulaLabel = Label(frame, text="Fórmula:", underline=0)
	respostaFormulaValor = Label(frame, textvariable=formula_consultada)
	
	def consulta():
		codigo = codigoEntry.get().strip()
		retorno = consulta_criterio(codigo)
		if retorno == None:			
			apresentaDialogo('Código não encontrado','Erro')
			codigoEntry.delete(0,END)			
			codigoEntry.focus_set()
			respostaCodigoLabel.grid_remove()
			respostaCodigoValor.grid_remove()
			respostaFormulaLabel.grid_remove()
			respostaFormulaValor.grid_remove()
			excluiButton.grid_remove()
			root.bind('<Key>', lambda a : configura_enter(a,consulta))
		else:
			codigo_consultado.set(retorno['codigo'])
			formula_consultada.set(retorno['formula'])
			respostaCodigoLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
			respostaCodigoValor.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			respostaFormulaLabel.grid(row=2, column=0, sticky=W, pady=3,padx=3)
			respostaFormulaValor.grid(row=2, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			excluiButton.grid(row=3, column=3, sticky=EW, pady=3, padx=3)
			consultaButton.grid_remove()
			root.bind('<Key>', lambda a : configura_enter(a,exclui))
			
	def exclui():
		codigo = codigoEntry.get().strip()
		
		conf = apresentaDialogo("Deseja excluir o critério " + codigo,"Conf")
		if conf == 'yes':
			retorno = exclui_criterio(codigo)
			codigoEntry.delete(0,END)
			codigoEntry.focus_set()
			respostaCodigoLabel.grid_remove()
			respostaCodigoValor.grid_remove()
			respostaFormulaLabel.grid_remove()
			respostaFormulaValor.grid_remove()
			excluiButton.grid_remove()
			consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
			root.bind('<Key>', lambda a : configura_enter(a,consulta))
		else:
			codigoEntry.delete(0,END)			
			codigoEntry.focus_set()
			respostaCodigoLabel.grid_remove()
			respostaCodigoValor.grid_remove()
			respostaFormulaLabel.grid_remove()
			respostaFormulaValor.grid_remove()
			excluiButton.grid_remove()	
			
	consultaButton = Button(frame, text="Consultar", command=consulta)
	excluiButton = Button(frame, text="Excluir", command=exclui)
	consultaButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : configura_enter(a,consulta))	

def criterios_gerar_relacao(root):
	frame = Frame()
	
	relacaoCriterios = gera_relacao_criterios()

	tree = ttk.Treeview(frame, columns = (1,2), height = 5, show = "headings")
	tree.pack(side = 'left')

	tree.heading(1, text="Código")
	tree.heading(2, text="Fórmula")

	tree.column(1, width = 100)
	tree.column(2, width = 100)

	scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
	scroll.pack(side = 'right', fill = 'y')

	tree.configure(yscrollcommand=scroll.set)

	for criterio in relacaoCriterios:
		tree.insert('', 'end', values = (criterio['codigo'], criterio['formula']) )

	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : gera_relacao_criterios())
	
	def OnDoubleClick(event):
		print("selected items:")
		for item in tree.selection():
			valor = tree.item(item)['values']
			item_codigo = str(valor[0])
			item_formula = valor[1]
			print(item_codigo + " - " + item_formula)

	tree.bind("<<TreeviewSelect>>", OnDoubleClick)	

