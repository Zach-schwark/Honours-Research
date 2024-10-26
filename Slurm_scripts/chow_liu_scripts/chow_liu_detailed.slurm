#!/bin/bash

#SBATCH --job-name=ChowLiu_detailed
#SBATCH --output=/home-mscluster/zschwark/Honours-Research/output_logs/chowliu_detailed_output_logs.txt
#SBATCH -N 1
#SBATCH -p bigbatch

source ~/.bashrc
conda activate HonoursResearch
python3 ~/Honours-Research/Cross_Validation/ChowLiu_cross_validation.py detailed