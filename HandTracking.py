import cv2
import mediapipe as mp

def main():
    handTracking = HandTracking()
    handTracking.start(0) 

class HandTracking:
    
    #Funcao que inicia o rastreamento das mãos. Ele recebe como parâmetro o número da 
    #câmera a ser utilizada (0 para câmera padrão do computador) e cria um loop infinito 
    #para processar os frames do vídeo em tempo real.
    def start(self, cam):
        #Variavel que guarda a camera a ser utilizada:
        video = cv2.VideoCapture(cam)
        #Variavel que guarda a solution hands do MediaPipe, que possibilita trabalhar com o tracking de maos:
        hands = mp.solutions.hands
        #Configura a solution para detectar no maximo duas maos:
        Hands = hands.Hands(max_num_hands = 2)
        #Variavel que guarda a solution responsavel pela representação visual dos resultados do tracking:
        mpDraw = mp.solutions.drawing_utils

        while True:
            #Leitura do frame do video:
            success, frame = video.read()
            #Conversao do frame de BGR para RGB, para que possa ser processado:
            frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            #Variavel que guarda os resultados do processamento do frame:
            results = Hands.process(frameRGB)
            #Variavel que guarda os landmarks de cada mao processada:
            handsLandmarks = results.multi_hand_landmarks
            
            #Verifica se houve processamento de maos no frame, caso não, o loop segue normalmente:
            if handsLandmarks != None:
                #Variavel que guarda o numero total de dedos abertos nas maos:
                totalOpenFingers = 0
                #Laço que itera sobre os Landmarks (Objetos) de cada mao:
                for Landmarks in handsLandmarks:
                    #Variavel que gurda as coordenadas globais de cada ponto de tracking da mao:
                    worldKeyPoints = self.__worldKeyPoints(frame, Landmarks.landmark)
                    
                    #Verifica se a mao esta para cima, para garantir o funcionamento correto do codigo:
                    if self.__handUp(worldKeyPoints) == True:
                        #Desenha os pontos e as conexoes entre os pontos de tracking no frame:
                        mpDraw.draw_landmarks(frame, Landmarks, hands.HAND_CONNECTIONS)
                        #Atribuicao da quantidade de dedos abertos na mao analisada:
                        totalOpenFingers += self.__fingersOpen(worldKeyPoints)
                        
                #Adiciona um display no frame que mostra o numero total de dedos abertos:           
                self.__digitalDisplay(frame, totalOpenFingers)
            
            #Vizualização do frame com as informações adicionadas:
            cv2.imshow('Frame', frame)
            cv2.waitKey(1)
    
    #Uma função que converte as coordenadas especificas de tracking da mao em
    #coordenadas globais, referentes a posicoes reais de pixels no frame:         
    def __worldKeyPoints(self, frame, landmark):
        #Variaveis que guardam a altura e a largura do frame, respectivamente:
        height, width, _  = frame.shape
        #Lista temporaria que guarda as coordenadas globais:
        worldKeyPoints = []
        
        for cord in landmark:
            #Conversao dos eixos X e Y especificos para globais por meio da 
            #multiplicação pelas dimensoes do frame:
            x, y = int(cord.x * width), int(cord.y * height)
            #Adiciona a coordenada convertida na lista:
            worldKeyPoints.append((x, y))
        
        return worldKeyPoints

    #Funcao que verifica se a mao esta para cima, por meio de
    #comparacoes entre as coordenadas dos pontos:
    def __handUp(self, worldKeyPoints):
        if worldKeyPoints[0][1] < worldKeyPoints[2][1]:
            return False
        elif worldKeyPoints[1][1] < worldKeyPoints[17][1]:
            return False
        else:
            return True
    
    #Funcao que verifica quantos dedos da mao estão abertos,
    #por meio de comparacoes entre as coordenadas dos pontos:
    def __fingersOpen(self, worldKeyPoints):
        #Variavel temporaria que guarda o numero de dedos abertos:
        fingersOpen = 0
        #Lista que guarda o id das pontas dos dedos com eixo vertical:
        fingersTips = [8, 12, 16, 20]     
        for tip in fingersTips:
            if worldKeyPoints[tip][1] < worldKeyPoints[tip-2][1]:
                fingersOpen += 1
        
        if worldKeyPoints[4][0] < worldKeyPoints[17][0]:
            if worldKeyPoints[4][0] < worldKeyPoints[3][0]:
                fingersOpen += 1
        elif worldKeyPoints[4][0] > worldKeyPoints[3][0]:
            fingersOpen += 1
                
        return fingersOpen
    
    #Funcao que desenha um display digital no frame que exibe o 
    #numero de dedos abertos totais na imagem:
    def __digitalDisplay(self, frame, totalOpenFingers):
        #Desenha um retangulo verde:
        cv2.rectangle(frame, (0, 0), (220, 120), (0, 200, 0), -1)
        #Desenha a quantidade de dedos abertos:
        cv2.putText(frame, str(totalOpenFingers), (20, 100), cv2.FONT_HERSHEY_DUPLEX, 4, (255, 255, 255), 5)

if __name__ == "__main__":
    main()
