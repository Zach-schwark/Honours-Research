#!/bin/bash

#SBATCH --job-name=BDeu_BN
#SBATCH --output=/home-mscluster/zschwark/bdeu_output_logs.txt
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p stampede

python3 ~/Bayesian_Networks/BDeu_BN.py