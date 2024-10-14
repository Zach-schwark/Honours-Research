#!/bin/bash

#SBATCH --job-name=BIC_BN
#SBATCH --output=/home-mscluster/zschwark/Honours-Research/output_logs/bic_output_logs.txt
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p bigbatch

source ~/.bashrc
conda activate HonoursResearch
python3 ~/Honours-Research/Bayesian_Networks/BIC_BN.py
