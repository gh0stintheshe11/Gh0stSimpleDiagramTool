import matplotlib.pyplot as plt
import matplotlib.patches as patches

class SimpleDiagramTool:
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def add_block(self, position, size, label, boundary_color='r', text_size=10):
        """
        Adds a rectangular block to the diagram.

        Parameters:
        - position: A tuple (x, y) for the bottom left corner of the block.
        - size: A tuple (width, height) of the block.
        - label: A string label for the block.
        - boundary_color: Color of the block boundary.
        - text_size: Size of the label text.
        """
        rect = patches.Rectangle(position, *size, linewidth=1, edgecolor=boundary_color, facecolor='none')
        self.ax.add_patch(rect)
        self.ax.text(position[0] + size[0] / 2, position[1] + size[1] / 2, label, 
                     ha='center', va='center', fontsize=text_size)

    def add_line(self, start_pos, end_pos, line_color='k'):
        """
        Adds a line between two points.

        Parameters:
        - start_pos: A tuple (x, y) for the start position of the line.
        - end_pos: A tuple (x, y) for the end position of the line.
        - line_color: Color of the line.
        """
        self.ax.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], color=line_color)

    def add_arrow(self, start_pos, end_pos, arrow_color='k'):
        """
        Adds an arrow between two points.

        Parameters:
        - start_pos: A tuple (x, y) for the start position of the arrow.
        - end_pos: A tuple (x, y) for the end position of the arrow.
        - arrow_color: Color of the arrow.
        """
        self.ax.annotate("", xy=end_pos, xycoords='data', xytext=start_pos, textcoords='data',
                         arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color=arrow_color))

    def show(self):
        """
        Displays the diagram.
        """
        self.ax.set_aspect('equal')
        plt.axis('off')
        plt.show()
