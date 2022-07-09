.. cubeofrubik documentation master file, created by
   sphinx-quickstart on Sat Jul  9 18:03:22 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to cubeofrubik's documentation!
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

cubeofrubik
===========

A Rubik’s cube model and solver. Visit the project `homepage <https://github.com/blevic/cubeofrubik/>`__.

Installation
~~~~~~~~~~~~

.. code:: bash

   pip install cubeofrubik

Documentation
~~~~~~~~~~~~~

Find complete documentation on:
`cubeofrubik.rtfd.io <https://cubeofrubik.rtfd.io/>`__.

Usage:
~~~~~~

.. code:: python

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



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
