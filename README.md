[![Python application test with Github Actions](https://github.com/pavani-tvs88/functions_dec_2025/actions/workflows/main.yml/badge.svg)](https://github.com/pavani-tvs88/functions_dec_2025/actions/workflows/main.yml)

# functions_dec_2025

A Python project that extracts noun phrases from Wikipedia summaries using NLP techniques.

## Overview

This project demonstrates NLP functionality by searching Wikipedia for a given name and extracting noun phrases from the summary using TextBlob.

## Features

- Search Wikipedia for a given name
- Get Wikipedia summaries
- Extract noun phrases using TextBlob
- Command-line interface via Fire
- Automated testing and CI/CD with GitHub Actions

## Installation

Install dependencies using the Makefile:

```bash
make install
```

This will install all required packages from [requirements.txt](requirements.txt) and download TextBlob corpora.

## Usage

### Command Line

Run the script with a name to get noun phrases:

```bash
python wikiphrases.py "Golden State Warriors"
```

### Python Module

```python
from nlplogic.corenlp import get_phrases

phrases = get_phrases("Golden State Warriors")
print(phrases)
```

## Development

### Run Tests

```bash
make test
```

### Format Code

```bash
make format
```

### Lint Code

```bash
make lint
```

### Run All (Install, Lint, Test)

```bash
make all
```

## Project Structure

- `nlplogic/corenlp.py` - Core NLP functions
- `wikiphrases.py` - Command-line entry point
- `test_corenlp.py` - Unit tests
- `Makefile` - Development commands

## Dependencies

See [requirements.txt](requirements.txt) for full list of dependencies.
