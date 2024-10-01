#!/bin/bash

#SBATCH --job-name=Random_BN
#SBATCH --output=/home-mscluster/zschwark/random_output_logs.txt
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p stampede

python3 ~/Bayesian_Networks/Random_BN.py