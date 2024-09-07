def pulaLinhas ():
    print('\n'*40)
def atalhosQuiz (Q):
    indice = 0
    for indice in range (len(Gabarito)):
        if (Q[1:] == "\ BROWSE" + (indice + 1))or (Q == "\ BROWSE" + (indice + 1)):
            return questoes(indice+1)
        elif (Q[1:] == "\ newAnswer"):
            Q = str(input("Resposta: ")).upper()
        indice+=1
        
         

def validacao (Q):
    while Q != "A" or Q!= "B" or Q != "C" or Q != "D" or Q != "E":
            print("Resposta inválida")
            input("Digite uma resposta válida(entre A e E): ")
    
  
def TelaInicial ():
    print('''
                        Seja Bem-Vindo ao Quiz Musical!



                                Dicas de jogo:

         \ browse + nº da questão : comando para navegar entre as questões
             \ newAnswer: comando para alterar a resposta fornecida
                 \ finish + pressione ENTER: finalizar o teste
\ answers: comando para visualizar as respostas para cada item, após o término do quiz
\ template: comando para visualizar o gabarito de cada questão, após o término do quiz
                 \home: finalizar e retornar a página inicial
     \ restart: comando para jogar novamente (com o mesmo nome/apelido de antes)
                       

    ''')
    
    Jogador = str(input("Digite seu nome/apelido: "))
    if Jogador == "":
        pulaLinhas()
        return TelaInicial()
def RegrasDoJogo ():
    print('''
                                                        Atenção para as regras do jogo:


O QUIZ MUSICAL possui 10 perguntas com 5 alternativas de resposta. Apenas uma é a correta. Para responder às perguntas você deve escolher a opção que achar correta e,
em seguida, escrevê-la no campo "Resposta: " conforme o exemplo:
                                                                Resposta: A
Suas respostas são salvas automaticamente após pressionar a tecla ENTER do seu teclado.

Caso deseje retornar ou navegar pelas questões, basta escrever \ browse + o nº da questão desejada. Pode usar este atalho quantas vezes precisar!
Seguem alguns exemplos:

                                                     Resposta: \ browse2" (retorna para a questão 2)
                                Resposta: A\ browse6 (mantém salva sua resposta na questão atual - A - e vai para a questão 6) 

Para alterar sua resposta em qualquer pergunta basta digitar \ newAnswer e, após pressionar ENTER, inserir a nova resposta. Exemplo:

                                                     Resposta: E (resposta inicial)

                                                     Resposta: E\ newAnswer (solicitação de nova resposta)

                                                     Resposta: A (nova resposta salva após pressionar ENTER)

Para finalizar o quiz digite \ finish ao lado de sua última resposta. ATENÇÃO: para finalizar é necessário ter respondido TODAS AS QUESTÕES.
DICA EXTRA SOBRE OS ATALHOS: CUIDADO COM O ESPAÇAMENTO!

Escreva \ start para começar:
''')
    start = str(input()).lower()
    if start != "\ start":
        pulaLinhas()
        return RegrasDoJogo()
  
def Questoes ():
    global respostas
    global Q
    global questoes 
    respostas = []
    def Pergunta1 ():
        A1 = print('''
"Questão 1:\n"
A Música pode ser entendida como a arte de combinar sons e ritmos a partir de uma pré-organização construída ao longo da história. Trata-se, portanto, do uso ordenado
do som. Existe uma diferença essencial entre o que pode ou não ser considerado música, e esta definição está associada à distinção entre SOM e RUÍDO. 

O som é qualquer vibração regular – causada por um corpo sonoro musical, pelo canto dos pássaros, voz humana e instrumentos musicais – que o ouvido humano possa captar
e interpretar em notas musicais. Já o Ruído é um resultado de vibrações irregulares produzidas, por exemplo, pelas máquinas, carros, turbina de avião, entre outros.

De acordo com a definição dada acima, analise as opções abaixo e assinale a que NÃO CONDIZ com esta classificação (isto é, marque a INCORRETA):
A)Canto dos Pássaros: SOM
B)“Chiados” em uma televisão sem sinal: RUÍDO
C)O barulho produzido ao abrir ou fechar um Zíper: RUÍDO
D)O barulho de uma porta abrindo: SOM
E)O som de uma flauta: SOM''')
        Q = str(input("Resposta: ")).upper()
        atalhosQuiz(Q)
        validacao(Q)
        respostas.append(Q)
        pulaLinhas()

#fim da questão 1    
    def Pergunta2 ():
        A2 = print('''
"Questão 2:\n"
Na base de toda música estão as NOTAS MUSICAIS. Todos nós, em algum momento da vida, somos apresentados a essas notas; e os mais sortudos têm o interesse – ou a
oportunidade – de praticar um instrumento desde a infância ou juventude. TODAS (repetindo: TODAS) as músicas que você conhece são escritas, cantadas, produzidas,
compostas e tocadas em cima das notas musicais.

Abaixo, assinale QUANTAS e QUAIS são as notas musicais:
A)8: DÓ – RÉ – MI – FÁ – SOL – LÁ – SI – DÓ
B)7: DÓ – RÉ – MI – FÁ – SOL – LÁ – SI 
C)5: DÓ – RÉ – MI – FÁ – DÓ
D)6: DÓ – RÉ – MI – FÁ – SOLÁ – SI
E)5: DÓ – RÉ – MI – FA – SOL''')
        Q = str(input("Resposta: ")).upper()
        atalhosQuiz(Q)
        validacao(Q)
        respostas.append(Q)
        pulaLinhas()

#fim da questão 2
    def Pergunta3 ():
        A3 = print('''
"Questão 3:\n"
As grandes e pequenas composições, de forma geral, foram feitas com base na utilização primorosa dos mais diversos instrumentos e vozes musicais. Existem inúmeros
instrumentos de diferentes tipos: instrumentos de sopro, de cordas, de teclas, de percussão e entre outros. Alguns instrumentos são mais conhecidos popularmente, como
o Violão, a Guitarra, a Bateria e o Piano. Relacione a coluna da esquerda com a da direita abaixo e, em seguida, assinale a alternativa que apresenta a sequência
CORRETA:

INSTRUMENTO	TIPO
(A) TROMPETE	(1) INSTRUMENTO DE TECLAS
(B) TECLADO	(2) INSTRUMENTO DE CORDAS
(C) PRATOS	(3) INSTRUMENTO DE SOPRO
(D) CONTRABAIXO	(4) INSTRUMENTO DE PERCUSSÃO

A)A4 – B1 – C2 – D3
B)A2 – B1 – C4 – D3
C)A3 – B1 – C4 – D2
D)A2 – B3 – C1 – D4
E)A1 – B3 – C2 – D4''')
        Q = str(input("Resposta: ")).upper()
        atalhosQuiz(Q)
        validacao(Q)
        respostas.append(Q)
        pulaLinhas()
#fim da questão 3
    def Pergunta4 ():
        B1 = print('''
"Questão 4:\n"
Ao longo do tempo, muitos músicos marcaram a história com canções e obras atemporais; obras estas que são lembradas até os dias atuais. A seguir são listados apenas
alguns dos nomes mais importantes para a música nacional e mundial. Ao lado de cada nome existe uma estimativa de qual época, aquele músico viveu e algumas músicas
marcantes do autor. 
Observe atentamente as opções e, logo após, assinale qual alternativa você acredita que esteja mais próxima com a verdade. Ou seja: escreva a alternativa em que o
conjunto (nome do autor, época e obras) pareça o mais próximo possível com a realidade:
DICA: Vale usar o “chutômetro”, desde que feito com consciência (risos)

A)Heitor Villa-Lobos - (1560 – 1621) – Bachianas Brasileiras;
B)Queen – (1910) – Bohemian Rhapsody, We are the Champions, We Will Rock You;
C)Frank Sinatra - (2001- presente) – Fly me to the moon, My Way, That’s Life;
D)Ludwig van Beethoven - (1770 – 1827) – Rondo Alla Turca e Lacrimosa;
E)Michael Jackson - (1958 – 2009) - Smooth Criminal, Beat It, Billie Jean e Thiller;''')
        Q = str(input("Resposta: ")).upper()
        atalhosQuiz(Q)
        validacao(Q)
        respostas.append(Q)
        pulaLinhas()
#fim da questão 4
    def Pergunta5 ():
        B2 = print('''
"Questão 5:\n"
Sobre o gênero musical conhecido como “música clássica” existem diversos compositores que marcaram esta fase. Assinale abaixo a alternativa que contém APENAS músicos
e instrumentistas clássicos:
A)Chopin, Bach, Beethoven, Mozart.
B)Carlinhos Brown, Luis Gonzaga, Tim Maia e Ed Motta.
C)Adele, Ariana Grande, Bruno Mars e Justin Timberlake.
D)Beethoven, Tchaikovski, Franz Schubert e Ray Charles.
E)Fabio Assunção, Antônio Fagundes, Tom Holland e Dwaney Johnson.''')
        Q = str(input("Resposta: ")).upper()
        atalhosQuiz(Q)
        validacao(Q)
        respostas.append(Q)
        pulaLinhas()
#fim da questão 5
    def Pergunta6 ():
        B3 = print('''
"Questão 6:\n"
Uma das maiores confusões feitas por muita gente é utilizar os termos “gênero” e “ritmo” como sinônimos no estudo da Música. Gêneros são categorias que contém peças
musicais que compartilham elementos em comum. Os gêneros definem e classificam músicas em suas qualidades. Ademais, alguns gêneros musicais possuem semelhanças entre
si, o que muitas vezes torna difícil classificar “x” música em gênero “A” ou “B”. Já o Ritmo faz referência ao tempo ou “andar” da música.

Levando em consideração o enunciado acima, assinale a alternativa que NÃO APRESENTA gêneros musicais com características semelhantes:
A)Rock e Heavy Metal
B)Jazz, Blues, Soul e Funk.
C)Axé e Forró.
D)Samba e Pagode
E)Hip-hop e Eletrônica.''')
        Q = str(input("Resposta: ")).upper()
        atalhosQuiz(Q)
        validacao(Q)
        respostas.append(Q)
        pulaLinhas()
#fim da questão 6
    def Pergunta7 ():
        C1 = print('''
"Questão 7:\n"
Como dito em questões anteriores, toda música é feita de notas musicais. Mas, apenas as notas não são suficientes para caracterizar uma boa música. Toda música
utiliza, das mais variadas formas, um conjunto de sons e pausas (silêncios) que a torna agradável ao ouvido. Ela possui três características fundamentais: MELODIA,
HARMONIA E RITMO.  Qual seria o melhor conjunto de definições para cada uma das 3 características citadas, respetivamente?

A)Melodia é o “carro-chefe” da música. É ela que conduz tudo o que acontece e tudo gira entorno dela. Harmonia faz referência ao fato da música ser agradável ou não,
e pode variar conforme a percepção de cada um. Ritmo, por fim, diz respeito aos diferentes tipos de música, como Country, Jazz, Samba e Choro.

B)Melodia é o “carro-chefe” da música. É ela que conduz tudo o que acontece e tudo gira entorno dela. Harmonia faz referência ao fato da música ser agradável ou não,
e pode variar conforme a percepção de cada um. Ritmo, por fim, diz respeito ao tempo da música; em uma partitura poderia ser representado pela fórmula
de compasso (2/4;3/4;4/4 entre outros).

C)A melodia de uma música é a sequência de notas que são tocadas ou cantadas. É a voz principal da música, podendo ser representada pelo canto ou por um solo de
guitarra, por exemplo. A harmonia é o elemento mais importante da música, definida como um conjunto de acordes formados pela união de várias notas tocadas
simultaneamente. É a sonoridade que serve de base para a melodia. Por fim, o ritmo é a marcação do tempo de uma música; ele que determina a duração, velocidade,
intensidade e os valores de cada nota. O ritmo é responsável por gerir e equilibrar os momentos de som e pausa dentro da composição. Em uma partitura, podem ser
representados pelas fórmulas de compasso (2/4;3/4;4/4 entre outros).

D)Melodia, Ritmo e Harmonia são a mesma coisa, porém com nomes e aplicações diferentes.

E)Melodia é o tempo da música e o andamento da mesma; Harmonia é a voz principal e o Ritmo é um conjunto de notas (acordes) que servem de base para a Harmonia.''')
        Q = str(input("Resposta: ")).upper()
        atalhosQuiz(Q)
        validacao(Q)
        respostas.append(Q)
        pulaLinhas()
#fim da questão 7
    
    def Pergunta8 ():
        C2 = print('''
"Questão 8:\n"
Uma vez que as notas são dispostas em conjunto, podemos começar a falar de ESCALAS MUSICAIS. Escalas nada mais são do que uma sequência de notas ordenadas a partir de
um referencial, que se sucedem conforme “padrões de distâncias” bem definidos. Esses padrões são chamados de INTERVALOS MUSICAIS. A distância pode ser medida de duas
formas: TOM e SEMITOM. Dizer que uma nota “caminha” um tom é dizer que ela fez o percurso completo. Imagine que você precise subir uma escada: você pode subir ela até
o final ou então subir até a metade dela (ou então nem subir). Quando a nota “sobe metade da escada” dizemos que ela caminhou em um Semitom.

Esta é a base de qualquer formação de escala musical. Existem inúmeras escalas musicais, mas as mais conhecidas são: ESCALA MAIOR e ESCALA MENOR. Abaixo está exposta
a escala maior da nota dó (referencial da escala):
                                                        DÓ – RÉ – MI – FÁ – SOL – LÁ – SI – DÓ 
Sabendo que somente a nota MI e a nota SI podem caminhar, no máximo, 1 semitom, escreva quais são os intervalos característicos de uma escala maior:
A)TOM – TOM – SEMITOM – TOM – TOM – TOM – TOM
B)SEMITOM – TOM – TOM – SEMITOM – TOM – TOM –TOM
C)TOM – SEMITOM – TOM – TOM – TOM – SEMITOM – TOM
D)TOM – TOM – TOM – SEMITOM – TOM – TOM – SEMITOM
E)TOM – TOM – SEMITOM – TOM – TOM – TOM – SEMITOM''')
        Q = str(input("Resposta: ")).upper()
        atalhosQuiz(Q)
        validacao(Q)
        respostas.append(Q)
        pulaLinhas()
#fim da questão 8
    
    def Pergunta9 ():
        C3 = print('''
"Questão 9:\n"
Quando tratamos de harmonia estamos falando de um empilhar de notas, podendo ser em forma de tríades (3 notas) ou tétrades (4 notas). Para se referir aos acordes de
cada nota musical utiliza-se as 7 primeiras letras do alfabeto, conforme o exemplo: C (acorde de DÓ); D (Acorde de RÉ); E (Acorde de MI); [...]

Seguindo este raciocínio, analise as opções a seguir e assinale a alternativa que contém a letra correta para o respectivo acorde:
A)A: acorde de LÁ;
B)G: acorde de MI;
C)H: acorde de LÁ;
D)B: acorde de RÉ;
E)Z: acorde de SOL;''')
        Q = str(input("Resposta: ")).upper()
        atalhosQuiz(Q)
        validacao(Q)
        respostas.append(Q)
        pulaLinhas()
#fim da questão 9
    def Pergunta10 ():
        C4 = print('''
"Questão 10:\n"
Os acordes podem ser do tipo maior ou menor. O Acorde maior é representado apenas pelas letras (C, D, E...), enquanto o acorde menor é acompanhado do símbolo “m” ao
lado da Letra em questão: Dm (acorde de Ré menor); Em (acorde de Mi menor), entre outros.

Não é apenas a nomenclatura que define um acorde maior ou menor, mas a sequência de intervalos.
O acorde de C (Dó maior) corresponde a união entre as notas Dó, Mi e Sol (perceba a distância entre estas notas: de Dó para Mi temos 2 TONS, e de Mi para Sol temos
1 TOM e 1 SEMITOM).
O acorde de Dm (Ré menor) corresponde a união entre as notas Ré, Fá e Lá (perceba a distância entre as notas: de Ré para Fá temos 1 TOM e 1 SEMITOM; de Fá para Lá
temos 2 TONS).

Após compreender esta relação, observe a sequência abaixo:
                                                        C – Dm – Em – F – G – Am – Bm – C
Quantos destes acordes possuem 2 TONS de distância entre alguma de suas notas?
A)Os acordes C, F, G e C.
B)Nenhum.
C)Os acordes Dm, Em, Am, Bm.
D)Todos.
E)Os acordes C, F e G.''')
        Q = str(input("Resposta: ")).upper()
        atalhosQuiz(Q)
        validacao(Q)
        respostas.append(Q)
        pulaLinhas()
#fim da questão 10
    questoes = [Pergunta1,Pergunta2,Pergunta3,Pergunta4,Pergunta5,Pergunta6,Pergunta7,Pergunta8,Pergunta9,Pergunta10]


def gabarito (respostas):
    if Gabarito == respostas:
        print("10/10")
    else:
        i=0
        incorretas = []
        num_pergunta = []
        for i in range (len(Gabarito)):
            if respostas[i] != Gabarito[i]:
                incorreta = respostas[i]
                num_questao = i+1
                incorretas.append(incorreta)
                num_pergunta.append(num_questao)
                i+=1
        print ("você errou as seguintes questões: ")
        j=0
        for j in range (len(incorretas)):
            A = num_pergunta[j]
            B = incorretas[j]
            print (A, "(respondeu ", B, ")")
def telaFinal ():
    print('''



''')
def main ():
    global Jogador
    global Gabarito
    Gabarito = ['D','B','C','E','A','B','C','E','A','D']    
    TelaInicial()
    pulaLinhas()
    RegrasDoJogo()
    pulaLinhas()
    Questoes()
    gabarito(respostas)

main()
