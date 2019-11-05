import pygame


class VisualizeWarehouse:
    """Display the visualization of the warehouse using pygame."""
    def __init__(self):
        self.surface = None
        self.height = 500
        self.width = 500
        self.screen_buffer = 10
        self.rectangle_list = []
        self.board_size = False
        self.item_list = None
        self.height_segment = None
        self.width_segment = None
        self.create_screen()

    @staticmethod
    def find_starting_index(board, count):
        """Locate the starting index of a specific item in the warehouse.+"""
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == str(count):
                    return j, i

    @staticmethod
    def find_full_box_size(board, width_index, height_index, count):
        """Find the total size of an item based on the starting indices."""
        height = 0
        width = 0
        for i in range(height_index, len(board)):
            if board[i][width_index] == str(count):
                height += 1
        for i in range(width_index, len(board[0])):
            if board[height_index][i] == str(count):
                width += 1
        return width, height

    def create_screen(self):
        """Initialize the pygame surface."""
        pygame.init()
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((195, 195, 195))

    def form_display(self, board, item_list):
        """Initialize the parameters that are needed to display the board nicely."""
        self.item_list = item_list
        self.height_segment = ((self.height - self.screen_buffer * 2) / len(board))
        self.width_segment = ((self.width - self.screen_buffer * 2) / len(board[0]))
        self.create_item_rect(board=board, item_list=item_list)

    def create_item_rect(self, board, item_list):
        """Create the pygame rectangles of each item that are being displayed."""
        count = 1
        self.rectangle_list = []
        for _ in item_list:
            width_index, height_index = self.find_starting_index(board=board, count=count)
            width, height = self.find_full_box_size(board=board, width_index=width_index, height_index=height_index,
                                                    count=count)
            item_rect = pygame.Rect(width_index * self.width_segment + self.screen_buffer,
                                    height_index * self.height_segment +
                                    self.screen_buffer, width * self.width_segment, height * self.height_segment)
            self.rectangle_list.append(item_rect)
            count = count + 1

    def draw_display(self, match_id=None):
        """Draw the item rectangles onto the pygame surface."""
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((195, 195, 195))
        border_color = (0, 0, 0)
        for i in range(len(self.item_list)):
            color = (243, 214, 96)
            if match_id is not None:
                if self.item_list[i].item_id == match_id:
                    color = (46, 122, 208)
            self.surface.fill(border_color, self.rectangle_list[i])
            self.surface.fill(color, self.rectangle_list[i].inflate(-2, -2))
        return self.surface


'''
if __name__ == "__main__":
    """Main method for testing."""
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
