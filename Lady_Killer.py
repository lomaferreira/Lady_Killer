import pygame
import os  # Caminho do diretório do jogo
from random import randint

# Armazena o caminho absoluto do arquivo, permitindo que rode em qualquer mâquina
diretorio_principal = os.path.dirname(__file__)
# armazena o diretorio/caminho que as sprites estão unindo com o dirétorio principal(onde o arquivo do jogo está)
diretorio_sprites = os.path.join(diretorio_principal, 'sprites')
diretorio_audio = os.path.join(diretorio_principal, 'audio')
diretorio_background = os.path.join(diretorio_principal, 'background')
diretorio_janelas = os.path.join(diretorio_principal, 'windows')


pygame.init()

largura = 840
altura = 580

cor_preto = (0, 0, 0)
cor_branco = (255, 255, 255)

# Controle de volume da musica de fundo(0 a 1)
pygame.mixer.music.set_volume(0.1)
# Carregando audios
musica_de_fundo = pygame.mixer.music.load(
    'audio/BoxCat Games - Young Love.mp3')
barulho_colisao = pygame.mixer.Sound('audio/smw_spring_jump.wav')
barulho_colisao.set_volume(0.4)
# Repete a música
pygame.mixer.music.play(-1)


# Cria a tela com largura e altura pré definida
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Lady Killer')


# Carrengando todas as sprites
sprite_sheet_duck = pygame.image.load(os.path.join(
    diretorio_background, 'duck_spritesheet.png')).convert_alpha()
sprite_sheet_walk = pygame.image.load(os.path.join(
    diretorio_sprites, 'Walk.png')).convert_alpha()
sprite_sheet_Idle = pygame.image.load(os.path.join(
    diretorio_sprites, 'Idle.png')).convert_alpha()
sprite_sheet_Idle_invisivil = pygame.image.load(os.path.join(
    diretorio_sprites, 'Idle_invisivel.png')).convert_alpha()
sprite_sheet_vitima = pygame.image.load(os.path.join(
    diretorio_sprites, 'vitima/Walk_vitima.png')).convert_alpha()
sprite_sheet_Attack = pygame.image.load(os.path.join(
    diretorio_sprites, 'Attack_4.png')).convert_alpha()
sprite_morte = pygame.image.load(os.path.join(
    diretorio_sprites, 'morte/Running.png')).convert_alpha()


# Cenário do jogo
imagem_fundo = pygame.image.load(os.path.join(
    diretorio_background, 'city_background.jpg')).convert_alpha()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

imagem_fundo2 = pygame.image.load(os.path.join(
    diretorio_background, 'city_background2.jpg')).convert_alpha()
imagem_fundo2 = pygame.transform.scale(imagem_fundo2, (largura, altura))

# Janelas e botões do jogo
imagem_fim_de_jogo = pygame.image.load(os.path.join(
    diretorio_janelas, 'fim_de_jogo.png')).convert_alpha()
imagem_fim_de_jogo = pygame.transform.scale(
    imagem_fim_de_jogo, (largura, altura))

imagem_botao_jogar = pygame.image.load(os.path.join(
    diretorio_janelas, 'botao_jogar.png')).convert_alpha()
imagem_botao_jogar = pygame.transform.scale(imagem_botao_jogar, (200, 100))

imagem_botao_controles = pygame.image.load(os.path.join(
    diretorio_janelas, 'controles.png')).convert_alpha()
imagem_botao_controles = pygame.transform.scale(
    imagem_botao_controles, (180, 80))

imagem_botao_sair = pygame.image.load(os.path.join(
    diretorio_janelas, 'botao_sair.png')).convert_alpha()
imagem_botao_sair = pygame.transform.scale(imagem_botao_sair, (180, 80))

imagem_mensagem = pygame.image.load(os.path.join(
    diretorio_janelas, 'mensagem_intrucao.png')).convert_alpha()
imagem_mensagem = pygame.transform.scale(imagem_mensagem, (largura, altura))

tela_inicial = pygame.image.load(os.path.join(
    diretorio_janelas, 'tela_inicial.png')).convert_alpha()


# Cria uma superficie e coloca a sprite sobre ela
def Obter_Sprite(sprite, frame, y_coordenada, largura_sprite, altura_sprite, scale, colour):
    # cria  uma superficie img
    img = pygame.Surface((largura_sprite, altura_sprite)).convert_alpha()
    # obter a área retangular da superfície
    img.get_rect()
    # colocando a image na coordenada (0,0) na superficie criada
    img.blit(sprite, (0, 0), ((frame*largura_sprite),
             (y_coordenada*altura_sprite), largura_sprite, altura_sprite))
    img = pygame.transform.scale(
        img, (largura_sprite*scale, altura_sprite*scale))
    # torna a superficie atras da sprite transparente
    img.set_colorkey(colour)
    return img

# Update das animações


def Atualizar_animacao(animation_list, line_list):
    global current_time, last_update, animation_cooldown, frame
    if current_time - last_update >= animation_cooldown:  # testa o intervalo do jogo com o tempo escolhido
        frame += 1
        last_update = current_time
    # Testa e volta para o inicio da lista da sprite
    if frame >= len(animation_list[line_list]):
        frame = 0
    return frame


def Criar_texto(mensagem, cor_texto, posicionamento, tamanho_do_texto):
    fonte = pygame.font.SysFont('arial', tamanho_do_texto, True, True)
    texto = fonte.render(mensagem, True, cor_texto)
    return tela.blit(texto, posicionamento)


def Colissao():
    global estado_vitima, pontos, velocidade_vitima, velocidade_morte, distancia_max
    if sprite_assassina.colliderect(sprite_vitima) and action == 2 and estado_vitima:
        barulho_colisao.play()
        estado_vitima = False
        pontos += 1
        testa_pontos = 3
        if pontos == testa_pontos:
            velocidade_morte += 1
            velocidade_vitima += 0.5
            distancia_max += 2
            testa_pontos += 3


def random(numero_inicial, numero_final):
    return randint(numero_inicial, numero_final)


def Reiniciar_jogo():
    global pontos, x_principal, x_vitima, x_morte, velocidade_morte, velocidade_vitima, distancia_max, morte_na_tela, estado_vitima, contador_morte
    pontos = 0
    x_principal = 0
    x_vitima = largura+10
    x_morte = largura-20
    velocidade_morte = 3
    velocidade_vitima = 1
    distancia_max = 20
    morte_na_tela = False
    estado_vitima = True
    contador_morte = 0


# Obtem o tempo em milissegundos(usado na função Atualizar_animacao() )
last_update = pygame.time.get_ticks()
animation_cooldown = 200

# Passa os quadros das sprites
frame = 0


# Quantidade de frames de cada sprite
animation_steps = [6, 8, 5, 4]


# Listas com os frames dos sprites
animation_list = []
action = 0

cont = 0

# Laço para a assassina e o pato
for animation in animation_steps:  # interando sobre o vetor
    temp_img_list = []
    temp_invisil = []
    for _ in range(animation):
        if animation == 5:
            temp_img_list.append(Obter_Sprite(
                sprite_sheet_Attack, cont, 0, 128, 128, 1.1, cor_preto))
            cont += 1
        if animation == 6:
            temp_img_list.append(Obter_Sprite(
                sprite_sheet_Idle, cont, 0, 128, 128, 1.1, cor_preto))
            cont += 1
        if animation == 8:
            temp_img_list.append(Obter_Sprite(
                sprite_sheet_walk, cont, 0, 128, 128, 1.1, cor_preto))
            cont += 1
        if animation == 4:
            temp_img_list.append(Obter_Sprite(
                sprite_sheet_Idle_invisivil, cont, 0, 128, 128, 1.1, cor_preto))
            cont += 1
    cont = 0
    animation_list.append(temp_img_list)

# Laço para a vitima
steps = [8]
animation_list_vitima = []
action_vitima = 0
for animation2 in steps:
    temp = []
    for i in range(animation2):
        if animation2 == 8:
            temp.append(Obter_Sprite(
                sprite_sheet_vitima, cont, 0, 128, 128, 1.1, cor_branco))
            cont += 1
    cont = 0
    animation_list_vitima.append(temp)


# Laço para a morte
etapas_morte = [12]
lista_animacao_morte = []
acao_morte = 0
for animation3 in etapas_morte:
    temp_lista_da_morte = []
    for _ in range(animation3):
        if animation3 == 12:
            temp_lista_da_morte.append(Obter_Sprite(
                sprite_morte, cont, 0, 900, 900, 1/8, cor_branco))
            cont += 1
    cont = 0
    lista_animacao_morte.append(temp_lista_da_morte)


# Laço para o pato
etapas_pato = [4]
animation_duck = []
action_duck = 0
for animicao4 in etapas_pato:
    temp_duck = []
    for _ in range(animicao4):
        temp_duck.append(Obter_Sprite(
            sprite_sheet_duck, 0, cont, 16, 16, 2, cor_preto))
        cont += 1
    cont = 0
    animation_duck.append(temp_duck)


# Coordenadas do pato
x_duck = largura+10
y_duck = random(100, 200)

# Coodernadas e velocidade da sprite principal
velocidade = 5
x_principal = 0
y_principal = 400


# Coodernada da vitima e velocidade
x_vitima = largura+10
y_vitima = 400
velocidade_vitima = 1
estado_vitima = True


# Coordenadas e velocidade da morte
x_morte = largura-100
y_morte = 450
velocidade_morte = 3
morte_na_tela = False
contador_morte = 0

passa_imagem = 0

pontos = 0
# ajustar os frame do jogo
relogio = pygame.time.Clock()

distancia_max = 20

# Estados das janelas do jogo
fim_de_jogo = False
jogo = False
menu = True

while menu:
    x_mouse, y_mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    x_botao_jogar = (largura//2)-90
    y_botao_jogar = (altura//2)-75

    x_botao_sair = (largura//2)-90
    y_botao_sair = (altura//2)+110

    x_instrucao = (largura//2)-90
    y_instrucao = (altura//2)+10

    tela.blit(tela_inicial, (0, 0))
    pygame.draw.rect(tela, (cor_preto),
                     (x_botao_jogar, y_botao_jogar, 180, 80))
    pygame.draw.rect(tela, (cor_preto), (x_instrucao, y_instrucao, 180, 80))
    pygame.draw.rect(tela, (cor_preto), (x_botao_sair, y_botao_sair, 180, 80))

    tela.blit(imagem_botao_jogar, ((largura//2)-100, (altura//2)-95))
    tela.blit(imagem_botao_controles, ((largura//2)-90, (altura//2)+10))
    tela.blit(imagem_botao_sair, ((largura//2)-90, (altura//2)+110))
    Criar_texto('ATENÇÃO! Esse jogo não incentiva e nem concorda com nenhum tipo de violência',
                (cor_branco), (240, 500), 10)
    # Testa se a posição do mouse coincide com o butão
    if click != (0, 0, 0):
        if x_mouse >= x_botao_jogar and x_mouse <= x_botao_jogar + 180 and y_mouse >= y_botao_jogar and y_mouse <= y_botao_jogar + 80:
            jogo = True
            menu = False
        if x_mouse >= x_botao_sair and x_mouse <= x_botao_sair + 180 and y_mouse >= y_botao_sair and y_mouse <= y_botao_sair + 80:
            Reiniciar_jogo()
            menu = False
            jogo = False
        if x_mouse >= x_instrucao and x_mouse <= x_instrucao + 180 and y_mouse >= y_instrucao and y_mouse <= y_instrucao + 80:
            Reiniciar_jogo()
            mensagem_intrucao = True
            while mensagem_intrucao:
                tela.blit(imagem_mensagem, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Reiniciar_jogo()
                        menu = False
                        jogo = False
                        mensagem_intrucao = False
                    if event.type == pygame.KEYDOWN:
                        mensagem_intrucao = False
                pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Reiniciar_jogo()
            menu = False
            jogo = False
    pygame.display.update()

    while jogo:
        # Controla a quantidade de quadros
        relogio.tick(30)
        # Detecta se algum evento ocorreu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reiniciar_jogo()
                jogo = False
            # Detecta se a tecla não esta pressionda e volta ao frame[0]
            if event.type == pygame.KEYUP:
                action = 0

        # Controles da assassina
        if pygame.key.get_pressed()[pygame.K_d] and action != 3:
            x_principal += velocidade
            action = 1
        if pygame.key.get_pressed()[pygame.K_a] and action != 3:
            x_principal -= velocidade
            action = 1
        if pygame.key.get_pressed()[pygame.K_k] and action != 3:
            action = 2
        if pygame.key.get_pressed()[pygame.K_q]:
            action = 3

        # Limita a sprite principal na tela e troca o background
        if x_principal > largura and passa_imagem == 0:
            x_principal = 0
            imagem_fundo, imagem_fundo2 = imagem_fundo2, imagem_fundo
            passa_imagem = 1
        elif x_principal > largura and passa_imagem == 1:
            x_principal = 0
            imagem_fundo2, imagem_fundo = imagem_fundo, imagem_fundo2
            passa_imagem = 0

        # Faz o pato andar horizontalmente
        if x_duck < 0:
            x_duck = largura
            y_duck = random(100, 200)

        if x_vitima < 0:
            x_vitima = largura + 10

        if x_morte < 0:
            x_morte = largura+10

        # obtem o tempo atual do jogo
        current_time = pygame.time.get_ticks()

        # Variaveis das sprites com as coordenadas da matriz
        imagem_sprite = animation_list[action][Atualizar_animacao(
            animation_list, action)]
        imagem_duck = animation_duck[action_duck][Atualizar_animacao(
            animation_duck, action_duck)]
        imagem_vitima = animation_list_vitima[action_vitima][Atualizar_animacao(
            animation_list_vitima, action_vitima)]
        imagem_morte = lista_animacao_morte[acao_morte][Atualizar_animacao(
            lista_animacao_morte, acao_morte)]

        # Coloca o cenário e as sprites na tela
        tela.blit(imagem_fundo, (0, 0))
        sprite_assassina = tela.blit(imagem_sprite, (x_principal, y_principal))
        tela.blit(imagem_duck, (x_duck, y_duck))

        # Condição para colocar a morte na tela
        if morte_na_tela:
            tela.blit(imagem_morte, (x_morte, y_morte))
            x_morte -= velocidade_morte

        # Testa se a vitima esta viva(True)
        if estado_vitima:
            sprite_vitima = tela.blit(imagem_vitima, (x_vitima, y_vitima))
            x_vitima -= velocidade_vitima

        # Quando a vitima morre sorteia o intervalo para desenhar a morte e a vitima de novo
        if not estado_vitima:
            intervalo_de_tempo_para_desenhar_na_tela = random(50, 100)
            # Tempo pra vitima aparecer de novo
            if intervalo_de_tempo_para_desenhar_na_tela > 50 and intervalo_de_tempo_para_desenhar_na_tela < 52:
                estado_vitima = True
                x_vitima = largura+10

        # Tempo pra morte aparecer de novo
        if contador_morte > 200:
            morte_na_tela = True
        if contador_morte > 200 and x_morte < 0:
            morte_na_tela = False
            contador_morte = 0

        Colissao()

        # Testa a proximidade da assassina com a morte and o keyup da tecla, se True dar Gamer Over
        if x_morte - x_principal < distancia_max and x_principal-x_morte < distancia_max and action != 3 and morte_na_tela:
            fim_de_jogo = True
            morte_na_tela = False
            while fim_de_jogo:
                tela.blit(imagem_fim_de_jogo, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Reiniciar_jogo()
                        fim_de_jogo = False
                        jogo = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            Reiniciar_jogo()
                            fim_de_jogo = False
                        if event.key == pygame.K_m:
                            Reiniciar_jogo()
                            fim_de_jogo = False
                            jogo = False
                            menu = True
                pygame.display.update()

        Criar_texto(f"Mortes:{pontos}", (255, 255, 255), (600, 50), 40)

        # Decrementando o x_duck
        x_duck -= 2
        contador_morte += 1

        # atualizando a tela
        pygame.display.update()
