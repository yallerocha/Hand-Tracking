# Contador de Dedos com OpenCV e MediaPipe

👉 Este é um exemplo de um programa Python que utiliza as bibliotecas OpenCV e MediaPipe para rastrear e contar os dedos das mãos em um fluxo de vídeo da webcam. O programa detecta as mãos no vídeo, calcula o número de dedos abertos e exibe esse número em um display digital no canto superior esquerdo do vídeo.

## Pré-Requisitos

- ✅ Python
- ✅ OpenCV (cv2)
- ✅ MediaPipe

## Como Usar

![Imagem 2 - Sobre o Projeto](assets/print2.jpg)

1. Certifique-se de que você tenha as bibliotecas OpenCV e MediaPipe instaladas. Você pode instalá-las usando o `pip`:

   ```bash
   pip install opencv-python-headless mediapipe
   ```
2. Execute o código Python fornecido no seu ambiente Python.

    ```bash
    python HandTracking.py
    ```
3. O programa iniciará a câmera padrão do seu computador e começará a rastrear as mãos em tempo real.

4. O número de dedos abertos é exibido em um display digital no canto superior esquerdo do vídeo.

## Como Funciona

✅ Ele inicia a câmera e começa a capturar frames de vídeo.

✅ Utiliza o MediaPipe para detectar as mãos nos frames do vídeo.

✅ Calcula as coordenadas dos pontos de referência das mãos (landmarks) e converte essas coordenadas em coordenadas globais no frame.

✅ Verifica se a mão está voltada para cima para garantir a precisão do rastreamento.

✅ Conta quantos dedos estão abertos com base na posição dos landmarks das mãos.

✅ Exibe o número de dedos abertos em um display digital no vídeo.
