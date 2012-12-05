from distutils.core import setup, Extension

setup (name="jenkins",
       version="1.0",
       maintainer="Rafik Salama",
       description="Wrapper for Jenkins Hash Functions",
       ext_modules=[Extension('jenkins',sources=['jenkins.c'])]
)
