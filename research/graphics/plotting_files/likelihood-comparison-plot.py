import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style for publication-quality plot
#plt.style.use('seaborn-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

def create_comparison_plot(data_path):
    # Read CSV
    df = pd.read_csv(data_path)
    
    # Create figure with appropriate size for publication
    fig, ax = plt.subplots(figsize=(10, 6))
    
    #colors = {
    #    'Random': '#ff0000',  # Red
    #    'K2': '#ffa500',      # Orange
    #    'ChowLiu': '#00ff00', # Green
    #    'BDs': '#000000',     # Black
    #    'BIC': '#0000ff'      # Blue
    #}
    colors = {
        'Random_very_basic' : '#EC915C',
        'Random_basic' : '#EE6B1F',
        'Random_detailed' : '#FD0606',
        'Random_advanced' : '#BD0505',
        'ChowLiu_very_basic' : '#A0CA6A',
        'ChowLiu_basic' : '#5E9C02',
        'ChowLiu_detailed' : '#02BF38',
        'ChowLiu_advanced' : '#02611D',
        'BIC_very_basic' : '#07EBE2',
        'BIC_basic' : '#45BDFC',
        'BIC_detailed' : '#034FCE',
        'BIC_advanced' : '#01245E',
    }
    
    df = df[df['dataset size']>=45000]
    
    
    # Plot each algorithm
    for algorithm in ['Random','ChowLiu','BIC']:
        for evidence_list in ['very_basic','basic', 'detailed', 'advanced']:
            print(f'{algorithm}_{evidence_list} - {evidence_list}_log_likelihood')
            ax.plot(df['dataset size'], 
                    df[f'{algorithm}_{evidence_list} - {evidence_list}_log_likelihood'],
                    label=f'{algorithm} {evidence_list}',
                    color=colors[f'{algorithm}_{evidence_list}'],
                    linewidth=0.85)
    
    #for algorithm in ['Random', 'K2', 'ChowLiu', 'BDs', 'BIC']:
    #    ax.plot(df['dataset size'], 
    #            df[f'{algorithm} - log_likelihood'],
    #            label=algorithm,
    #            color=colors[algorithm],
    #            linewidth=1)
    
    #ax.set_ylim(-600000, -220000) 
    #ax.set_xlim(50000,105000)
    
    #ax.set_ylim(-600000, -40)
    #ax.set_xlim(50,105000)
    
    #ax.set_ylim(-40500, -10)
    #ax.set_xlim(50,90000)
    
    ax.set_ylim(-40000, -7000)
    ax.set_xlim(45000,90000)
    
    # Set log scale for x-axis (matching W&B)
    ax.set_xscale('log')
    ax.set_yscale('symlog')
    
    # Customize the plot
    ax.set_xlabel('Dataset Size', fontsize=18)
    ax.set_ylabel('Log Likelihood', fontsize=18)
    
    # Add grid with light gray color
    ax.grid(True, linestyle='-', alpha=0.2, color='gray')
    
    # Customize legend
    ax.legend(frameon=False, fontsize=13, ncols=3, alignment = 'left', columnspacing = 0.75, borderaxespad=0.25, handlelength=1, handletextpad=0.25)
    
    # Set y-axis limits to match the scale in the image
    
    # Format x-axis ticks to match W&B style

    #ax.set_xticks([pow(10,2), pow(10,3), pow(10,4), pow(10,5)])
    #ax.set_xticklabels(['10$^2$','10$^3$', '10$^4$', '10$^5$'],fontsize=14)
    #
    #ax.set_yticks([-pow(10,2), -pow(10,3),-pow(10,4), -pow(10,5)])
    #ax.set_yticklabels(['-10$^2$', '-10$^3$', '-10$^4$', '-10$^5$'],fontsize=14)
    
    #ax.set_xticks([5*pow(10,4), 6*pow(10,4), 7*pow(10,4), 8*pow(10,4), 9*pow(10,4), pow(10,5)])
    #ax.set_xticklabels(['5x10$^4$','6x10$^4$', '7x10$^4$', '8x10$^4$','9x10$^4$','10$^5$'],fontsize=14)
    #
    #ax.set_yticks([-3*pow(10,5), -4*pow(10,5), -5*pow(10,5)])
    #ax.set_yticklabels(['-3x10$^5$', '-4x10$^5$', '-5x10$^5$'],fontsize=14)
    
    #ax.set_xticks([pow(10,2), pow(10,3), pow(10,4)])
    #ax.set_xticklabels(['10$^2$','10$^3$', '10$^4$'],fontsize=14)
    #
    #ax.set_yticks([-pow(10,1), -pow(10,2),-pow(10,3), -pow(10,4)])
    #ax.set_yticklabels(['-10$^1$', '-10$^2$', '-10$^3$', '-10$^4$'],fontsize=14)
    
    ax.set_xticks([5*pow(10,4), 6*pow(10,4), 7*pow(10,4), 8*pow(10,4), 9*pow(10,4)])
    ax.set_xticklabels(['5x10$^4$','6x10$^4$', '7x10$^4$', '8x10$^4$','9x10$^4$'],fontsize=14)
    
    ax.set_yticks([-pow(10,4), -2*pow(10,4), -3*pow(10,4)])
    ax.set_yticklabels(['-10$^4$', '-2x10$^4$', '-3x10$^4$'],fontsize=14)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot in various formats
    plt.savefig('Graphics/results_plots/evidence_list_comparison_magnified.pdf', format='pdf', bbox_inches='tight', dpi=300)
    #plt.savefig('algorithm_comparison.png', format='png', bbox_inches='tight', dpi=300)
    
    return fig, ax

# Function call
create_comparison_plot('Graphics/Weights_and_biases_chart_data/evidence_lists_loglikelihood.csv')
