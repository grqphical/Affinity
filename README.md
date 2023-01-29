
<div align="center" float="left"><span><img src="affinity.png" width="100" height="100"></span><h1>Affinity</h1></div>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://badgen.net/github/license/Naereen/Strapdown.js)](https://github.com/grqphical07/Affinity/blob/master/LICENSE)
[![GitHub latest commit](https://badgen.net/github/last-commit/grqphical07/Affinity)](https://GitHub.com/grqphical07/Affinity/commit)
[![GitHub stars](https://img.shields.io/github/stars/grqphical07/Affinity.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/grqphical07/Affinity/stargazers/)

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

Now you should be able to see the JSON response from the API. But what if we want to output it into a file. You can use the *-f* flag plus a file name to output the results into a file.
```bash
$ affinity https://api.github.com/ -f response.json
```
*Note: You can use -o and -f at the same time*
This takes the response and writes it to response.json

If you want to learn more either visit the wiki or use the -h flag for help
