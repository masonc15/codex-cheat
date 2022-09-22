from setuptools import setup

setup(
    name="codex-sh",
    version="0.1.0",
    py_modules=["main"],
    install_requires=[
        "rich",
        "pyperclip",
        "openai",
        "argparse",
    ],
    entry_points={"console_scripts": ["codex=main:main"]}
)
