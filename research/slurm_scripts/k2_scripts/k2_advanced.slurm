#!/bin/bash

#SBATCH --job-name=K2_advanced
#SBATCH --output=/home-mscluster/zschwark/Honours-Research/output_logs/k2_advanced_output_logs.txt
#SBATCH -N 1
#SBATCH -p bigbatch

source ~/.bashrc
conda activate HonoursResearch
python3 ~/Honours-Research/Cross_Validation/K2_cross_validation.py dirichlet 5 advanced