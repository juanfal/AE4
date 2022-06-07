# Autómata Evolutivo 4
<i>Evolutionary automaton</i>

 - Javier Falgueras
 - Carlos Villagrasa, originally
 - Juan Falgueras
 - Andrés Moya


This program is to be executed on a UNIX/Linux Terminal. It uses
Python 3 and a few standard python libraries.

If you use a modern Windows, you need to install Python which is not pre-installed.  You can do that using this
[link https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe](https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe)

If you have an old Windows, perhaps you would need to see which one could suit your version:
[link https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

You have many videos explain the process [like this one](https://www.youtube.com/watch?v=Kn1HF3oD19c)

The Terminal command on Windows can be the simple `command.com` you can find it through the "Start" button and searching for `Command Prompt`

<!-- On Windows there is not a default Terminal, but it is easy to install one See footnote <sup id="a1">[1](#f1)</sup>.
 -->

On MacOSX/Linux search for the application terminal and check python3 works there.

Once Terminal + Python are ready, continue installing our AE4:

First of all you have to download the directory with the program using
 [the repository https://github.com/juanfal/AE4](https://github.com/juanfal/AE4)

 The simplest way is to Use the Green Button-Menu -> Download Zip

 Then decompress the .zip file and execute your Terminal aplication on your
 computer, once the window of your Terminal is prompting you for a command,
change to the fresh uncompressed directory where `ae4.py` is.

    cd ...../AE4 

the dots depend on the place you decompressed the downloaded .zip file

There you can execute it by:

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


To follow the examples described in the Article this program is made for:

Once the program is installed and running, to try each of the examples you can
use the name of the file in `data` (no need to use the name of the `data`
directory) like: `Paper2/2Plank1.json`

Or you can add specific parameters like the ones in the Article this program is
the base for.  In this case the parameters parameters for each case can be
copy–pasted into the Terminal from the table “Terminal Command or Rank:” found
in the Supplementary Material.

For example, for the 'Paradox of the plankton' one of the examples is:

    python3 ae4.py Paper1/1Plank4 --numGen=200 --saveExcel --setRandomSeed=1 --verbose



Málaga, 2021-05-25

[<b id="f1">1</b> [↩](#a1)] With Windows, you can use
[Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab). To install python3 on Windows, you can
go to [Get started using Python on Windows for beginners](https://docs.microsoft.com/en-us/windows/python/beginners)