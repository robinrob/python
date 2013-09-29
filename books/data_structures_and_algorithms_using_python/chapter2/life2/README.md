# Installation

##Install Homebrew:
- ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

##Install Python2.7:
This is necessary purely to run the Fabric tool as it has not been ported to Python3 yet!

## Install Fabric:
- pip-2.7 install fabric

- brew install python2.7

##Install Python3: 
- brew install Python3

##Install Pip3:
- curl -O http://python-distribute.org/distribute_setup.py
- sudo python3 distribute_setup.py

Depending on the version of Python3 you installed, put this in your terminal profile file (.bashrc, .zshrc):
- export PATH=/Library/Frameworks/Python.framework/Versions/3.3/bin:$PATH

Check the version of pip:
- pip --version

You can use the old version of pip using:
- pip-2.7

Instructions from: http://iainhunter.wordpress.com/2012/11/08/howto-install-python3-pip3-tornado-on-mac/

##Install Pythonbrew:
- sudo easy_install pythonbrew 
- pythonbrew_install

Instructions from: http://www.howopensource.com/2011/05/how-to-install-and-manage-different-versions-of-python-in-linux/

						
##Build the Life project:
fab install


# Running Life

## Command Usage

### Help
- fab run:args="--help"

### Example
- fab run:args="100 30 100 0.1"


# Configuring Life
Run-time configuration is made using the command-line arguments.

Edit the settings.py file to change the starting configuration of cells. Examples are in that file as comments.