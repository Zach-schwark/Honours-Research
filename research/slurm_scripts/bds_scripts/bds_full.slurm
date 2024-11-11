#!/bin/bash

#SBATCH --job-name=BDs_full
#SBATCH --output=/home-mscluster/zschwark/Honours-Research/output_logs/bds_full_output_logs.txt
#SBATCH -N 1
#SBATCH -p stampede

source ~/.bashrc
conda activate HonoursResearch
python3 ~/Honours-Research/Cross_Validation/BDs_cross_validation.py 50 dirichlet 5 none
