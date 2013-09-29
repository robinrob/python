# Installation

##Install Homebrew:
- ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

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

Use this if you get stuck: http://iainhunter.wordpress.com/2012/11/08/howto-install-python3-pip3-tornado-on-mac/

##Install Pythonbrew:
http://www.howopensource.com/2011/05/how-to-install-and-manage-different-versions-of-python-in-linux/

						
##Build the Life project:
- make install