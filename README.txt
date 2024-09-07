===QUIZ MUSICAL===

DESCRIÇÃO:
	O OBJETIVO DESTE JOGO/QUIZ É VERIFICAR O NÍVEL DE CONHECIMENTO GERAL DO JOGADOR SOBRE A MÚSICA, DESDE NOMES DE MÚSICAS E/OU MUSICISTAS IMPORTANTES PARA A HISTÓRIA; IDENTIFICAÇÃO E DISTINÇÃO DOS INSTRUMENTOS MUSICAIS; CONHECIMENTOS SOBRE TEORIA MUSICAL (MELODIA, HARMONIA, RITMO, NOTAS MUSICAIS, ACORDES E ESCALAS), ATÉ GÊNEROS MUSICAIS (SAMBA, PAGODE, ROCK, JAZZ, BLUES, ETC).
	
PÚBLICO ALVO:
	O PÚBLICO ALVO DESTE JOGO SÃO TODAS AS IDADES, MAS PREFERENCIALMENTE DO PÚBLICO ADOLESCENTE ATÉ ADULTO (UMA VEZ QUE, PROVAVELMENTE, ESTA FAIXA ETÁRIA POSSUI MAIS EXPERIÊNCIA COM O ASSUNTO). EM SUMA, QUALQUER PESSOA PODE JOGAR E TESTAR SEU CONHECIMENTO.

MECÂNICA DO JOGO:
	Regra 1: O QUIZ MUSICAL possui 10 perguntas com 5 alternativas (letra A até E) de respostas em que apenas uma é a correta. Para participar do quiz o jogador deve fornecer seu nome/apelido, que será utilizado durante todo o jogo. O não preenchimento deste campo acarretará em não participação e finalização imediata do jogo, retornando a “tela principal”;

	Regra 2: Durante a execução do quiz o jogador deve escolher a opção em que acredita estar a resposta correta, escrevendo, então, no campo “Resposta: “ a alternativa conforme exemplos: “A”, “B”,”C”,”D”,”E”. As respostas são salvas automaticamente após o jogador pressionar a tecla “ENTER” do teclado;

	Regra 3: Caso o usuário deseje retornar à questão anterior ou navegar por entre as questões, basta utilizar o comando: “\browse” + o nº da questão desejada no campo “Resposta: ” de qualquer uma das 10 questões (Exemplo 1). Este comando pode ser usado quantas vezes for necessário. Caso a questão que o usuário esteja visualizando já estiver com alguma resposta, basta escrever o comando à direita da resposta atual (Exemplo 2). Abaixo, dois exemplos:
	Exemplo 1: “Resposta: \browse2”(retorna para a questão 2)
	Exemplo 2: “Resposta: A\browse6”(mantém salvo a resposta da questão (no caso, letra A) e retorna para a questão 6

	Regra 4: Caso o usuário deseje alterar a resposta fornecida em alguma questão basta retornar à pergunta e, ao lado da resposta “antiga”, digitar “\newAnswer” e escrever a nova resposta. Atenção: após a nova digitação deve ser pressionado o botão ENTER do teclado. Exemplo:

 	  Resposta: E (resposta inicial)

	  Resposta: E\newAnswer (solicitação de nova resposta)

	  Resposta: A (nova resposta salva após pressionar ENTER e a próxima pergunta é exibida para o jogador)

	Regra 5: Sempre que o usuário acessar a 10ª pergunta aparecerá um “lembrete” com a mensagem “Dica: digite \finish e pressione ENTER para finalizar o teste” acima do enunciado da questão. Assim que este comando for ativado o jogo limpa a tela e apresenta os resultados (erros e acertos) do jogador, assim como os comentários personalizados. Ao final da página é possível ver 5 mensagens, respectivamente: 
		“Se deseja visualizar suas respostas para cada item digite \answers”
		“Se deseja visualizar o gabarito de cada questão digite \template”
		“Se deseja finalizar e retornar para a página inicial digite \home”
		“Se deseja jogar novamente digite \restart” (permanece com o mesmo nome/ apelido de antes)
		“O que deseja fazer agora? R: ”
	
	Regra 6: Para finalizar o quiz, todas as perguntas precisam ser respondidas. Caso o usuário finalize parcialmente o quiz, o comando “\finish” não funcionará e ele (jogador) receberá o seguinte aviso: “Ops... Parece que você não respondeu alguma(s) questão(ões)”. Em seguida, será informado quais questões não foram respondidas. Para retornar as questões não respondidas basta digitar “\browse”+ o número da questão.
	
	Regra 7: Todos os comandos de atalho aqui fornecidos estarão dispostos na tela inicial do jogo.	

QUANTIDADE E DESCRIÇÃO DOS NÍVEIS:
	- As questões que abordem conteúdos teóricos avançados (melodia, harmonia, escalas e acordes, ritmos, etc) são classificadas como nível difícil. 
	- As questões que abrangem conteúdos como: nomes de músicas, nome de músicos, eventos históricos e gêneros musicais são classificadas como nível médio. 
	- As questões que envolvem identificar e/ou diferenciar instrumentos e notas musicais são classificadas como nível fácil.
	- As 10 questões do quiz estão dispostas da seguinte forma: 3 questões fáceis, 4 questões médias e 4 questões difíceis.

PONTUAÇÃO:
	A cada resposta certa o jogador totaliza 1 ponto. Errar questões significa, portanto, não somar pontos. Assim sendo, não é possível perder pontos, apenas ganhar; A pontuação final do jogador será exibida ao término do quiz, seguindo o formato: “N/10”, em que N é o número de pontos obtidos e 10 é o total de pontos possíveis;
	
	Após a pontuação, será exibido na tela um comentário personalizado baseado na quantidade de pontos obtidos:
  	
  	0-2:  “Você sabe pouco sobre música, mas esta é uma oportunidade para aprender mais! Ouça, estude e viva música!”
  	3-5: “Engatinhando no mundo da música! Continue trilhando o caminho das notas musicais e verá que uma surpresa o espera no final do percurso!”
  	6-8: “Você está no caminho certo! Só mais alguns passos e, quando menos perceber, estará tirando músicas de ouvido!”
  	9-10: “Música é vida interior, e quem tem vida interior jamais padecerá de solidão! - Arthur da Távola”
