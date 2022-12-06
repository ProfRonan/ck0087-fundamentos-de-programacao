# Programa para simular a formiguinha de Langton

# Em grade infinita uma formiga anda...
# toda vez que ela encontra um quadrado preto ela gira 90 graus no sentido horário, muda a cor do quadrado para branco e anda para frente.
# toda vez que ela encontra um quadrado branco ela gira 90 graus no sentido anti-horário, muda a cor do quadrado para preto e anda para frente.

# TODO (difícil) Fazer a grade ficar "infinita" adicionando linhas e colunas a medida que for necessário e exibindo somente a parte "proxima" da formiga.
# TODO (difícil) Fazer com que a formiga deixe um rastro colorido.
# TODO Fazer com que o espaço pause o jogo, apertar de novo o jogo volta a rodar.
import pygame

TAMANHO_GRADE = 150
TAMANHO_PIXELS = 5
pos_x = TAMANHO_GRADE//2
pos_y = TAMANHO_GRADE//2

pygame.init()

janela = pygame.display.set_mode(
    (TAMANHO_GRADE*TAMANHO_PIXELS, TAMANHO_GRADE*TAMANHO_PIXELS))

PRETO = 0
COR_PRETA = 0, 0, 0
BRANCO = 1
COR_BRANCA = 255, 255, 255

CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

direção = CIMA  # Começa indo para cima.

grade = []
for i in range(TAMANHO_GRADE):
    linha = []
    for j in range(TAMANHO_GRADE):
        linha.append(PRETO)
    grade.append(linha)


def gira_horário(direção: int):
    return (direção + 1) % 4


def gira_anti_horário(direção: int):
    return (direção - 1) % 4


def anda_para_frente(direção, pos_x, pos_y):
    if direção == CIMA:
        pos_y += 1
    if direção == DIREITA:
        pos_x += 1
    if direção == BAIXO:
        pos_y -= 1
    if direção == ESQUERDA:
        pos_x -= 1
    # Para evitar que a formiga fuja da grade!
    return pos_x % TAMANHO_GRADE, pos_y % TAMANHO_GRADE


def pintar_grade():
    for i in range(TAMANHO_GRADE):
        for j in range(TAMANHO_GRADE):
            if grade[i][j] == BRANCO:
                # pintar de branco essa parte da janela!
                inicio_x = i * TAMANHO_PIXELS
                inicio_y = j * TAMANHO_PIXELS
                pygame.draw.rect(janela, COR_BRANCA, (inicio_x,
                                 inicio_y, TAMANHO_PIXELS, TAMANHO_PIXELS))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    janela.fill(COR_PRETA)
    if grade[pos_x][pos_y] == PRETO:
        grade[pos_x][pos_y] = BRANCO
        direção = gira_horário(direção)
    else:
        grade[pos_x][pos_y] = PRETO
        direção = gira_anti_horário(direção)
    pos_x, pos_y = anda_para_frente(direção, pos_x, pos_y)
    pintar_grade()
    pygame.display.flip()
