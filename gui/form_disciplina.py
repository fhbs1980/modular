from tkinter import *
from tkinter import ttk
from entidades.criterio_aprovacao import *
from entidades.disciplina import *
from entidades.criterio_aprovacao import *
from gui.mensagem import apresentaDialogo
from gui.util import *

def disciplinas_incluir(root):
	frame = Frame()
	codigoLabel = Label(frame, text="Código:", underline=0)
	codigoEntry = Entry(frame, textvariable="")
	codigoEntry.focus_set()
	nomeLabel = Label(frame, text="Nome:", underline=0)
	nomeEntry = Entry(frame, textvariable="")
	ementaLabel = Label(frame, text="Ementa:", underline=0)
	ementaEntry = Text(frame, height=10, width=50)
	
	criterioEscolhido = StringVar()
	
	relacaoCriterios = gera_relacao_criterios()

	treeCriterios = ttk.Treeview(frame, columns = (1,2), height = 5, show = "headings")
	#treeCriterios.pack(side = 'left')

	treeCriterios.heading(1, text="Código")
	treeCriterios.heading(2, text="Fórmula")

	treeCriterios.column(1, width = 100)
	treeCriterios.column(2, width = 100)

	scrollCriterios = ttk.Scrollbar(frame, orient="vertical", command=treeCriterios.yview)
#	scrollCriterios.grid(side = 'right', fill = 'y')

	treeCriterios.configure(yscrollcommand=scrollCriterios.set)

	for criterio in relacaoCriterios:
		treeCriterios.insert('', 'end', values = (criterio['codigo'], criterio['formula']) )
	
	def OnDoubleClick(event):
		for item in treeCriterios.selection():
			valor = treeCriterios.item(item)['values']
			criterioEscolhido.set(str(valor[0]))
	
	treeCriterios.bind("<<TreeviewSelect>>", OnDoubleClick)
	
	def insere():
		codigo = codigoEntry.get().strip()
		retorno = insere_disciplina(codigo, nomeEntry.get().title(), ementaEntry.get("1.0",END), criterioEscolhido.get())
		if retorno == 1:
			apresentaDialogo('Disciplina já cadastrada','Erro')
		elif retorno == 2:
			apresentaDialogo('Favor preencher os campos','Erro')
		codigoEntry.delete(0,END)
		nomeEntry.delete(0,END)
		ementaEntry.delete("1.0",END)
		codigoEntry.focus_set()

	okButton = Button(frame, text="Inserir", command=insere)
	codigoLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
	codigoEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	nomeLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
	nomeEntry.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	ementaLabel.grid(row=2, column=0, sticky=W, pady=3,padx=3)
	ementaEntry.grid(row=2, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	treeCriterios.grid(row=3, column=0, columnspan=3, sticky=EW, pady=3, padx=3)
	
	okButton.grid(row=4, column=2, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
#	root.bind('<Key>', lambda a : configura_enter(a, insere))    # parametro de ponteiro para função

def disciplinas_consultar(root):
	frame = Frame()
	codigoLabel = Label(frame, text="Código:", underline=0)
	codigoEntry = Entry(frame, textvariable="")
	codigoEntry.focus_set()
	codigo_consultado = StringVar()
	nome_consultado = StringVar()
	ementa_consultada = StringVar()
	criterio_consultado = StringVar()
	codigoLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
	codigoEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	respostaCodigoLabel = Label(frame, text="Código:", underline=0)
	respostaCodigoValor = Label(frame, textvariable=codigo_consultado)
	respostaNomeLabel = Label(frame, text="Nome:", underline=0)
	respostaNomeValor = Label(frame, textvariable=nome_consultado)
	respostaEmentaLabel = Label(frame, text="Ementa:", underline=0)
	respostaEmentaValor = Text(frame, height=10, width=5)
	respostaCriterioLabel = Label(frame, text="Critério:", underline=0)
	respostaCriterioValor = Label(frame, textvariable=criterio_consultado)
	
	def consulta():
		codigo = codigoEntry.get().strip()
		retorno = consulta_disciplina(codigo)
		if retorno == None:			
			apresentaDialogo('Disciplina não encontrada','Erro')
			codigoEntry.delete(0,END)			
			codigoEntry.focus_set()
			respostaCodigoLabel.grid_remove()
			respostaCodigoValor.grid_remove()
			respostaNomeLabel.grid_remove()
			respostaNomeValor.grid_remove()
			respostaEmentaLabel.grid_remove()
			respostaEmentaValor.grid_remove()
		else:
			codigo_consultado.set(retorno['codigo'])
			nome_consultado.set(retorno['nome'])
			ementa_consultada.set(retorno['ementa'])
			
			criterio_consultado.set(retorno['criterio_aprovacao'])
			
			criterio_pesquisado = consulta_criterio(criterio_consultado.get())
			
			if criterio_pesquisado == None:
				criterio_consultado.set("Criterio ainda não escolhido")
			else:
				criterio_consultado.set("Critério " + criterio_pesquisado['codigo'] + ": " + criterio_pesquisado['formula'])
			
			respostaEmentaValor.insert("1.0", ementa_consultada.get())
			respostaCodigoLabel.grid(row=1, column=0, sticky=W, pady=3,padx=3)
			respostaCodigoValor.grid(row=1, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			respostaNomeLabel.grid(row=2, column=0, sticky=W, pady=3,padx=3)
			respostaNomeValor.grid(row=2, column=1, columnspan=3, sticky=EW, pady=3, padx=3)	
			respostaEmentaLabel.grid(row=3, column=0, sticky=W, pady=3,padx=3)
			respostaEmentaValor.grid(row=3, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
			
	consultaButton = Button(frame, text="Consultar", command=consulta)
	consultaButton.grid(row=4, column=2, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : configura_enter(a,consulta))	
	
def criterios_alterar(root):
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

def disciplinas_gerar_relacao(root):
	frame = Frame()
	
	relacaoDisciplinas = gera_relacao_disciplinas()

	treeDisciplinas = ttk.Treeview(frame, columns = (1,2), height = 5, show = "headings")
	treeDisciplinas.pack(side = 'left')

	treeDisciplinas.heading(1, text="Código")
	treeDisciplinas.heading(2, text="Nome")

	treeDisciplinas.column(1, width = 100)
	treeDisciplinas.column(2, width = 100)

	scrollDisciplinas = ttk.Scrollbar(frame, orient="vertical", command=treeDisciplinas.yview)
	scrollDisciplinas.pack(side = 'right', fill = 'y')

	treeDisciplinas.configure(yscrollcommand=scrollDisciplinas.set)

	for disciplina in relacaoDisciplinas:
		treeDisciplinas.insert('', 'end', values = (disciplina['codigo'], disciplina['nome']) )

	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	root.bind('<Key>', lambda a : gera_relacao_disciplinas())
	
	def OnDoubleClick2(event):
		print("selected items:")
		for item in treeDisciplinas.selection():
			valor = treeDisciplinas.item(item)['values']
			item_codigo = str(valor[0])
			item_nome = valor[1]
			print(item_codigo + " - " + item_nome)

	treeDisciplinas.bind("<<TreeviewSelect>>", OnDoubleClick2)	


