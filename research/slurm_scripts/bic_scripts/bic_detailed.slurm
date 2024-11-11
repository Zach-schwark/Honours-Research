#!/bin/bash

#SBATCH --job-name=bic_detailed
#SBATCH --output=/home-mscluster/zschwark/Honours-Research/output_logs/bic_detailed_output_logs.txt
#SBATCH -N 1
#SBATCH -p bigbatch

source ~/.bashrc
conda activate HonoursResearch
python3 ~/Honours-Research/Cross_Validation/BIC_cross_validation.py dirichlet 5 detailed
