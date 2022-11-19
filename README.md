# slackabet

[![PyPI version](https://img.shields.io/pypi/v/slackabet.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/slackabet)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/slackabet.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/slackabet)
[![PyPI downloads](https://img.shields.io/pypi/dm/slackabet.svg)](https://pypistats.org/packages/slackabet)
[![GitHub Actions status](https://github.com/hugovk/slackabet/workflows/Test/badge.svg)](https://github.com/hugovk/slackabet/actions)
[![codecov](https://codecov.io/gh/hugovk/slackabet/branch/main/graph/badge.svg)](https://codecov.io/gh/hugovk/slackabet)
[![GitHub](https://img.shields.io/github/license/hugovk/slackabet.svg)](LICENSE.txt)
[![Code style: Black](https://img.shields.io/badge/code%20style-Black-000000.svg)](https://github.com/psf/black)

Convert text into
[Slack alphabet emoji](https://slack.com/intl/en-fi/help/articles/206870177-Add-custom-emoji-to-your-workspace?cvosrc=spredfast.facebook.Product#emoji-packs).

## How to use

Install the package into your lovely codebase.

```bash
python3 -m pip install slackabet
```

```python
from slackabet import slackabet

print(slackabet("hi"))
```

Or on the command line:

```console
$ slackabet hi
:alphabet-None-h::alphabet-None-i:
$ sb hi
:alphabet-None-h::alphabet-None-i:
```

And that's it!

## Usage

```console
$ slackabet --help
usage: slackabet [-h] [-V] [-w] [-y] [-r] [--words] [--no-copy] text [text ...]

positional arguments:
  text           Text to convert to emoji

optional arguments:
  -h, --help     show this help message and exit
  -V, --version  show program's version number and exit
  -w, --white    White alphabet
  -y, --yellow   Yellow alphabet
  -r, --random   Randomly coloured letters
  --words        Randomly coloured words
  --no-copy      Do not copy to clipboard
```
