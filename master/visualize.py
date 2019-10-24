import pygame
#from event_handler import EventHandler


class VisualizeWarehouse:
    def __init__(self):
        self.surface = None
        self.height = 500
        self.width = 500
        self.screen_buffer = 10
        self.board_size = False
        self.item_list = None
        self.height_segment = None
        self.width_segment = None
        self.create_screen()

    @staticmethod
    def find_starting_index(board, item_id):
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == item_id:
                    return j, i

    @staticmethod
    def find_full_box_size(board, item_id, width_index, height_index):
        height = 0
        width = 0
        for i in range(height_index, len(board)):
            if board[i][width_index] == item_id:
                height += 1
        for i in range(width_index, len(board[0])):
            if board[height_index][i] == item_id:
                width += 1
        return width, height

    def create_screen(self):
        pygame.init()
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((195, 195, 195))

    def form_display(self, board, item_list):
        self.item_list = item_list
        self.height_segment = ((self.height - self.screen_buffer * 2) / len(board))
        self.width_segment = ((self.width - self.screen_buffer * 2) / len(board[0]))
        self.create_item_rect(board=board, item_list=item_list)

    def create_item_rect(self, board, item_list):
        for item in item_list:
            #if item.warehouse_rect is None:
            width_index, height_index = self.find_starting_index(board, item.item_id)
            width, height = self.find_full_box_size(board, item.item_id, width_index, height_index)
            item_rect = pygame.Rect(width_index * self.width_segment + self.screen_buffer,
                                    height_index * self.height_segment +
                                    self.screen_buffer, width * self.width_segment, height * self.height_segment)
            item.warehouse_rect = item_rect

    def draw_display(self, match_id=None):
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((195, 195, 195))
        border_color = (0, 0, 0)
        for item in self.item_list:
            color = (243, 214, 96)
            if match_id is not None:
                if item.item_id == match_id:
                    color = (46, 122, 208)
            self.surface.fill(border_color, item.warehouse_rect)
            self.surface.fill(color, item.warehouse_rect.inflate(-2, -2))
        return self.surface

'''
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
            pass
            # vis.update_display(board=board1, num_of_items=4)
            # vis.update_display(board=board2, num_of_items=5)
'''