
# Encapsulamento dos atributos e disponibilização apenas das funções de acesso
__all__ = ["insere_aluno","altera_aluno", "gera_relacao_alunos","exclui_aluno","consulta_aluno"]

alunos = []

def insere_aluno(matricula, nome):
	matricula = matricula.strip()
	nome = nome.strip()
	if matricula == '' or nome == '':
		return 2
	for aluno in alunos:
		if aluno['matricula'] == matricula:
			return 1
	novo_aluno = {'matricula': matricula, 'nome': nome}
	alunos.append(novo_aluno)
	print(alunos)
	return 0
	
def altera_aluno(matricula, campo, valor):
	for aluno in alunos:
		if aluno['matricula'] == matricula:
			aluno[campo] = valor
			return 0
	return 1

def exclui_aluno(matricula):
	for aluno in alunos:
		if aluno['matricula'] == matricula:
			alunos.remove(aluno)
			return 0
	return 1

def consulta_aluno(matricula):
	for aluno in alunos:
		if aluno['matricula'] == matricula:
			return aluno
	return None

def gera_relacao_alunos():
	relacao_alunos = []
	for aluno in alunos:
		relacao_alunos.append(aluno)
	return relacao_alunos

