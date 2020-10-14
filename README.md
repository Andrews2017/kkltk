[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

# KKLTK: Kinyarwanda and Kirundi Languages ToolKit
KKLTK is a Python package for Kinyarwanda and Kirundi languages processing. KKLTK currently provides the sets of stopwords for both languages and other preprocessing tools such as Kinyarwanda and Kirundi tokenizers will be added soon. KKLTK requires Python 3.0, 3.5, 3.6, 3.7, or 3.8.

For more details information on how these stopwords were obtained, please refer to the paper to appear in [COLING 2020](https://coling2020.org/) titled  ["KINNEWS and KIRNEWS: Benchmarking Cross-Lingual Text Classification for Kinyarwanda and Kirundi"](https://github.com/Andrews2017/KINNEWS-and-KIRNEWS) by [Rubungo Andre Niyongabo](https://scholar.google.com/citations?user=5qnTWQEAAAAJ&hl=en), [Hong Qu](https://scholar.google.com/citations?user=Aiq9mFMAAAAJ&hl=en), [Julia Kreutzer](https://scholar.google.co.uk/citations?user=j4cOSzAAAAAJ&hl=en), and Li Huang.
# Installation
```sh
pip install kkltk==1.0
```

# Usage
## Stopwords
```sh
from kkltk.kin_kir_stopwords import stopwords

# Kinyarwanda
stopset_kin = stopwords.words('kinyarwanda')

# Kirundi
stopset_kir = stopwords.words('kirundi')
```

# Contributing
KKLTK is the beginning step of putting under-represented languages on the NLP map. The provided stopwords lists on both languages are still growing. Please [contact me](https://sites.google.com/view/niyongabo-rubungo-andre/contact) for any contribution you may want to provide.
