#!/bin/bash

#SBATCH --job-name=BIC_BN
#SBATCH --output=/home-mscluster/zschwark/bic_output_logs.txt
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p stampede

python3 ~/Bayesian_Networks/BIC_BN.py