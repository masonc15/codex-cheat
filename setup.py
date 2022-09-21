from setuptools import setup

setup(
    name="codex-cli",
    version="0.1",
    py_modules=["main"],
    install_requires=[
        "rich",
        "pyperclip",
        "openai",
        "python-dotenv",
        "argparse",
    ],
    entry_points={"console_scripts": ["codex=main:main"]},
)
