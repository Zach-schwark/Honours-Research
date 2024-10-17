#!/bin/bash

#SBATCH --job-name=BDs_BN
#SBATCH --output=/home-mscluster/zschwark/Honours-Research/output_logs/bds_output_logs.txt
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p bigbatch

source ~/.bashrc
conda activate HonoursResearch
python3 ~/Honours-Research/Cross_Validation/BDs_cross_validation.py
