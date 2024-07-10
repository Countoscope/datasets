# Create the parameter file for the LAMMPS simulation

import os, sys, shutil
import numpy as np
from pint import UnitRegistry
ureg = UnitRegistry()

temperature = 1 # no units
desired_packing = 0.1 # packing fraction of particles
dim = 2 # desired dimension
required_box_size = 90 # Angstroms
damping = 2 # thermostat damping (use ~ 2-5 for overdamped, 100 for normal MD simulation)

# define the basic LJ fluid properties
sigma = 3 * ureg.angstrom # A
cut_off = sigma*2**(1/6) # WCA potential
epsilon = 0.1 * ureg.kcal / ureg.mol # kcal/mol
mass = 1.0 * ureg.g / ureg.mol # g/mol
kB = 1.987204259e-3 * ureg.kcal / ureg.mol / ureg.K # kcal/mol/K

# estimate the temperature in Kelvin
T_star = temperature
temp_pref = epsilon/kB
T = np.round(temp_pref * T_star, 3) # K

# set the basic simulation properties
time_pref = np.sqrt(mass*sigma**2/epsilon)
timestep = 0.005 * time_pref # fs
timestep = timestep.to(ureg.fs)  # fs

volume_single_particle = np.pi * sigma**dim / 6

actual_box_size = np.int32((required_box_size / sigma).magnitude)*sigma
total_volume = actual_box_size ** dim
particule_number  = np.int32(desired_packing * total_volume / volume_single_particle)

number_density = particule_number / total_volume
non_dim_number_density = number_density * sigma**3
actual_packing_fraction = particule_number * volume_single_particle / total_volume

print("n_part = "+str(particule_number))
print("box dimension = "+str(actual_box_size))
print("adim number density:", np.round(non_dim_number_density.magnitude,4))
print("packing fraction:", np.round(actual_packing_fraction.magnitude,4), "--- desired:", desired_packing)

f = open("parameters.lammps", "w")
f.write("# LAMMPS parameters \n")
f.write("\n")
f.write("# Random numbers \n")
for i in range(1,4):
    f.write("variable rdm"+str(i)+" equal " + str(np.random.randint(10000, 99999)) + "\n")
f.write("\n")
f.write("# Fluid parameters \n")
f.write("variable mass equal " + str(mass.magnitude) + " # " + str(mass.units) + "\n")
f.write("variable sigma equal " + str(sigma.magnitude) + " # " + str(sigma.units) + "\n")
f.write("variable epsilon equal " + str(epsilon.magnitude) + " # " + str(epsilon.units) + "\n")
f.write("\n")
f.write("# Simulation parameters \n")
f.write("variable dt equal " + str(timestep.magnitude) + " # " + str(timestep.units) + "\n")
f.write("variable n_part equal " + str(particule_number) + "\n")
f.write("variable L equal " + str(actual_box_size.magnitude) + " # " + str(actual_box_size.units) + "\n")
f.write("variable L_up equal " + str(actual_box_size.magnitude/2) + " # " + str(actual_box_size.units) + "\n")
f.write("variable L_down equal " + str(-actual_box_size.magnitude/2) + " # " + str(actual_box_size.units) + "\n")
f.write("variable S_up equal " + str(actual_box_size.magnitude/2/3) + " # " + str(actual_box_size.units) + "\n")
f.write("variable S_down equal " + str(-actual_box_size.magnitude/2/3) + " # " + str(actual_box_size.units) + "\n")
f.write("variable cut_off equal " + str(cut_off.magnitude)  + " # " + str(cut_off.units) + "\n")
f.write("variable T equal " + str(T.magnitude) + " # " + str(T.units) + "\n")
f.write("variable damp_langevin equal " + str(timestep.magnitude*damping) + " # " + str(timestep.units) + "\n")
f.close()