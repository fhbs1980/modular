
# Encapsulamento dos atributos e disponibilização apenas das funções de acesso
__all__ = ["insere_professor","altera_professor", "gera_relacao_professores","exclui_professor","consulta_professor"]

professores = []

def insere_professor(matricula, nome):
	for professor in professores:
		if professor['matricula'] == matricula:
			return 1
	novo_professor = {'matricula': matricula, 'nome': nome}
	professor.append(novo_professor)
	return 0
	
def altera_professor(matricula, campo, valor):
	for professor in professores:
		if professor['matricula'] == matricula:
			professor[campo] = valor
			return 0
	return 1

def exclui_professor(matricula):
	for professor in professores:
		if professor['matricula'] == matricula:
			professores.remove(aluno)
			return 0
	return 1

def consulta_professor(matricula):
	for professor in professores:
		if professor['matricula'] == matricula:
			return professor
	return None

def gera_relacao_professores():
	relacao_professores = []
	for professor in professores:
		relacao_professores.append(professor)
	return relacao_professores

