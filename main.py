# -*- coding: utf-8 -*-

import pygame
from constants import *
from robot import *


# https://gm0.org/en/latest/docs/software/odometry.html


def main():
    pygame.init()
    screen = pygame.display.set_mode((FULL_MAP_WIDTH + CON_WIDTH,
                                      FULL_MAP_HEIGHT))
    pygame.display.set_caption(' Robot  |  Odometría ')
    font = pygame.font.SysFont("Ubuntu", 18, False, False)
    imagen_robot = cargar_robot()

    robot = Robot()
    screen.fill(COLOR_BLANCO)
    # robot.dibujar_fondo(screen)
    robot.dibujar_robot(screen, imagen_robot)
    enc_der, enc_izq = 0, 0

    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                enc_der, enc_izq = 0, 0
                # Movimiento continuo hacia delante. Tecla W.
                if event.key == pygame.K_w:
                    enc_der, enc_izq = robot.movimiento_W()
                # Movimiento continuo hacia atrás. Tecla S.
                if event.key == pygame.K_s:
                    enc_der, enc_izq = robot.movimiento_S()
                # Movimiento de giro sobre si mismo a la izquierda. Tecla A.
                if event.key == pygame.K_a:
                    enc_der, enc_izq = robot.movimiento_A()
                # Movimiento de giro sobre si mismo a la derecha. Tecla D.
                if event.key == pygame.K_d:
                    enc_der, enc_izq = robot.movimiento_D()
                # Movimiento continuo con desviación izquierda. Tecla Q.
                if event.key == pygame.K_q:
                    enc_der, enc_izq = robot.movimiento_Q()
                # Movimiento continuo con desviación derecha. Tecla E.
                if event.key == pygame.K_e:
                    enc_der, enc_izq = robot.movimiento_E()
                # Tecla incorrecta = 0.
                # robot.odo_calc(enc_der, enc_izq)  # Revisar

        # robot.dibujar_fondo(screen)
        robot.odo_calc(enc_der, enc_izq)  # Revisar
        robot.dibujar_robot(screen, imagen_robot)
        clock.tick(FPS)
        pygame.display.flip()

    pygame.quit()


def cargar_robot():
    """
        Carga de la imagen del robot.
    """
    robot = pygame.transform.scale(pygame.image.load("assets/car_top_view.png"),
                           (FULL_MAP_WIDTH / 10, FULL_MAP_HEIGHT / 10))
    rotada = robot
    rect = rotada.get_rect(center=(400, 400))
    return robot

if __name__ == '__main__':
    main()