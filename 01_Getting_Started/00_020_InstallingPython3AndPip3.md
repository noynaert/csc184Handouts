# 00.020 Installing Python3 and Pip

## Versions of Python

Python 3 is the current version of Python.  It is what we will be using in this class.

Python 2 is an older version.  Python 2 and Python 3 are very, very similar.  However, there are some things in Python 3 that "break" Python 2.  

You probably will never need Python 2, but be aware of which version you are using.  Also, if you are on a machine you are not familiar with it is important to see which version of python you are using.  How to check the version is discussed later.

## Installing Python and Pip

We need to install Python3 and a related program called Pip.

### Windows installation

Visit [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

The Windows installer listed above will include pip automatically.

### Linux installation

For Debian-based systems like Ubuntu, Mint, and Pop! use the following commands:

```bash
sudo apt update
sudo apt install python3 python3-pip
sudo apt install python-is-python3
```

if you are on a .rpm system like Fedora or CentOS use your package manage instead of ```apt```.  This would probably be ```dnf``` or ```yum``` but if you are using one of those systems I assume you know what to do.

### Mac installation

Consult [https://docs.python.org/3/using/mac.html](https://docs.python.org/3/using/mac.html) to set up Python3 on your Mac.  Don't worry too much about the python launcher.


## Testing your install

Open a terminal

Type the following commands:

    python --version
    pip --version

You might need to type ```python3``` instead of python.  (That is why I had you install python-is-python on linux systems.)



