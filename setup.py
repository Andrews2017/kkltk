from distutils.core import setup
setup(
  name = 'kkltk',         # package name
  packages = ['kkltk'],   # same as "name"
  version = '1.0',      # first version
  license='MIT',        # This package is licenced under MIT licence
  description = 'kkltk is a toolkit designed for Kinyarwanda and Kirundi languages processing',
  author = 'Rubungo Andre Niyongabo',
  author_email = 'niyongabor.andre@gmail.com',
  url = 'https://sites.google.com/view/niyongabo-rubungo-andre/home',
  download_url = 'https://github.com/Andrews2017/kkltk/archive/v1.0.tar.gz',
  keywords = ['Low-resource languages', 'natural language processing', 'computational linguistics', 'Kinyarwanda', 'Kirundi', 'text preprocessing', 'stopwords', 'tokenizing'],   # Keywords that define kkltk package
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Education',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Developers',
    'Topic :: Text Processing',
    'Topic :: Text Processing :: Filters',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Operating System :: OS Independent',
  ],
)