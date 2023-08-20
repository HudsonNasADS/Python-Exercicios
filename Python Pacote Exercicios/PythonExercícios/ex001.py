import turtle

def desenhar_arvore(tamanho, niveis):
    if niveis == 0:
        return

    # Desenhar tronco
    if niveis < 3:
        turtle.color('saddle brown')
    else:
        turtle.color('brown')
    turtle.pensize(niveis)
    turtle.forward(tamanho)
    turtle.right(20)

    # Desenhar galhos direitos
    turtle.color('green')
    turtle.forward(tamanho * 0.6)
    desenhar_arvore(tamanho * 0.6, niveis - 1)

    # Recuar e voltar para a posição anterior
    turtle.backward(tamanho * 0.6)
    turtle.left(40)

    # Desenhar galhos esquerdos
    turtle.color('green')
    turtle.forward(tamanho * 0.6)
    desenhar_arvore(tamanho * 0.6, niveis - 1)

    # Recuar e voltar para a posição anterior
    turtle.backward(tamanho * 0.6)
    turtle.right(20)
    turtle.backward(tamanho)

def desenhar_flores():
    turtle.up()
    turtle.goto(0, 200)
    turtle.down()
    turtle.color('red')

    for _ in range(36):
        turtle.forward(10)
        turtle.backward(10)
        turtle.right(10)

# Configurações da tartaruga
tamanho_tronco = 100
niveis_arvore = 7

# Configurações da janela
largura = 800
altura = 600

# Inicialização da tartaruga
turtle.setup(width=largura, height=altura)
turtle.speed(0)

# Movendo a tartaruga para a posição inicial
turtle.penup()
turtle.goto(0, -altura/2 + 50)
turtle.pendown()

# Personalização da tartaruga
turtle.left(90)

# Chamada para desenhar a árvore
desenhar_arvore(tamanho_tronco, niveis_arvore)

# Chamada para desenhar flores no topo
desenhar_flores()

# Fechando a janela ao clicar nela
turtle.exitonclick()