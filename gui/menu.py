from tkinter import *
from gui.form_aluno import *

def executa1():
	frame = Frame()
	nameLabel = Label(frame, text="Nome:", underline=0)
	nameEntry = Entry(frame, textvariable="oi")
	nameEntry.focus_set()
	okButton = Button(frame, text="Localizar", command=executa2)
	cancelButton = Button(frame, text="Cancelar", command=root.quit)
	nameLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
	nameEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
	okButton.grid(row=2, column=2, sticky=EW, pady=3, padx=3)
	cancelButton.grid(row=2, column=3, sticky=EW, pady=3, padx=3)
	frame.grid(row=0, column=0, sticky=NSEW)
	frame.columnconfigure(1, weight=1)
	

   
def executa2():
   frame = Frame()
   nameLabel = Label(frame, text="Nome2:", underline=0)
   nameEntry = Entry(frame, textvariable="oi")
   nameEntry.focus_set()
   okButton = Button(frame, text="Localizar", command=executa2)
   cancelButton = Button(frame, text="Cancelar", command=root.quit)
   nameLabel.grid(row=0, column=0, sticky=W, pady=3,padx=3)
   nameEntry.grid(row=0, column=1, columnspan=3, sticky=EW, pady=3, padx=3)
   okButton.grid(row=3, column=2, sticky=EW, pady=3, padx=3)
   cancelButton.grid(row=2, column=3, sticky=EW, pady=3, padx=3)
   frame.grid(row=0, column=0, sticky=NSEW)
   frame.columnconfigure(1, weight=1)
   
def executa3():
   filewin = Toplevel(root)
   button = Button(filewin, text="C")
   button.pack()
   
def executa4():
   filewin = Toplevel(root)
   button = Button(filewin, text="D")
   button.pack()

def executa5():
   filewin = Toplevel(root)
   button = Button(filewin, text="E")
   button.pack()

def criaMenu():
	root = Tk()
	root.geometry("300x200+200+100")
	root.title("Aplicação Matrícula")

	menu_aluno = [{'nome':'Incluir','id':'incluir'},{'nome':'Alterar','id':'alterar'},{'nome':'Excluir','id':'excluir'},{'nome':'Consultar','id':'consultar'},{'nome':'Gerar Relação','id':'gerar_relacao'}]
	menu_criterio = [{'nome':'Incluir','id':'incluir'},{'nome':'Alterar','id':'alterar'},{'nome':'Excluir','id':'excluir'},{'nome':'Consultar','id':'consultar'},{'nome':'Gerar Relação','id':'gerar_relacao'}]
	menu_disciplina = [{'nome':'Incluir','id':'incluir'},{'nome':'Alterar','id':'alterar'},{'nome':'Excluir','id':'excluir'},{'nome':'Consultar','id':'consultar'},{'nome':'Gerar Relação','id':'gerar_relacao'}]
	menu_professor = [{'nome':'Incluir','id':'incluir'},{'nome':'Alterar','id':'alterar'},{'nome':'Excluir','id':'excluir'},{'nome':'Consultar','id':'consultar'},{'nome':'Gerar Relação','id':'gerar_relacao'}]
	menu_turma = [{'nome':'Incluir','id':'incluir'},{'nome':'Alterar','id':'alterar'},{'nome':'Excluir','id':'excluir'},{'nome':'Consultar','id':'consultar'},{'nome':'Gerar Relação','id':'gerar_relacao'}]

	menu_cadastro = [{'nome':'Alunos','id':'alunos','opcoes': menu_aluno}, 
					{'nome':'Critérios de Aprovação','id':'criterios','opcoes': menu_criterio}, 
					{'nome':'Disciplinas','id':'disciplinas','opcoes': menu_disciplina}, 
					{'nome':'Professores','id':'professores','opcoes': menu_professor}, 
					{'nome':'Turmas','id':'turmas','opcoes': menu_turma}]

	menu_principal = [{'nome':'Cadastros','opcoes': menu_cadastro}]

	funcionalidades = {'alunos_incluir':alunos_incluir,
					   'alunos_alterar':executa2,
					   'alunos_excluir':executa3,
					   'alunos_consultar':executa4,
					   'alunos_gerar_relacao':executa5,
                       'criterios_incluir':executa1,
                       'criterios_alterar':executa2,
                       'criterios_excluir':executa3,
                       'criterios_consultar':executa4,
                       'criterios_gerar_relacao':executa5,
                       'disciplinas_incluir':executa1,
                       'disciplinas_alterar':executa2,
                       'disciplinas_excluir':executa3,
                       'disciplinas_consultar':executa4,
                       'disciplinas_gerar_relacao':executa5,
                       'professores_incluir':executa1,
                       'professores_alterar':executa2,
                       'professores_excluir':executa3,
                       'professores_consultar':executa4,
                       'professores_gerar_relacao':executa5,
                       'turmas_incluir':executa1,
                       'turmas_alterar':executa2,
                       'turmas_excluir':executa3,
                       'turmas_consultar':executa4,
                       'turmas_gerar_relacao':executa5,
                      }

	menubar = Menu(root)
	for nivel1 in menu_principal:
		menunivel1 = Menu(menubar, tearoff = 0)
		for nivel2 in nivel1['opcoes']:
			menunivel2 = Menu(menunivel1, tearoff = 0)
			for nivel3 in nivel2['opcoes']:
				nome_funcao = nivel2['id'] + '_' + nivel3['id']
				nome_funcao = nome_funcao.lower()
				menunivel2.add_command(label=nivel3['nome'], command = funcionalidades[nome_funcao])
			menunivel1.add_cascade(label=nivel2['nome'], menu=menunivel2)
		menubar.add_cascade(label=nivel1['nome'], menu=menunivel1)
	menubar.add_command(label = "Sair", command = root.quit)

	root.config(menu = menubar)
	root.mainloop()
