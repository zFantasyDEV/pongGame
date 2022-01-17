import pygame #importa a biblioteca

pygame.init() #inicializa o pygame

window = pygame.display.set_mode([1280, 720]) #seta as proporções e cria a janela
title = pygame.display.set_caption("Futebol Pong") #nome do jogo

field = pygame.image.load("assets/field.png") #carrega o campo

score1 = 0
score1_img = pygame.image.load("assets/score/0.png")
score2 = 0
score2_img = pygame.image.load("assets/score/0.png")

win = pygame.image.load("assets/win.png")

player1 = pygame.image.load("assets/player1.png") #carrega o primeiro player
player1_y = 310 #seta a posição inicial
player1_moveup = False #cria a variavel que movera o player 1 para cima
player1_movedown = False #cria a variavel que movera o player 1 para baixo

player2 = pygame.image.load("assets/player2.png") #carrega o player 2
player2_y = 310 #seta a posição inicial
player2_moveup = False
player2_movedown = False

def move_player2(): #faz com que o player 2 siga a bolinha no eixo y
    global player2_y
    if player2_moveup:
        player2_y -= 5
    else:
        player2_y -= 0

    if player2_movedown:
        player2_y += 5
    else:
        player2_y += 0

    if player2_y <= 0:
        player2_y = 0
    elif player2_y >= 575:
        player2_y = 575

def move_player(): #movimento do jogador
    global player1_y #importamos a variavel player1_y para alterar seus valores
    if player1_moveup: #verifica se o jogador está clicando para cima e caso seja verdadeiro ele move para cima
        player1_y -= 5 # -= 5 é a velocidade
    else:
        player1_y -= 0

    if player1_movedown: #verifica se o jogador está clicando para baixo e caso seja verdadeiro ele move para baixo
        player1_y += 5
    else:
        player1_y += 0

    if player1_y <= 0: #limita para onde o jogador poderá andar
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575

ball = pygame.image.load("assets/ball.png") #carrega a bola
ball_x = 617
ball_y = 337
ball_dir_x = -8
ball_dir_y = 1

def move_ball(): #cria função dos movimentos da bolinha
    #faz com que todas as variaveis possam ser usadas na função
    global ball_y
    global ball_x
    global ball_dir_x
    global ball_dir_y
    global score1
    global score2
    global score1_img
    global score2_img


    #adiciona o movimento aos eixos
    ball_x += ball_dir_x
    ball_y += ball_dir_y


    if ball_x < 130: #verifica se a possição x da bolinha é menor qua posição onde o jogador fica
        if player1_y < ball_y + 40: #verifica a hitbox na região de cima do jogador
            if player1_y + 146 > ball_y: #verifica a hitbox na região de baixo do jogador
                ball_dir_x *= -1 #inverte a posição da bolinha

    if ball_x > 1100:
        if player2_y < ball_y + 40:
            if player2_y + 146 > ball_y:
                ball_dir_x *= -1

    #limita a bola na proporção da janela do jogo
    if ball_y > 680:
        ball_dir_y *= -1
    elif ball_y <= 0:
        ball_dir_y *= -1

    #apos a bola sair da tela, o jogo reseta ela no centro
    if ball_x <= -50:
        ball_x = 617
        ball_y = 337
        ball_dir_x *= -1
        ball_dir_y *= -1
        score2 += 1
        score2_img = pygame.image.load("assets/score/" + str(score2) +".png")
    elif ball_x >= 1300:
        ball_x = 617
        ball_y = 337
        ball_dir_x *= -1
        ball_dir_y *= -1
        score1 += 1
        score1_img = pygame.image.load("assets/score/" + str(score1) + ".png")

def draw(): #desenha todos os itens
    if score1 or score2 < 9: #verifico se o placar é menor que 10
        window.blit(field, (0, 0)) #desenha o campo
        window.blit(player1, (50, player1_y)) #desenha o player 1
        window.blit(player2, (1150, player2_y)) #desenha o player 2
        window.blit(ball, (ball_x, ball_y)) #desenha a bola
        window.blit(score1_img, (500, 50))
        window.blit(score2_img, (710, 50))

        #instancio a função após ela ser criada
        move_player()  # instacia a função de movimento do jogador
        move_player2()  # instacia a função de movimento do jogador
        move_ball()  # instacia a função de movimento da bola
    else:
        window.blit(win, (300, 330))


loop = True #mantem o jogo rodando
while loop:
    for events in pygame.event.get(): #pesquisa em pygame.event.get()
        if events.type == pygame.QUIT: #se o tipo do evento for == pygame.QUIT ele encerra o jogo fechando o mesmo
            loop = False

        if events.type == pygame.KEYDOWN: #Se o jogador pressionar
            #JOGADOR 1
            if events.key == pygame.K_w: #se a tecla pressionada for w ele altera o parametro da variavel para True
                player1_moveup = True
            if events.key == pygame.K_s: #se a tecla pressionada for s ele altera o parametro da variavel para True
                player1_movedown = True

            #JOGADOR 2
            if events.key == pygame.K_UP:
                player2_moveup = True
            if events.key == pygame.K_DOWN:
                player2_movedown = True

        if events.type == pygame.KEYUP: #Se o jogador soltar

            #JOGADOR 1
            if events.key == pygame.K_w: #se a tecla soltada for w ele altera o parametro da variavel para False
                player1_moveup = False

            if events.key == pygame.K_s: #se a tecla soltada for w ele altera o parametro da variavel para False
                player1_movedown = False

            #JOGADOR 2
            if events.key == pygame.K_UP:
                player2_moveup = False
            if events.key == pygame.K_DOWN:
                player2_movedown = False

    draw() #desenha as imagens

    pygame.display.update() # mantém se atualizando o jogo
