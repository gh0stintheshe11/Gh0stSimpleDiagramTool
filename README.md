## Quick Start Guide

Here's how to create a simple diagram with a block, a line, and an arrow:

```python
from gh0st_SimpleDiagramTool import SimpleDiagramTool

tool = SimpleDiagramTool()
tool.add_block((0.1, 0.1), (0.2, 0.1), "Start", boundary_color='blue', text_size=12)
tool.add_line((0.3, 0.15), (0.4, 0.15), line_color='green')
tool.add_arrow((0.4, 0.15), (0.5, 0.15), arrow_color='red')
tool.show()
