#!/bin/bash

#SBATCH --job-name=ChowLiu_Vbasic
#SBATCH --output=/home-mscluster/zschwark/Honours-Research/output_logs/chowliu_vbasic_output_logs.txt
#SBATCH -N 1
#SBATCH -p stampede

source ~/.bashrc
conda activate HonoursResearch
python3 ~/Honours-Research/Cross_Validation/ChowLiu_cross_validation.py very_basic