import sys
import pygame
ancho=700
alto=480
color=(0,64,0)
def main():
  pygame.init()
  pantalla=pygame.display.set_mode((ancho,alto),0,32)
  circulo=pygame.image.load('Warrior.png')
  pygame.display.set_caption("Mi Primer ejemplo")
  arear=circulo.get_rect()
  desplazar=[3,3]
  while True:
      pantalla.fill(color)
      arear.x = arear.x  + desplazar[0]
      arear.y=arear.y + desplazar[1]
      if arear.top<0:
        desplazar[1]=-desplazar[1]
      if arear.right> ancho:
        desplazar[0]=-desplazar[0]
      if arear.bottom>alto:
        desplazar[1]=desplazar[-1]
      if arear.left<0:
        desplazar[0]=-desplazar[0]
      pantalla.blit(circulo,arear)
      pygame.display.flip()
      for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
          sys.exit()
if __name__ == '__main__':
  main()
