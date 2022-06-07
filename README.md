# Autómata Evolutivo 4
<i>Evolutionary automaton</i>

 - Javier Falgueras
 - Carlos Villagrasa, originally
 - Juan Falgueras
 - Andrés Moya


This program is to be executed on a UNIX/Linux Terminal. It uses
Python 3 and a few standard python libraries.

On Windows there is not a default Terminal, but it is easy to install one See footnote <sup id="a1">[1](#f1)</sup>.

First of all you have to download the directory with the program using
 [the repository https://github.com/juanfal/AE4](https://github.com/juanfal/AE4)

Change to the directory where `ae4.py` is.  There you can execute it by:

    python3 ae4.py

First thing you need to try is:

    python3 ae4.py --help

## Python libraries AE4 needs

If you don't have some of the required standard libraries it needs, you'll be
asked for them just in the first execution.  The program will show you the
standard command to install it.

The next libraries have to be installed

    argparse
    datetime 
    functools 
    matplotlib 
    numpy
    pathlib 
    subprocess 
    urllib 
    xlsxwriter

It is possible to repeat the installation of libraries already installed, 
so if you had any of them but want to ensure you have all the needed ones,
execute each of the following commands:

    pip3 install argparse
    pip3 install datetime
    pip3 install functools
    pip3 install matplotlib
    pip3 install numpy
    pip3 install pathlib
    pip3 install subprocess
    pip3 install urllib
    pip3 install xlsxwriter


Málaga, 2021-05-25

[<b id="f1">1</b> [↩](#a1)] With Windows, you can use
[Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab). To install python3 on Windows, you can
go to [Get started using Python on Windows for beginners](https://docs.microsoft.com/en-us/windows/python/beginners)