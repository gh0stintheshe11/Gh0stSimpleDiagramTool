from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="gh0st-SimpleDiagramTool",
    version="0.1",
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
