
import pygame, time

from pygame.locals import *
pygame.init() # pygame 라이브러리를 로드 한다.

display_screen = pygame.display.set_mode((815,85)) # 디스플레이 창 크기 설정

pygame.display.set_caption("MINI PYTHON PIANO") # 디스플레이 이름

pygame.mouse.set_visible(1) # 마우스 커서 활성화

white = (255, 255, 255) # 색 지정

black = (0, 0, 0)

display_font = pygame.font.SysFont("arialrounded", 20) #폰트 지정


text = (u"키보드 1~8까지 꾸욱 눌러 보세요. \n Esc키를 누르면 종료 됩니다.") # 유니코드 인코딩으로 텍스트 설계

display_text = display_font.render(text, True, black, white) # 설계한 텍스트를 렌더링한다.

display_text_vis = display_text.get_rect() # 디스플레이에 표시

display_text_vis.center = (340, 34) # # 디스플레이에 표시되는 위치 설정


def mp(file):  # 소리 파일을 불러 오는 파일을 불러오는 함수
    pygame.mixer.music.load(file)

    while True :

        display_screen.fill(white) # 디스플레이의 배경색 지정

        display_screen.blit(display_text, display_text_vis) # 디스플레이에 텍스트 표시

        pygame.display.update() # 디스플레이를 계속 업데이트 한다.

        for event in pygame.event.get(): # 이벤트 시작

            if(event.type == pygame.KEYDOWN): # 키를 눌렀을 경우 mp함수가 음악 파일을 불러오고 pygame 모듈이 재생
                if(event.key == pygame.K_1):

                    mp("/home/seo/project/1.mp3")
                    pygame.mixer.music.play()

                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_2):

                        mp("/home/seo/project/2.mp3")
                        pygame.mixer.music.play()

                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_3):

                        mp("/home/seo/project/3.mp3")
                        pygame.mixer.music.play()

                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_4):

                        mp("/home/seo/project/4.mp3")
                        pygame.mixer.music.play()

                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_5):

                        mp("/home/seo/project/5.mp3")
                        pygame.mixer.music.play()

                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_6):

                        mp("/home/seo/project/6.mp3")
                        pygame.mixer.music.play()

                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_7):

                        mp("/home/seo/project/7.mp3")
                        pygame.mixer.music.play()

                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_8):

                        mp("/home/seo/project/8.mp3")
                        pygame.mixer.music.play()

                if(event.type == pygame.KEYDOWN): # 키가 올라갔을때(땠을 때) 재생을 중단 시킴


                    pygame.mixer.music.stop()

                
                if(event.type == pygame.KEYDOWN): # esc 키를 누르고 땠을 때 종료 실행
                    if(event.key == pygame.K_ESCAPE):

                        pygame.quit()

                if(event.type == pygame.KEYDOWN): # 창을 종료 했을 때 정상 종료 수행 
                    pygame.quit()



            