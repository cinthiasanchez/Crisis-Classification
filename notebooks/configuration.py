from IPython import get_ipython
import sys
import os


ipython = get_ipython()
ipython.magic('load_ext autoreload')
ipython.magic('autoreload 2')
sys.path.append(os.path.abspath(os.path.join('..')))
