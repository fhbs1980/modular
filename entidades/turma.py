
# Encapsulamento dos atributos e disponibilização apenas das funções de acesso
__all__ = ["insere_turma","gera_relacao_turmas","exclui_turma","consulta_turma"]

turmas = []

def insere_turma(codigo):
	for turma in turmas:
		if turma['codigo'] == codigo:
			return 1
	nova_turma = {'codigo': codigo}
	turmas.append(nova_turma)
	return 0

def altera_turma(codigo, campo, valor):
	for turma in turmas:
		if turma['codigo'] == codigo:
			turma[campo] = valor
			return 0
	return 1

def exclui_turma(codigo):
	for turma in turmas:
		if turma['codigo'] == codigo:
			turmas.remove(turma)
			return 0
	return 1

def consulta_turma(codigo):
	for turma in turmas:
		if turma['codigo'] == codigo:
			return turma
	return None

def gera_relacao_turmas():
	relacao_turmas = []
	for turma in turmas:
		relacao_turmas.append(turma)
	return relacao_turmas

