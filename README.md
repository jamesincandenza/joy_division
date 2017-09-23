# joy_division
matlibplot to recreate Unknown Pleasures album cover

Taken from: https://news.ycombinator.com/item?id=5729268

Installing:
* virtualenv joy —python=python2.7
    * Installs python 2.7 virtualenv (required for above script)
* source joy/bin/activate
* pip install scipy
* brew install freetype
    * free type is a dependant library that allows export to .png
    * threw error but didn’t seem to matter...
* pip install matplotlib==1.4.0
    * Installs required matplotlib which included pylab

Creates a random pulsar wave diagram that looks a lot like the Uknown Pleasures album cover.
