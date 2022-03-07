import pygame               # Importa pygame
from pygame.locals import * # Importa e copia tudo do pygame.locals para o script
import numpy as np          # Importa a bliblioteca numpy (Numerical Python) - trabalho com arrays (matrizes)
import pygame_menu          # Importa a a biblioteca para a criação de menus

pygame.init()               # Inicializa todos os módulos pygame importados

def start():                # Função do jogo em si

    class Drone:            # Conjunto de funções que envolvem o drone

        def __init__(self):     # Criando objeto da classe
            self.m = 0.250      # Massa [kg]
            self.g = 9.81       # Gravidade [m/s²]
            self.V_max = 15000  # Velocidade máxima [rpm]
            self.V_min = 0      # Velocidade mínima [rpm]

        def gravidade(self):            # Gravidade
            v = self.m * self.g * np.sin(np.pi/2)
            return v

        def v_y(self, accelerate, fi):  # Velocidade eixo Y
            v = self.m * accelerate * np.sin(fi)*2 
            
            if v >= self.V_max:         # Condição de limite máximo para velocidade
                v = self.V_max
            
            elif v <= self.V_min:       # Condição de limite mínimo para velocidade
                v = self.V_min
            return -v

        def v_x(self, accelerate, fi):  # Velocidade eixo X
            forca = drone.v_y(accelerate, pi/2)*2
            v = np.cos(fi) * forca
            return v


    if __name__ == "__main__":                      # Permite a execução do código somente com a importação dos módulos
        pygame.init()                               # Inicialização do pygame
        clock = pygame.time.Clock()                 # Inicialização do tempo no jogo
        screen = pygame.display.set_mode((900,550)) # Inicialização da janela

        bg = pygame.image.load(r"bg_mario.jpg")                             # Carrega a imagem de fundo
        drn = pygame.image.load(r"drone2.png")                              # Carrega a imagem do drone
        pygame.display.set_caption('Trabalho SEMB II - Simulação de Drone') # Nome da janela
        pygame.display.flip()                                               # Atualiza o conteúdo de todo o display
        drone = Drone()
        autonomo = False                                                    # Modo autônomo desativado

        # Parâmetros
        pi = np.pi              # Utilização de pi para matrizes
        fi = pi/2               # Angulação inicial 90º
        x = 450 - (81/2)        # Posição inicial em X e centraliza o drone
        y = 300                 # Posição inicial em Y
        aceleracao = 0          # Inicializa nulo
        forca_y = 0             # Inicializa nulo (uma das forças aplicadas no sistema)
        y1 = 0                  # Inicializa nulo
        x1 = 0                  # Inicializa nulo
        erro_acumulado_y = 0    # Inicializa nulo
        erro_acumulado_x = 0    # Inicializa nulo
        iteracao = 0            # Inicializa nulo
        erro_anterior = 0       # Inicializa nulo
        derivativo_x = 0        # Inicializa nulo
        
        running = True          # Código em execução
        while running:          # Condição para enquanto o programa está em execução:

            clock.tick(60)                                                      # Nº máximo de quadros por segundo
            screen.blit(bg, (0,0))                                              # Background
            screen.blit(pygame.transform.rotate(drn, -np.degrees(fi)), (x, y))  # Posição inicial do drone
            key = pygame.key.get_pressed()
            
            # Encerramento o programa
            for event in pygame.event.get():                            # Evento
                if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:   # Se o evento for do tipo QUIT (botão "Fechar" ou "Esc")
                    running = False                                     # Fecha o jogo

            # Movimentação lateral
            if key[pygame.K_LEFT]:              # Clique do botão [<-]
                fi -= pi/180                    # Ângulo decresce para a direita
                autonomo = False                # Modo autônomo desativado

            elif key[pygame.K_RIGHT]:           # Clique do botão [->]
                fi += pi/180                    # Ângulo decresce para a esquerda
                autonomo = False                # Modo autônomo desativado

            # Movimentação de altura
            if key[pygame.K_UP]:                # Ao apertar [^]
                aceleracao += 0.5               # Decresce a posição no eixo vertical
                autonomo = False                # Modo autônomo desativado

            elif autonomo == False:             # Quando não é aperdado o botão [^] e o modo autônomo permanece desativado
                aceleracao -= 0.2               # Decresce a posição no eixo vertical para baixo
                autonomo = False                # Modo autônomo desativado

            # Comando do WayPoint
            if event.type == MOUSEBUTTONDOWN:   # Se o evento for clique do mouse
                x1,y1 = pygame.mouse.get_pos()  # Transforma as posições X e Y na posiçao do clique
                x1 = x1 - (81/2)                # Corrige a posição X em metade do tamanho do drone (para centralizá-lo)
                iteracao = 0                    # Interação é zero
                autonomo = True                 # Modo autônomo é ativado
            
            if autonomo == True:                                            # Quando o modo autônomo é verdadeiro
                iteracao += 1                                               # A interação é incrementada em 1
                erro_x = (x - x1)                                           # Erro em X é a diferença entre a posição atual e a do clique
                erro_y = (y - y1)                                           # Erro em Y é a diferença entre a posição atual e a do clique
                erro_acumulado_y += erro_y * iteracao                       # Encontrando o erro acumulado em Y
                erro_acumulado_x += ((-erro_x / 1800) / 90) * iteracao      # Encontrando o erro acumulado em X
                derivativo_x = (erro_acumulado_x - erro_anterior)/iteracao  # Encontrando o derivativo em X
                erro_anterior = erro_acumulado_x                            # Erro anterior
                aceleracao = (erro_acumulado_y * 0.000005) + (erro_y * 0.1) # Aceleração
                fi = erro_acumulado_x * 0.5 + derivativo_x * 5000           # Angulação

            # Limites do Mapa
            if y <= 5:      # Limite superior
                y = 5

            elif y >= 445:  # Limite inferior
                y = 445

            if x <= 0:      # Limite lateral esquerda
                x = 0

            elif x >= 805:  # Limite lateral direita
                x = 805

            # Limitações do drone
            if fi <= pi/4:          # Fixa o valor mínimo de angulação do giro do drone
                fi = pi/4

            elif fi >= 3*pi/4:      # Fixa o valor máximo de angulação do giro do drone
                fi = 3*pi/4

            if aceleracao >= 10:    # Fixa o valor máximo de aceleração
                aceleracao = 10

            elif aceleracao <= -10: # Fixa o valor mínimo de aceleração
                aceleracao = -10

            # Forças aplicadas no sistema
            x += drone.v_x(aceleracao, fi)
            forca_y = drone.v_y(aceleracao, fi)
            y = forca_y + y
            y += drone.gravidade()

            pygame.display.update() # Atualiza o display (não necessariamente por inteiro)

m = pygame.display.set_mode((900, 562))                                                     # Define o tamanho da tela do menu
menu = pygame_menu.Menu('Menu Principal', 900, 562, theme=pygame_menu.themes.THEME_DARK)    # Abre o Menu Principal, com tamanho e tema
menu.add.button('Iniciar jogo', start)                                                      # Botão "Iniciar Jogo"
menu.add.button('Sair', pygame_menu.events.EXIT)                                            # Botão "Sair"
menu.mainloop(m)                                                                            # Loop no menu