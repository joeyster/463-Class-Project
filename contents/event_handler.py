import sys
import pygame


class EventHandler:

    @staticmethod
    def check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pass # save WS to file
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                    pass # save WS to file
