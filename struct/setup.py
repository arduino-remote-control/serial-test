from distutils.core import setup, Extension

# define the extension module
module = Extension('sc_module', sources=['main.c'])

# run the setup
setup(ext_modules=[module])
