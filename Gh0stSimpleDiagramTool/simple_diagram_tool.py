import matplotlib.pyplot as plt
import matplotlib.patches as patches

class SimpleDiagramTool:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.fig, self.ax = plt.subplots(figsize=(self.length, self.width))
        self.ax.set_xlim(0, self.length)
        self.ax.set_ylim(0, self.width)
        
    def _is_out_of_bounds(self, position, size=(0, 0)):
        x, y = position
        w, h = size
        if x < 0 or y < 0 or x + w > self.length or y + h > self.width:
            raise ValueError("Element is out of the plot bounds.")

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
        self._is_out_of_bounds(position, size)
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
        self._is_out_of_bounds(start_pos)
        self._is_out_of_bounds(end_pos)
        self.ax.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], color=line_color)

    def add_arrow(self, start_pos, end_pos, arrow_color='k'):
        """
        Adds an arrow between two points.

        Parameters:
        - start_pos: A tuple (x, y) for the start position of the arrow.
        - end_pos: A tuple (x, y) for the end position of the arrow.
        - arrow_color: Color of the arrow.
        """
        self._is_out_of_bounds(start_pos)
        self._is_out_of_bounds(end_pos)
        self.ax.annotate("", xy=end_pos, xycoords='data', xytext=start_pos, textcoords='data',
                         arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color=arrow_color))

    def show(self):
        """
        Displays the diagram.
        """
        plt.axis('off')
        plt.show()
