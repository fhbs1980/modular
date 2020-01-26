def configura_enter(event, funcao):
	key = event.keysym
	if key == 'Return':
		funcao()
