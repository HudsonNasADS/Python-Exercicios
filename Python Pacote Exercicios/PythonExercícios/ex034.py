import cv2

def convert_image_to_sketch(image_path):
    # Carrega a imagem usando o OpenCV
    image = cv2.imread(image_path)

    # Converte a imagem para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplica um desfoque à imagem em escala de cinza usando o filtro Gaussiano
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Detecta as bordas na imagem desfocada usando o operador de Sobel
    edges = cv2.Canny(blurred_image, 30, 150)

    # Inverte as cores da imagem de bordas
    inverted_edges = cv2.bitwise_not(edges)

    return inverted_edges

# Caminho da imagem de entrada
input_image_path = "caminho/para/imagem.jpg"

# Chama a função para converter a imagem em um desenho
sketch = convert_image_to_sketch(input_image_path)

# Mostra a imagem de saída
cv2.imshow("Desenho", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
