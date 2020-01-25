
# Encapsulamento dos atributos e disponibilização apenas das funções de acesso
__all__ = ["insere_criterio","altera_criterio", "gera_relacao_criterios","exclui_criterio","consulta_criterio"]

criterios = []

def insere_criterio(codigo, formula):
	for criterio in criterios:
		if criterio['codigo'] == codigo:
			return 1
	novo_criterio = {'codigo': codigo, 'formula': formula}
	criterios.append(novo_criterio)
	return 0

def altera_criterio(codigo, campo, valor):
	for criterio in criterios:
		if criterio['codigo'] == codigo:
			criterio[campo] = valor
			return 0
	return 1

def exclui_criterio(codigo):
	for criterio in criterios:
		if criterio['codigo'] == codigo:
			criterios.remove(criterio)
			return 0
	return 1

def consulta_criterio(codigo):
	for criterio in criterios:
		if criterio['codigo'] == codigo:
			return criterio
	return None	

def gera_relacao_criterios():
	relacao_criterios = []
	for criterio in criterios:
		relacao_criterios.append(criterio)
	return relacao_criterios


