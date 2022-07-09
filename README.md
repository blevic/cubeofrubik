# cubeofrubik
<p align="left">
  <a href='https://pypi.org/project/cubeofrubik/'>
    <img src='https://img.shields.io/pypi/v/cubeofrubik' alt='PyPi Version' />
  </a>
  <a href='https://pypi.org/project/cubeofrubik/'>
    <img src='https://img.shields.io/pypi/dm/cubeofrubik' alt='Downloads/Month' />
  </a>
    <a href='https://github.com/blevic/cubeofrubik/actions/workflows/package-tests.yml'>
    <img src='https://github.com/blevic/cubeofrubik/actions/workflows/package-tests.yml/badge.svg?branch=main' alt='Package Tests' />
  </a>
  <a href='https://cubeofrubik.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/cubeofrubik/badge/?version=latest' alt='Documentation Status' />
  </a>
</p>

A Rubik's cube model and solver.

### Installation
    
```bash
pip install cubeofrubik
```

### Documentation
Find complete documentation on: [cubeofrubik.rtfd.io](https://cubeofrubik.rtfd.io/).

### Usage:

```python
>>> from cubeofrubik import RubiksCube

>>> cube = RubiksCube()

>>> cube.draw()
⬛ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
🟧 🟧 🟧 🟩 🟩 🟩 🟥 🟥 🟥 🟦 🟦 🟦
🟧 🟧 🟧 🟩 🟩 🟩 🟥 🟥 🟥 🟦 🟦 🟦
🟧 🟧 🟧 🟩 🟩 🟩 🟥 🟥 🟥 🟦 🟦 🟦
⬛ ⬛ ⬛ 🟨 🟨 🟨 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ 🟨 🟨 🟨 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ 🟨 🟨 🟨 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
>>> cube.scramble()
'B′DU′F′DB2FRDBF2URBDB2U′D′L2D'

>>> cube.draw()
⬛ ⬛ ⬛ 🟧 🟦 🟦 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬜ 🟩 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ 🟦 🟨 ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
🟩 🟥 🟨 🟧 🟥 🟩 🟥 🟥 ⬜ 🟥 🟥 🟨
🟩 🟧 ⬜ 🟦 🟩 🟨 🟧 🟥 🟧 🟦 🟦 🟧
🟧 🟩 🟨 🟩 🟦 🟨 🟥 🟧 ⬜ 🟧 🟩 🟩
⬛ ⬛ ⬛ 🟥 🟨 🟦 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ 🟨 🟨 ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬜ 🟦 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 

>>> cube.solve()
'RB′UR′UB′R2U2R2L2B′U′L2D′L2F2DL2UD′L2'

>>> cube.draw()
⬛ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
🟧 🟧 🟧 🟩 🟩 🟩 🟥 🟥 🟥 🟦 🟦 🟦
🟧 🟧 🟧 🟩 🟩 🟩 🟥 🟥 🟥 🟦 🟦 🟦
🟧 🟧 🟧 🟩 🟩 🟩 🟥 🟥 🟥 🟦 🟦 🟦
⬛ ⬛ ⬛ 🟨 🟨 🟨 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ 🟨 🟨 🟨 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ 🟨 🟨 🟨 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 

>>> cube.move("RUR′U′")
>>> cube.draw()
⬛ ⬛ ⬛ ⬜ ⬜ 🟧 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬜ 🟩 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬜ 🟩 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
🟦 🟧 🟧 🟩 🟩 🟨 🟥 🟥 ⬜ 🟦 🟥 🟥
🟧 🟧 🟧 🟩 🟩 ⬜ 🟦 🟥 🟥 🟦 🟦 🟦
🟧 🟧 🟧 🟩 🟩 🟩 ⬜ 🟥 🟥 🟦 🟦 🟦
⬛ ⬛ ⬛ 🟨 🟨 🟥 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ 🟨 🟨 🟨 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ 🟨 🟨 🟨 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 

>>> cube.is_solvable()
True

>>> cube.is_solved()
False

>>> cube.get_color('F')
'G'

>>> cube.find_position('G', 'Y', 'R')
'UFR'

>>> cube.get_size()
3

>>> cube.set_color('01', 'R')
>>> cube.draw()
⬛ ⬛ ⬛ ⬜ ⬜ 🟧 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬜ 🟩 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬜ 🟩 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
🟦 🟧 🟧 🟥 🟩 🟨 🟥 🟥 ⬜ 🟦 🟥 🟥
🟧 🟧 🟧 🟩 🟩 ⬜ 🟦 🟥 🟥 🟦 🟦 🟦
🟧 🟧 🟧 🟩 🟩 🟩 ⬜ 🟥 🟥 🟦 🟦 🟦
⬛ ⬛ ⬛ 🟨 🟨 🟥 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ 🟨 🟨 🟨 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ 🟨 🟨 🟨 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 

>>> cube.is_solvable()
False
```

### License

This cubeofrubik is available under the MIT license. Read the LICENSE file for more info.
