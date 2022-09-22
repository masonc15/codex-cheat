from setuptools import setup

setup(
    name="codex.sh",
    version="0.1",
    py_modules=["main"],
    install_requires=[
        "rich",
        "pyperclip",
        "openai",
        "python-dotenv",
        "argparse",
    ],
    data_files=[("prompts.txt", ["prompts.txt"])],
    entry_points={"console_scripts": ["codex=main:main"]}
)
