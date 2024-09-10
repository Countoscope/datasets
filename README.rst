Datasets for the countoscope
============================

This repository is used as a submodule of main `countoscope`_. The
trajectory files are used to test the Python code.

.. _countoscope: https://github.com/Countoscope/countoscope

Git LFS
-------

The trajectory files are stored as Git Large File Storage (LFS). Make sure to
install it using:

.. code:: bash

    git lfs install

If you want a particular type of file to be stored as LFS, type:

.. code:: bash

    git lfs track "*.psd"

This way, all future `.psd` files will be stored by Git as LFS.

MD trajectories
---------------

This repository contains .XYZ and .LAMMPSTRJ trajectory files for:
- 2D closed system with constant number of atoms
- 2D open system with varying number of atoms
- 3D closed system with constant number of atoms

All .XYZ and .LAMMPSTRJ stored used the LFS of GitHub.

The trajectories were generated using LAMMPS. Atoms are interacting through a WCA potential (purely repulsive) and are overdamped by a Langevin thermostat to suppress the balistic motion.

Home-made trajectories
----------------------

A trajectory in a homemade text format is provided. The first 2 columns are the X, Y coordinates, and the 3rd is the frame id. It starts like:

.. code:: bash

    79.22997498 41.66934981 0
    52.68320482 56.56090417 0
    95.31904644 10.28635822 0
    73.22342313 2.88654587 0
    69.49561442 93.15505145 0
    19.92067812 89.50609614 0
    38.64668966 91.52427308 0
    70.50447852 52.47750822 0
    44.48873150 48.93966159 0
    51.18881667 38.76888911 0
    (...)

