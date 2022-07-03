# cubeofrubik
A Rubik's cube model and solver

### Installation
    
```bash
pip install cubeofrubik
```

### Usage:
```python
>>> from rubikscube import RubiksCube

>>> cube = RubiksCube.RubiksCube()

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
'DU′R2U′B2L′BUB′RU2R′U′RUR′FU2F′R′U′RFUF′U′FUF′LUL′U′B′U′BU2F′U′FURUR′U′LUL′U′B′U′BUFUF′U′L′U′LU2FRUR′U′RUR′U′F′RUR′URU2R′U2BUB′UBU2B′URDR′D′RDR′D′URDR′D′RDR′D′URDR′D′RDR′D′U2'

>>> cube.draw()
⬛ ⬛ ⬛ 🟨 🟨 🟨 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ 🟨 🟨 🟨 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ 🟨 🟨 🟨 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
🟧 🟧 🟧 🟦 🟦 🟦 🟥 🟥 🟥 🟩 🟩 🟩
🟧 🟧 🟧 🟦 🟦 🟦 🟥 🟥 🟥 🟩 🟩 🟩
🟧 🟧 🟧 🟦 🟦 🟦 🟥 🟥 🟥 🟩 🟩 🟩
⬛ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 

>>> cube.move("RUR′U′")
>>> cube.draw()
⬛ ⬛ ⬛ 🟨 🟨 🟧 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ 🟨 🟨 🟦 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ 🟨 🟨 🟦 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
🟩 🟧 🟧 🟦 🟦 ⬜ 🟥 🟥 🟨 🟩 🟥 🟥
🟧 🟧 🟧 🟦 🟦 🟨 🟩 🟥 🟥 🟩 🟩 🟩
🟧 🟧 🟧 🟦 🟦 🟦 🟨 🟥 🟥 🟩 🟩 🟩
⬛ ⬛ ⬛ ⬜ ⬜ 🟥 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
⬛ ⬛ ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 
```

### License

This cubeofrubik is available under the MIT license. Read the LICENSE file for more info.