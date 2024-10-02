#!/bin/bash

#SBATCH --job-name=Random_BN
#SBATCH --output=/home-mscluster/zschwark/Honours-Research/output_logs/random_output_logs.txt
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p stampede

source ~/.bashrc
conda activate HonoursResearch
python3 ~/Honours-Research/Bayesian_Networks/Random_BN.py