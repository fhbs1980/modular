import unittest
from entidades.aluno import *
from entidades.criterio_aprovacao import *
from entidades.disciplina import *
from entidades.professor import *
from entidades.turma import *

class TestAluno(unittest.TestCase):
	
	#funções são testadas em ordem alfabetica e precisam comecar com test_,
	# por isso test_01 test_02 ...
	
	def test_01_inserir_aluno_ok_condicao_retorno(self):
		print("Script:    Testes")
		print("Autor:     Flavio Bevilacqua")
		print("Data:      21/01/2020")
		print("Propósito: Testar todos os módulos da aplicação de forma automatizada")
		print("\n\n--------------------------------------------------------")
		print("Casos de teste - Módulo Aluno")
		print("--------------------------------------------------------")
		print("Caso de Teste 01 - Condicao de Retorno 0 ao inserir com sucesso")
		retorno_esperado = insere_aluno('9014513','Flavio')
		self.assertEqual(retorno_esperado, 0)
		
	def test_02_inserir_aluno_ok_inserido_com_sucesso(self):
		print("Caso de Teste 02 - Verifica se inseriu efetivamente")
		self.assertIn({'matricula':'9014513','nome':'Flavio'},gera_relacao_alunos())

	def test_03_inserir_aluno_nok_ja_existente(self):
		print("Caso de Teste 03 - Impede a inserção caso já exista a matricula inserida")
		retorno_esperado = insere_aluno('9014513','Flavio')
		self.assertEqual(retorno_esperado, 1 )
		
	def test_04_inserir_aluno_nok_campo_em_branco(self):
		print("Caso de Teste 04 - Impede a inserção caso seja informado algum campo em branco")
		retorno_esperado = insere_aluno('','Flavio')
		self.assertEqual(retorno_esperado, 2 )
		
	def test_05_alterar_aluno_ok_condicao_retorno(self):
		print("Caso de Teste 05 - Condição de Retorno 0 ao alterar com sucesso")
		insere_aluno('9011122','João')
		insere_aluno('9012233','Ana')
		retorno_esperado = altera_aluno('9011122','nome','Matheus')
		self.assertEqual(retorno_esperado, 0)
		
	def test_06_alterar_aluno_ok_alterado_com_sucesso(self):
		print("Caso de Teste 06 - Verifica se alterou efetivamente")
		self.assertIn({'matricula':'9011122','nome':'Matheus'},gera_relacao_alunos())
		
	def test_07_alterar_aluno_nok_nao_existente(self):
		print("Caso de Teste 07 - Verifica se retorna erro ao alterar não existente")
		retorno_esperado = altera_aluno('9010000','nome','Matheus')
		self.assertEqual(retorno_esperado, 1)
		
	def test_08_excluir_aluno_ok_condicao_retorno(self):
		print("Caso de Teste 08 - Condição de Retorno 0 ao excluir com sucesso")
		retorno_esperado = exclui_aluno('9012233')
		self.assertEqual(retorno_esperado, 0)
		
	def test_09_excluir_aluno_ok_excluido_com_sucesso(self):
		print("Caso de Teste 09 - Verifica se excluiu efetivamente")
		self.assertNotIn({'matricula':'9012233','nome':'Ana'},gera_relacao_alunos())
		
	def test_10_excluir_aluno_nok_nao_existente(self):
		print("Caso de Teste 10 - Verifica se retorna erro ao excluir não existente")
		retorno_esperado = exclui_aluno('9010000')
		self.assertEqual(retorno_esperado, 1)
		
	def test_11_consultar_aluno_ok(self):
		print("Caso de Teste 11 - Consulta de aluno existente")
		self.assertEqual({'matricula':'9011122','nome':'Matheus'}, consulta_aluno('9011122'))
		
	def test_12_consultar_aluno_nok_nao_existente(self):
		print("Caso de Teste 12 - Consulta de aluno não existente")
		self.assertEqual(None, consulta_aluno('9011000'))
		
	def test_13_gerar_relacao_alunos(self):
		print("Caso de Teste 13 - Gerar relacao de alunos")
		self.assertEqual([{'matricula':'9014513', 'nome':'Flavio'}, {'matricula':'9011122', 'nome':'Matheus'}], gera_relacao_alunos())
		
	def test_14_gerar_relacao_alunos_vazia(self):
		print("Caso de Teste 14 - Gerar relacao vazia (todos os alunos deletados)")
		exclui_aluno('9014513')
		exclui_aluno('9011122')
		self.assertEqual([], gera_relacao_alunos())

class TestCriterio(unittest.TestCase):
	
	#funções são testadas em ordem alfabetica e precisam comecar com test_,
	# por isso test_1 test_2 ...
	
	def test_01_inserir_criterio_ok_condicao_retorno(self):
		print("\n\n--------------------------------------------------------")
		print("Casos de teste - Módulo Critério de Aprovação")
		print("--------------------------------------------------------")
		print("Caso de Teste 01 - Condicao de Retorno 0 ao inserir com sucesso")
		retorno_esperado = insere_criterio('1','G1+G2/2')
		self.assertEqual(retorno_esperado, 0)
		
	def test_02_inserir_criterio_ok_inserido_com_sucesso(self):
		print("Caso de Teste 02 - Verifica se inseriu efetivamente")
		self.assertIn({'codigo':'1','formula':'G1+G2/2'},gera_relacao_criterios())

	def test_03_inserir_criterio_nok_ja_existente(self):
		print("Caso de Teste 03 - Impede a inserção caso já exista o criterio inserido")
		retorno_esperado = insere_criterio('1','G1+3G2/4')
		self.assertEqual(retorno_esperado, 1 )
		
	def test_04_inserir_criterio_nok_campo_em_branco(self):
		print("Caso de Teste 04 - Impede a inserção caso seja informado algum campo em branco")
		retorno_esperado = insere_criterio('','')
		self.assertEqual(retorno_esperado, 2 )
		
	def test_05_alterar_criterio_ok_condicao_retorno(self):
		print("Caso de Teste 05 - Condição de Retorno 0 ao alterar com sucesso")
		insere_criterio('2','G1+3G2/4')
		insere_criterio('3','G1+2G2/3')
		retorno_esperado = altera_criterio('2','formula','2G1+3G2/5')
		self.assertEqual(retorno_esperado, 0)
		
	def test_06_alterar_criterio_ok_alterado_com_sucesso(self):
		print("Caso de Teste 06 - Verifica se alterou efetivamente")
		self.assertIn({'codigo':'2','formula':'2G1+3G2/5'},gera_relacao_criterios())
		
	def test_07_alterar_criterio_nok_nao_existente(self):
		print("Caso de Teste 07 - Verifica se retorna erro ao alterar não existente")
		retorno_esperado = altera_criterio('4','formula','G1+G2+G3/3')
		self.assertEqual(retorno_esperado, 1)
		
	def test_08_excluir_criterio_ok_condicao_retorno(self):
		print("Caso de Teste 08 - Condição de Retorno 0 ao excluir com sucesso")
		retorno_esperado = exclui_criterio('1')
		self.assertEqual(retorno_esperado, 0)
		
	def test_09_excluir_criterio_ok_excluido_com_sucesso(self):
		print("Caso de Teste 09 - Verifica se excluiu efetivamente")
		self.assertNotIn({'codigo':'1','formula':'G1+G2/2'},gera_relacao_criterios())
		
	def test_10_excluir_criterio_nok_nao_existente(self):
		print("Caso de Teste 10 - Verifica se retorna erro ao excluir não existente")
		retorno_esperado = exclui_criterio('6')
		self.assertEqual(retorno_esperado, 1)
		
	def test_11_consultar_criterio_ok(self):
		print("Caso de Teste 11 - Consulta de criterio existente")
		self.assertEqual({'codigo':'3','formula':'G1+2G2/3'}, consulta_criterio('3'))
		
	def test_12_consultar_criterio_nok_nao_existente(self):
		print("Caso de Teste 12 - Consulta de criterio não existente")
		self.assertEqual(None, consulta_criterio('5'))
		
	def test_13_gerar_relacao_criterios(self):
		print("Caso de Teste 13 - Gerar relacao de criterios")
		self.assertEqual([{'codigo':'2', 'formula':'2G1+3G2/5'}, {'codigo':'3', 'formula':'G1+2G2/3'}], gera_relacao_criterios())
		
	def test_14_gerar_relacao_criterios_vazia(self):
		print("Caso de Teste 14 - Gerar relacao vazia (todos os criterios deletados)")
		exclui_criterio('2')
		exclui_criterio('3')
		self.assertEqual([], gera_relacao_criterios())

class TestDisciplina(unittest.TestCase):
	
	#funções são testadas em ordem alfabetica e precisam comecar com test_,
	# por isso test_1 test_2 ...
	
	def test_01_inserir_disciplina_ok_condicao_retorno_sem_criterio(self):
		print("\n\n--------------------------------------------------------")
		print("Casos de teste - Módulo Disciplina")
		print("--------------------------------------------------------")
		print("Caso de Teste 01 - Condicao de Retorno 0 ao inserir com sucesso - sem criterio")
		retorno_esperado = insere_disciplina('INF1301','Programação Modular','Exemplo de Ementa')
		self.assertEqual(retorno_esperado, 0)
		
	def test_02_inserir_disciplina_ok_condicao_retorno_com_criterio(self):
		print("Caso de Teste 02 - Condicao de Retorno 0 ao inserir com sucesso - com criterio")
		insere_criterio('1','G1+G2/2')
		retorno_esperado = insere_disciplina('INF1082','Linguagens e Técnicas de Programação II','Exemplo de Ementa','1')
		self.assertEqual(retorno_esperado, 0)
		
	def test_03_inserir_disciplina_ok_inserido_com_sucesso_sem_criterio(self):
		print("Caso de Teste 03 - Verifica se inseriu efetivamente sem criterio")
		self.assertIn({'codigo':'INF1301','nome':'Programação Modular','ementa':'Exemplo de Ementa','criterio_aprovacao':''},gera_relacao_disciplinas())

	def test_04_inserir_disciplina_nok_campo_em_branco(self):
		print("Caso de Teste 04 - Impede a inserção caso seja informado algum campo em branco")
		retorno_esperado = insere_disciplina('','','','')
		self.assertEqual(retorno_esperado, 2 )

	def test_05_inserir_disciplina_ok_inserido_com_sucesso_sem_criterio(self):
		print("Caso de Teste 05 - Verifica se inseriu efetivamente com criterio")
		disciplina = consulta_disciplina('INF1082')
		criterio = consulta_criterio(disciplina['criterio_aprovacao'])
		print("Teste realizado: Disciplina" + disciplina['codigo'] + ' critério: ' + criterio['formula'])
		self.assertIn({'codigo':'INF1082','nome':'Linguagens e Técnicas de Programação II','ementa':'Exemplo de Ementa','criterio_aprovacao':'1'},gera_relacao_disciplinas())

	def test_06_inserir_disciplina_nok_ja_existente(self):
		print("Caso de Teste 06 - Impede a inserção caso já exista a disciplina inserida")
		retorno_esperado = insere_disciplina('INF1301','Modularização','Exemplo de Ementa','2')
		self.assertEqual(retorno_esperado, 1 )
		
	def test_07_alterar_disciplina_nome_ok_condicao_retorno(self):
		print("Caso de Teste 07 - Condição de Retorno 0 ao alterar nome com sucesso")
		insere_disciplina('INF1122','Programação III','Exemplo de Ementa')
		insere_disciplina('INF2233','Trabalho Final','Exemplo de Ementa')
		retorno_esperado = altera_disciplina('INF1122','nome','Técnicas de Programação III')
		self.assertEqual(retorno_esperado, 0)
		
	def test_08_alterar_disciplina_ok_alterado_com_sucesso(self):
		print("Caso de Teste 08 - Verifica se alterou nome efetivamente")
		self.assertIn({'codigo':'INF1122','nome':'Técnicas de Programação III','ementa':'Exemplo de Ementa','criterio_aprovacao':''},gera_relacao_disciplinas())
		
	def test_09_alterar_disciplina_ementa_ok_condicao_retorno(self):
		print("Caso de Teste 09 - Condição de Retorno 0 ao alterar ementa com sucesso")
		retorno_esperado = altera_disciplina('INF2233','ementa','Ementa alterada')
		self.assertEqual(retorno_esperado, 0)
		
	def test_10_alterar_disciplina_ok_alterado_com_sucesso(self):
		print("Caso de Teste 10 - Verifica se alterou ementa efetivamente")
		self.assertIn({'codigo':'INF2233','nome':'Trabalho Final','ementa':'Ementa alterada','criterio_aprovacao':''},gera_relacao_disciplinas())
	
	def test_11_alterar_disciplina_nok_nao_existente(self):
		print("Caso de Teste 11 - Verifica se retorna erro ao alterar não existente")
		retorno_esperado = altera_disciplina('INF1234','nome','Outra Disciplina')
		self.assertEqual(retorno_esperado, 1)
		
	def test_12_excluir_disciplina_ok_condicao_retorno(self):
		print("Caso de Teste 12 - Condição de Retorno 0 ao excluir com sucesso")
		retorno_esperado = exclui_disciplina('INF1082')
		self.assertEqual(retorno_esperado, 0)
		
	def test_13_excluir_disciplina_ok_excluido_com_sucesso(self):
		print("Caso de Teste 13 - Verifica se excluiu efetivamente")
		self.assertNotIn({'codigo':'INF1082','nome':'Linguagens e Técnicas de Programação II','ementa':'Exemplo de Ementa','criterio_aprovacao':'1'},gera_relacao_disciplinas())
		
	def test_14_excluir_disciplina_nok_nao_existente(self):
		print("Caso de Teste 14 - Verifica se retorna erro ao excluir não existente")
		retorno_esperado = exclui_disciplina('INF1234')
		self.assertEqual(retorno_esperado, 1)
		
	def test_15_consultar_disciplina_ok(self):
		print("Caso de Teste 15 - Consulta de criterio existente")
		self.assertEqual({'codigo':'INF1301','nome':'Programação Modular','ementa':'Exemplo de Ementa','criterio_aprovacao':''}, consulta_disciplina('INF1301'))
		
	def test_16_consultar_disciplina_nok_nao_existente(self):
		print("Caso de Teste 16 - Consulta de criterio não existente")
		self.assertEqual(None, consulta_disciplina('INF1235'))
		
	def test_17_gerar_relacao_disciplinas(self):
		print("Caso de Teste 17 - Gerar relacao de disciplinas")
		self.assertEqual([{'codigo':'INF1301','nome':'Programação Modular','ementa':'Exemplo de Ementa','criterio_aprovacao':''},{'codigo':'INF1122','nome':'Técnicas de Programação III','ementa':'Exemplo de Ementa','criterio_aprovacao':''},{'codigo':'INF2233','nome':'Trabalho Final','ementa':'Ementa alterada','criterio_aprovacao':''}], gera_relacao_disciplinas())
		
	def test_18_gerar_relacao_disciplina_vazia(self):
		print("Caso de Teste 18 - Gerar relacao vazia (todos os criterios deletados)")
		exclui_disciplina('INF1301')
		exclui_disciplina('INF1122')
		exclui_disciplina('INF2233')
		self.assertEqual([], gera_relacao_disciplinas())

class TestProfessor(unittest.TestCase):
	
	#funções são testadas em ordem alfabetica e precisam comecar com test_,
	# por isso test_01 test_02 ...
	
	def test_01_inserir_professor_ok_condicao_retorno(self):
		print("\n\n--------------------------------------------------------")
		print("Casos de teste - Módulo Professor")
		print("--------------------------------------------------------")
		print("Caso de Teste 01 - Condicao de Retorno 0 ao inserir com sucesso")
		retorno_esperado = insere_professor('9014513','Flavio')
		self.assertEqual(retorno_esperado, 0)
		
	def test_02_inserir_professor_ok_inserido_com_sucesso(self):
		print("Caso de Teste 02 - Verifica se inseriu efetivamente")
		self.assertIn({'matricula':'9014513','nome':'Flavio'},gera_relacao_professores())

	def test_03_inserir_professor_nok_ja_existente(self):
		print("Caso de Teste 03 - Impede a inserção caso já exista a matricula inserida")
		retorno_esperado = insere_professor('9014513','Flavio')
		self.assertEqual(retorno_esperado, 1 )
		
	def test_04_inserir_professor_nok_campo_em_branco(self):
		print("Caso de Teste 04 - Impede a inserção caso seja informado algum campo em branco")
		retorno_esperado = insere_professor('','Flavio')
		self.assertEqual(retorno_esperado, 2 )
		
	def test_05_alterar_professor_ok_condicao_retorno(self):
		print("Caso de Teste 05 - Condição de Retorno 0 ao alterar com sucesso")
		insere_professor('9011122','João')
		insere_professor('9012233','Ana')
		retorno_esperado = altera_professor('9011122','nome','Matheus')
		self.assertEqual(retorno_esperado, 0)
		
	def test_06_alterar_professor_ok_alterado_com_sucesso(self):
		print("Caso de Teste 06 - Verifica se alterou efetivamente")
		self.assertIn({'matricula':'9011122','nome':'Matheus'},gera_relacao_professores())
		
	def test_07_alterar_professor_nok_nao_existente(self):
		print("Caso de Teste 07 - Verifica se retorna erro ao alterar não existente")
		retorno_esperado = altera_professor('9010000','nome','Matheus')
		self.assertEqual(retorno_esperado, 1)
		
	def test_08_excluir_professor_ok_condicao_retorno(self):
		print("Caso de Teste 08 - Condição de Retorno 0 ao excluir com sucesso")
		retorno_esperado = exclui_professor('9012233')
		self.assertEqual(retorno_esperado, 0)
		
	def test_09_excluir_professor_ok_excluido_com_sucesso(self):
		print("Caso de Teste 09 - Verifica se excluiu efetivamente")
		self.assertNotIn({'matricula':'9012233','nome':'Ana'},gera_relacao_professores())
		
	def test_10_excluir_professor_nok_nao_existente(self):
		print("Caso de Teste 10 - Verifica se retorna erro ao excluir não existente")
		retorno_esperado = exclui_professor('9010000')
		self.assertEqual(retorno_esperado, 1)
		
	def test_11_consultar_professor_ok(self):
		print("Caso de Teste 11 - Consulta de professor existente")
		self.assertEqual({'matricula':'9011122','nome':'Matheus'}, consulta_professor('9011122'))
		
	def test_12_consultar_professor_nok_nao_existente(self):
		print("Caso de Teste 12 - Consulta de professor não existente")
		self.assertEqual(None, consulta_professor('9011000'))
		
	def test_13_gerar_relacao_professores(self):
		print("Caso de Teste 13 - Gerar relacao de alunos")
		self.assertEqual([{'matricula':'9014513', 'nome':'Flavio'}, {'matricula':'9011122', 'nome':'Matheus'}], gera_relacao_professores())
		
	def test_14_gerar_relacao_professores_vazia(self):
		print("Caso de Teste 14 - Gerar relacao vazia (todos os alunos deletados)")
		exclui_professor('9014513')
		exclui_professor('9011122')
		self.assertEqual([], gera_relacao_professores())
	
class TestTurma(unittest.TestCase):
	
	#funções são testadas em ordem alfabetica e precisam comecar com test_,
	# por isso test_1 test_2 ...
	
	def test_01_inserir_turma_ok_condicao_retorno(self):
		print("\n\n--------------------------------------------------------")
		print("Casos de teste - Módulo Critério de Aprovação")
		print("--------------------------------------------------------")
		print("Caso de Teste 01 - Condicao de Retorno 0 ao inserir com sucesso")
		retorno_esperado = insere_turma('3WA')
		self.assertEqual(retorno_esperado, 0)
		
	def test_02_inserir_turma_ok_inserido_com_sucesso(self):
		print("Caso de Teste 02 - Verifica se inseriu efetivamente")
		self.assertIn({'codigo':'3WA'},gera_relacao_turmas())

	def test_03_inserir_turma_nok_ja_existente(self):
		print("Caso de Teste 03 - Impede a inserção caso já exista a turma inserido")
		retorno_esperado = insere_turma('3WA')
		self.assertEqual(retorno_esperado, 1 )
		
	def test_04_inserir_turma_nok_campo_em_branco(self):
		print("Caso de Teste 04 - Impede a inserção caso seja informado algum campo em branco")
		retorno_esperado = insere_turma('')
		self.assertEqual(retorno_esperado, 2 )
		
	def test_05_alterar_turma_ok_condicao_retorno(self):
		print("Caso de Teste 05 - Condição de Retorno 0 ao alterar com sucesso")
		insere_turma('3WB')
		insere_turma('3WC')
		retorno_esperado = altera_turma('3WB','codigo','3WD')
		self.assertEqual(retorno_esperado, 0)
		
	def test_06_alterar_turma_ok_alterado_com_sucesso(self):
		print("Caso de Teste 06 - Verifica se alterou efetivamente")
		self.assertIn({'codigo':'3WD'},gera_relacao_turmas())
		
	def test_07_alterar_turma_nok_nao_existente(self):
		print("Caso de Teste 07 - Verifica se retorna erro ao alterar não existente")
		retorno_esperado = altera_turma('3WE','codigo','3WF')
		self.assertEqual(retorno_esperado, 1)
		
	def test_08_excluir_turma_ok_condicao_retorno(self):
		print("Caso de Teste 08 - Condição de Retorno 0 ao excluir com sucesso")
		retorno_esperado = exclui_turma('3WA')
		self.assertEqual(retorno_esperado, 0)
		
	def test_09_excluir_turma_ok_excluido_com_sucesso(self):
		print("Caso de Teste 09 - Verifica se excluiu efetivamenteo")
		self.assertNotIn({'codigo':'3WA'},gera_relacao_turmas())
		
	def test_10_excluir_turma_nok_nao_existente(self):
		print("Caso de Teste 10 - Verifica se retorna erro ao excluir não existente")
		retorno_esperado = exclui_turma('3WF')
		self.assertEqual(retorno_esperado, 1)
		
	def test_11_consultar_turma_ok(self):
		print("Caso de Teste 11 - Consulta de turma existente")
		self.assertEqual({'codigo':'3WD'}, consulta_turma('3WD'))
		
	def test_12_consultar_turma_nok_nao_existente(self):
		print("Caso de Teste 12 - Consulta de turma não existente")
		self.assertEqual(None, consulta_turma('3WG'))
		
	def test_13_gerar_relacao_turmas(self):
		print("Caso de Teste 13 - Gerar relacao de turmas")
		self.assertEqual([{'codigo':'3WD'}, {'codigo':'3WC'}], gera_relacao_turmas())
		
	def test_14_gerar_relacao_turmas_vazia(self):
		print("Caso de Teste 14 - Gerar relacao vazia (todas as turmas deletadas)")
		exclui_turma('3WD')
		exclui_turma('3WC')
		self.assertEqual([], gera_relacao_turmas())	
	
unittest.main()
