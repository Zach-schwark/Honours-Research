#!/bin/bash

#SBATCH --job-name=ChowLiu_basic
#SBATCH --output=/home-mscluster/zschwark/Honours-Research/output_logs/chowliu_basic_output_logs.txt
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p stampede

source ~/.bashrc
conda activate HonoursResearch
python3 ~/Honours-Research/Cross_Validation/ChowLiu_cross_validation.py basic