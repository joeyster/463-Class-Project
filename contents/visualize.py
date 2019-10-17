import pygame
from event_handler import EventHandler


class VisualizeWarehouse:
    def __init__(self):
        self.screen = None
        self.height = 500
        self.width = 500
        self.screen_buffer = 10
        self.board_size = False
        self.create_screen()

    @staticmethod
    def find_starting_index(board, item_ord):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if ord(board[i][j]) == item_ord:
                    return j, i

    @staticmethod
    def find_full_box_size(board, item_ord, width_index, height_index):
        height = 0
        width = 0
        for i in range(height_index, len(board)):
            if ord(board[i][width_index]) == item_ord:
                height += 1
        for i in range(width_index, len(board[0])):
            if ord(board[height_index][i]) == item_ord:
                width += 1
        return width, height

    def create_screen(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption("Workshop Display")
        pygame.display.flip()

    def update_display(self, board, num_of_items):
        height_segment = ((self.height - self.screen_buffer * 2) / len(board))
        width_segment = ((self.width - self.screen_buffer * 2) / len(board[0]))
        color = (243, 214, 96)
        border_color = (0, 0, 0)
        item_ord = 65
        for _ in range(0, num_of_items):
            width_index, height_index = self.find_starting_index(board, item_ord)
            width, height = self.find_full_box_size(board, item_ord, width_index, height_index)
            box_size = pygame.Rect(width_index * width_segment + self.screen_buffer, height_index * height_segment +
                                   self.screen_buffer, width * width_segment, height * height_segment)
            self.screen.fill(border_color, box_size)
            self.screen.fill(color, box_size.inflate(-2, -2))
            item_ord += 1
        pygame.display.flip()


if __name__ == "__main__":
    vis = VisualizeWarehouse()
    vis.create_screen()

    event_handler = EventHandler()
    board1 = [['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C'],
              ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C'],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'D'],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    board2 = [['A', 'A', ' ', 'E', ' ', 'B', 'B', 'B', 'B', 'C'],
              ['A', 'A', ' ', 'E', ' ', 'B', 'B', 'B', 'B', 'C'],
              ['A', 'A', ' ', 'E', ' ', ' ', ' ', ' ', ' ', 'D'],
              ['A', 'A', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' '],
              ['A', 'A', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' '],
              ['A', 'A', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' ']]

    while True:
        if event_handler.check_events():
            # vis.update_display(board=board1, num_of_items=4)
            vis.update_display(board=board2, num_of_items=5)
