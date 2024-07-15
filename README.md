# image2hex

Converts an image to a binary file where `00` means black and `FF` means white.

How to use (see details below):
* Install Python3
* (optionally) Create a virtual environment
* Install dependencies
* Run `python3 image2hex.py --input=text.jpg --output=text.bin --black_threshold=40`

## Creating virtual environment

[Docs](https://docs.python.org/3/library/venv.html)

On *nix:

```
python3 -m venv venv
```

On Windows, invoke the `venv` command as follows:


```
c:\>Python35\python -m venv c:\path\to\myenv
```

## Activating the virtual environment

On *nix:

```
python3 -m venv venv
```

On Windows:

```
C:\> <venv>\Scripts\activate.bat
```

or

```
PS C:\> <venv>\Scripts\Activate.ps1
```

## Installing dependencies

```
pip install -r requirements.txt
```

## How to use

```
python3 image2hex.py --input=text.jpg --output=text.bin --black_threshold=40
```

## Demo

![Demo](demo.gif)