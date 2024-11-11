#!/bin/bash

#SBATCH --job-name=bic_full
#SBATCH --output=/home-mscluster/zschwark/Honours-Research/output_logs/bic_full_output_logs.txt
#SBATCH -N 1
#SBATCH -p stampede

source ~/.bashrc
conda activate HonoursResearch
python3 ~/Honours-Research/Cross_Validation/BIC_cross_validation.py dirichlet 5 none 
