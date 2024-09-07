import time
global pontos
pontos = 0
gabarito= ['a']  # preencham esta lista com o gabarito de cada pergunta
resposta= []    # esta lsta irá armazenar as respostas
feedback= ['Veja o que as cores representam:O retângulo verde, que passou a representar nossa natureza,'
              'antes remetia à Casa de Bragança (a família de dom Pedro I).'
              'O amarelo, hoje símbolo da riqueza mineral do país, era a cor da Casa de Lorena'
              '(da arquiduquesa dona Leopoldina, esposa de dom Pedro I).'
              'E o círculo azul era a esfera armilar, também presente na bandeira portuguesa do Império.'
              'Agora, indica nosso céu estrelado.'] # preencha esta lista com o feedback de cada pergunta
def pergunta1():
    print('Cores de bandeiras')
    print('1. Quais as cores que estão presentes na bandeira do Brasil?')
    print('a)verde, amarelo, azul \nb)branco e vermelho\nc)verde, branco e vermelho\nd)verde, vemelho e amarelo\ne)azul, branco e vermelho')
    resp1 = input()
    # converter a entrada de dados p/ letra maiúscula ou letra minúscula
    # sugiro que incluam validação usando repetição (while)
    resposta.append(resp1)  # inclui a resposta na lista

def correcao1():
    global pontos
    for i in range(len(gabarito)):
        if gabarito[i]==resposta[i]:    
            print('Parabéns você ganhou 10 pontos')
            pontos+=10
        else:
            pontos-=10
            print('Você perdeu 10 pontos, pois errou.')
            time.sleep(5)   # parar 5 segundos p/ ensinar sobre a resposta certa
            print(feedback[i])
        
    
def main():
    pergunta1()
    correcao1()
    print('Pontuação: ', pontos)

main()

