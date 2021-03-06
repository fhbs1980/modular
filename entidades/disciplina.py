
# Encapsulamento dos atributos e disponibilização apenas das funções de acesso
__all__ = ["insere_disciplina","altera_disciplina", "gera_relacao_disciplinas","exclui_disciplina","consulta_disciplina"]

disciplinas = []

def insere_disciplina(codigo, nome, ementa, criterio_aprovacao=''):
	codigo = codigo.strip()
	nome = nome.strip()
	ementa = ementa.strip()
	criterio_aprovacao = criterio_aprovacao.strip()
	if codigo == '' or nome == '':
		return 2
	for disciplina in disciplinas:
		if disciplina['codigo'] == codigo:
			return 1
	nova_disciplina = {'codigo': codigo, 'nome': nome, 'ementa': ementa, 'criterio_aprovacao': criterio_aprovacao}
	disciplinas.append(nova_disciplina)
	print(disciplinas)
	return 0

def altera_disciplina(codigo, campo, valor):
	for disciplina in disciplinas:
		if disciplina['codigo'] == codigo:
			disciplina[campo] = valor
			return 0
	return 1

def exclui_disciplina(codigo):
	for disciplina in disciplinas:
		if disciplina['codigo'] == codigo:
			disciplinas.remove(disciplina)
			return 0
	return 1

def consulta_disciplina(codigo):
	for disciplina in disciplinas:
		if disciplina['codigo'] == codigo:
			return disciplina
	return None
		
def gera_relacao_disciplinas():
	relacao_disciplinas = []
	for disciplina in disciplinas:
		relacao_disciplinas.append(disciplina)
	return relacao_disciplinas

