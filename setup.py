from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="Gh0stSimpleDiagramTool",
    version="0.0.4",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
    ],
    author="gh0stintheshe11",
    author_email="gh0stintheshe11@gmail.com",
    description="A simple diagram drawing tool",
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important for Markdown
    license="MIT",
    keywords="diagram flowchart matplotlib",
    url="https://github.com/gh0stintheshe11/gh0st-SImpleDiagramTool",
)
