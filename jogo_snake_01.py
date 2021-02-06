import pygame  # Importando pygame

pygame.init()

horizontal = 400
vertical = 300
velocidade = 5

janela = pygame.display.set_mode((800, 600))  # Definindo a variável que vai receber o display.
pygame.display.set_caption('Game Python')  # Nome da janela.

janela_on = True  # variável janela_on recendo valor booleano (True) Verdadeiro.

while janela_on:  # Enquanto variável janela_on for verdadeiro(True) Faça isso.
    pygame.time.delay(50)  # Delay para poder visualizar a janela.

    for event in pygame.event.get():  # Para o evento teclar(get)press.
        if event.type == pygame.QUIT:  # Se clicar em fechar a janela Faça:
            janela_on = False  # Passe a variável janela_on para Falso(False)
            # Seguindo a lógica a variável se tornando falsa ele sai do for.

    comandos = pygame.key.get_pressed()  # variável comandos, recebendo um comando de uma tecla.
    if comandos[pygame.K_UP]:  # Se a variável comandos receber a tecla para cima apertada faça.
        vertical -= velocidade

    if comandos[pygame.K_DOWN]:
        vertical += velocidade

    if comandos[pygame.K_RIGHT]:
        horizontal += velocidade

    if comandos[pygame.K_LEFT]:
        horizontal -= velocidade

    janela.fill((0, 0, 0))
    pygame.draw.circle(janela, (0, 255, 0), (horizontal, vertical), 50)  # Criação do objeto.
    pygame.display.update()  # Atualiza a tela para aparecer o objeto.

pygame.quit()
