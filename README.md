# Autómata Evolutivo 4 #
Evolutionary automaton programmed in Python by

 - Javier Falgueras
 - Carlos Villagrasa, originally
 - Juan Falgueras
 - Andrés Moya

This programs needs Python 3 and, once available in your system, a few
standard python libraries.

To execute this program you need to be on a UNIX-like `Terminal` (Windows users see the footnote <sup id="a1">[1](#f1)</sup>).

Change to the directory where `ae4.py` is.  There you can execute it by:

    ./ae4.py

or

    python3 ae4.py


First thing you can try is:


    ./ae4.py --help

or

    python3 ae4.py --help

## Dependencies

If you don't have some of the required standard packages it needs, you'll be
asked for them just in the first execution.  The program will show you the
standard command to install it.


The next libraries are necessary
(`argparse`, `datetime`, `functools`, `matplotlib`, `numpy`,
`pathlib`, `subprocess`, `urllib`, `xlsxwriter`):


It doesn't harm to repeat their installation if you had any already installed:

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