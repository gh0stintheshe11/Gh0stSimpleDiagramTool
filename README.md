# SimpleDiagramTool

`SimpleDiagramTool` is a Python class that provides a simple interface for creating diagrams using matplotlib. It allows you to add blocks, lines, and arrows to a diagram, and then display the diagram.

## Installation

This tool requires matplotlib to be installed. You can install it using pip:

```bash
pip install matplotlib
```

## Usage

First, import the `SimpleDiagramTool` class:

```python
from simple_diagram_tool import SimpleDiagramTool
```

Then, create an instance of the class, specifying the length and width of the diagram:

```python
diagram = SimpleDiagramTool(10, 10)
```

### Adding a block

You can add a block to the diagram using the `add_block` method. This method takes the following parameters:

- `position`: A tuple `(x, y)` specifying the bottom left corner of the block.
- `size`: A tuple `(width, height)` specifying the size of the block.
- `label`: A string label for the block.
- `boundary_color`: (optional) The color of the block boundary. Default is 'r' (red).
- `text_size`: (optional) The size of the label text. Default is 10.

```python
diagram.add_block((1, 1), (2, 2), 'Block 1', boundary_color='b', text_size=12)
```

### Adding a line

You can add a line to the diagram using the `add_line` method. This method takes the following parameters:

- `start_pos`: A tuple `(x, y)` specifying the start position of the line.
- `end_pos`: A tuple `(x, y)` specifying the end position of the line.
- `line_color`: (optional) The color of the line. Default is 'k' (black).

```python
diagram.add_line((1, 1), (3, 3), line_color='g')
```

### Adding an arrow

You can add an arrow to the diagram using the `add_arrow` method. This method takes the following parameters:

- `start_pos`: A tuple `(x, y)` specifying the start position of the arrow.
- `end_pos`: A tuple `(x, y)` specifying the end position of the arrow.
- `arrow_color`: (optional) The color of the arrow. Default is 'k' (black).

```python
diagram.add_arrow((1, 1), (3, 3), arrow_color='r')
```

### Displaying the diagram

Finally, you can display the diagram using the `show` method:

```python
diagram.show()
```

## Error Handling

If you try to add an element that is out of the bounds of the diagram, a `ValueError` will be raised. Make sure that all elements fit within the specified length and width of the diagram.

## Examples

Here's a complete example that creates a diagram with a block, a line, and an arrow:

```python
from simple_diagram_tool import SimpleDiagramTool

diagram = SimpleDiagramTool(10, 10)
diagram.add_block((1, 1), (2, 2), 'Block 1', boundary_color='b', text_size=12)
diagram.add_line((1, 1), (3, 3), line_color='g')
diagram.add_arrow((1, 1), (3, 3), arrow_color='r')
diagram.show()
```

This will create a 10x10 diagram with a blue block labeled 'Block 1' at position (1, 1) with size (2, 2), a green line from (1, 1) to (3, 3), and a red arrow from (1, 1) to (3, 3).