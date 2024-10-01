#!/bin/bash

#SBATCH --job-name=BDs_BN
#SBATCH --output=/home-mscluster/zschwark/bds_output_logs.txt
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p stampede

python3 ~/Bayesian_Networks/BDs_BN.py