#!/bin/bash

#SBATCH --job-name=Random_detailed
#SBATCH --output=/home-mscluster/zschwark/Honours-Research/output_logs/random_detailed_output_logs.txt
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p bigbatch

source ~/.bashrc
conda activate HonoursResearch
python3 ~/Honours-Research/Cross_Validation/Random_cross_validation.py detailed
