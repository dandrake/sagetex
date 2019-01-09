from distutils.core import setup
setup(name='sagetex',
      description='Embed Sage code and plots into LaTeX',
      long_description="""The SageTeX package allows you to embed code,
  results of computations, and plots from the Sage mathematics
  software suite (http://sagemath.org) into LaTeX documents.""",
      version='3.2',
      author='Dan Drake',
      author_email='dr.dan.drake@gmail.com',
      maintainer='SageMath developers',
      maintainer_email='sage-devel@googlegroups.com',
      url='https://github.com/sagemath/sagetex',
      license='GPLv2+',
      py_modules=['sagetex'],
      data_files = [('share/texmf/tex/latex/sagetex',
        ['example.tex',
         'CONTRIBUTORS',
         'extractsagecode.py',
         'run-sagetex-if-necessary.py',
         'makestatic.py',
         'scripts.dtx',
         'remote-sagetex.dtx',
         'remote-sagetex.py',
         'py-and-sty.dtx',
         'sagetex.dtx',
         'sagetex.ins',
         'sagetexparse.py',
         'sagetex.sty']),
      ('share/doc/sagetex', [
         'example.tex',
         'sagetex.pdf',
         'example.pdf'])])
