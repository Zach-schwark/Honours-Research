#!/bin/bash

#SBATCH --job-name=BDs_detailed
#SBATCH --output=/home-mscluster/zschwark/Honours-Research/output_logs/bds_detailed_logs.txt
#SBATCH -N 1
#SBATCH -p bigbatch

source ~/.bashrc
conda activate HonoursResearch
python3 ~/Honours-Research/Cross_Validation/BDs_cross_validation.py 50 dirichlet 5 detailed
