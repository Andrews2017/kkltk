from distutils.core import setup
setup(
  name = 'kltk',         # package name
  packages = ['kltk'],   # same as "name"
  version = '0.1',      # first version
  license='MIT',        # This package is licenced under MIT licence
  description = 'kltk is a toolkit designed for Kinyarwanda and Kirundi languages',
  author = 'Rubungo Andre Niyongabo',
  author_email = 'niyongabor.andre@gmail.com',
  url = 'https://sites.google.com/view/niyongabo-rubungo-andre/home',
  download_url = 'https://github.com/Andrews2017/kltk/archive/v1.0.tar.gz',
  keywords = ['Kinyarwanda', 'Kirundi', 'toolkit', 'stopwords'],   # Keywords that define package
  install_requires=[            # I get to this in a second
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
