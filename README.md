# codex.sh
CLI implementation of Codex for explaining shell commands

>**Note:** This script requires a valid OpenAI API key with access to the Codex (`code-davinci-002`) model.

## Build Instructions

### Build from source

1. Clone the repo
2. Install dependencies
    - `pip install -r requirements.txt`
3. Build the package
    - `python setup.py build`
4. Install the package
    - `python setup.py install`
5. Set up your API key
    - `echo "OPENAI_API_KEY=your_key_here" > .env`
6. Run the package
    - `codex`

### Install from PyPI

1. Set up your API key
    - `echo "OPENAI_API_KEY=your_key_here" > .env`
2. Install the package
    - `pip install codex.sh`
3. Run the package
    - `codex`

## Usage

```
usage: codex [-h] [-t TEMP] [-n NUM] [-w] query [query ...]

OpenAI Codex CLI cheatsheet

positional arguments:
  query                 query to search for

optional arguments:
  -h, --help            show this help message and exit
  -t TEMP, --temp TEMP  Codex model temperature (randomness)
  -n NUM, --num NUM     Number of codex predictions to return
  -w, --wordcount       Print word count of prompt file for debugging
                        purposes
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Thanks to [OpenAI](https://openai.com/) for making this possible!
* Thanks to [Rich](https://github.com/Textualize/rich) for CLI formatting!
