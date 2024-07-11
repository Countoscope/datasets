# Datasets for the countoscope

This repository contains .XYZ and .LAMMPSTRJ trajectory files for:
- 2D closed system with constant number of atoms
- 2D open system with varying number of atoms
- 3D closed system with constant number of atoms

All .XYZ and .LAMMPSTRJ stored used the LFS of GitHub.

The trajectories were generated using LAMMPS. Atoms are interacting through a WCA potential (purely repulsive) and are overdamped by a Langevin thermostat to suppress the balistic motion.

This repository is called as a submodule by the [main countoscope repository](https://github.com/Countoscope/countoscope), and the trajectory are used to test the Python code.
