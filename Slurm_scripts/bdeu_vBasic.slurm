#!/bin/bash

#SBATCH --job-name=BDeu_Vbasic
#SBATCH --output=/home-mscluster/zschwark/Honours-Research/output_logs/bdeu_very_basic_output_logs.txt
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p bigbatch

source ~/.bashrc
conda activate HonoursResearch
python3 ~/Honours-Research/Cross_Validation/BDeu_cross_validation.py 50 dirichlet 2 very_basic
