#!/bin/bash

#SBATCH --job-name=K2_BN
#SBATCH --output=/home-mscluster/zschwark/k2_output_logs.txt
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p stampede

python3 ~/Bayesian_Networks/K2_BN.py