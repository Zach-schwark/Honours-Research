#!/bin/bash

#SBATCH --job-name=Random_basic
#SBATCH --output=/home-mscluster/zschwark/Honours-Research/output_logs/random_basic_output_logs.txt
#SBATCH -N 1
#SBATCH -p stampede

source ~/.bashrc
conda activate HonoursResearch
python3 ~/Honours-Research/Cross_Validation/Random_cross_validation.py basic
