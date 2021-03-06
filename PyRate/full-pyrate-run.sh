#! /bin/bash

# Script to run full pyrate pipeline on Canidae

# navigate to the working directory
cd ~/Desktop/eeb-177/eeb177-final-project/PyRate

# download the data
wget -O felidae_occ.csv "https://paleobiodb.org/data1.2/occs/list.csv?base_name=Felidae&show=acconly"

# use the R script we had created to format the data into a pyrate-friendly file
# NOTE!
# if the output files from the R script already exist in the working directory, 
# THIS STEP WILL NOT WORK!
# The existent files are NOT overwritten!
Rscript process_felid_data.R

# Verify that the data formatting worked, and redirect the output into a file called 
# data_summary.txt so that it may be inspected later.
python ~/PyRate/PyRate.py felidae_occ_PyRate.py -data_info > data_summary.txt

# And then, run PyRate!
python ~/PyRate/PyRate.py felidae_occ_PyRate.py -n 1000000

#change directory to the newly created 
cd pyrate_mcmc_logs/

#create graphs
python ~/PyRate/PyRate.py -plot felidae_occ_1_marginal_rates.log
