
<div align="center" float="left"><span><img src="affinity.png" width="100" height="100"></span><h1>Affinity</h1></div>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://badgen.net/github/license/Naereen/Strapdown.js)](https://github.com/grqphical07/Affinity/blob/master/LICENSE)

Affinity is a command line HTTP client similar to curl but made to be simplistic and easy-to-use. Affinity is written in 100% pure python

## Installation

1. Download the source code and extract it
2. Run: 
```bash
$ pip install .
```

## Quick Start Guide

To make a simple GET request to the [Github API](https://api.github.com/) you just need to run:
```bash
$ affinity https://api.github.com/
```

Now when you run that you will see:
```bash
200 GET https://api.github.com/
```

To see the data sent from the request add the *-o* flag to output the results to the console
```bash
$ affinity https://api.github.com/ -o
```

If you want to learn more either use the docs or run ```affinity -h```

To view docs run ```.\docs\make html``` on windows or ```docs/make html``` on bash

## Changelog

### 1.1.0
- Removed output to file option. Just use your shell's file redirect syntax
- Allowed for using JSON files in the header, parameters and form data
- Added ability to attach files to requests
- Removed debug flag, made it part of standard output
- Added full error handling
