import argparse
import pandas as pd
import matplotlib.pyplot as plt
from Bio import SeqIO
import os

def calculate_rolling_metrics(sequence, window_size=100):
    """Calculates rolling GC% and CpG count for a given sequence."""
    seq_str = str(sequence).upper()
    data = []
    
    for i in range(len(seq_str) - window_size + 1):
        window = seq_str[i:i+window_size]
        gc_content = (window.count('G') + window.count('C')) / window_size * 100
        cpg_count = window.count('CG')
        
        data.append({
            'Position': i,
            'GC_Percent': gc_content,
            'CpG_Count': cpg_count
        })
        
    return pd.DataFrame(data)

def analyze_fasta(input_fasta, window_size, output_dir):
    """Parses FASTA, runs metrics, and generates outputs."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    summary_stats = []

    for record in SeqIO.parse(input_fasta, "fasta"):
        print(f"Analyzing {record.id}...")
        df = calculate_rolling_metrics(record.seq, window_size)
        
        # Save detailed CSV
        csv_path = os.path.join(output_dir, f"{record.id}_profile.csv")
        df.to_csv(csv_path, index=False)
        
        # Generate Plot
        fig, ax1 = plt.subplots(figsize=(10, 5))
        
        ax1.set_xlabel('Sequence Position (bp)')
        ax1.set_ylabel('GC Content (%)', color='tab:blue')
        ax1.plot(df['Position'], df['GC_Percent'], color='tab:blue', label='GC%')
        ax1.tick_params(axis='y', labelcolor='tab:blue')
        ax1.axhline(50, color='gray', linestyle='--', alpha=0.5) # 50% baseline
        
        ax2 = ax1.twinx()
        ax2.set_ylabel('CpG Count per Window', color='tab:red')
        ax2.plot(df['Position'], df['CpG_Count'], color='tab:red', alpha=0.6, label='CpG')
        ax2.tick_params(axis='y', labelcolor='tab:red')
        
        plt.title(f'Sequence Profile: {record.id} (Window={window_size}bp)')
        fig.tight_layout()
        plt.savefig(os.path.join(output_dir, f"{record.id}_plot.png"))
        plt.close()

        # Collect summary
        summary_stats.append({
            'Sequence_ID': record.id,
            'Length': len(record.seq),
            'Mean_GC': df['GC_Percent'].mean(),
            'Total_CpGs': str(record.seq).upper().count('CG')
        })

    pd.DataFrame(summary_stats).to_csv(os.path.join(output_dir, "summary.csv"), index=False)
    print("Analysis complete. Check the output directory.")

if __name__ == "__main__":
    # Setup for command line execution
    parser = argparse.ArgumentParser(description="Profile cis-regulatory sequences.")
    parser.add_argument("--input", required=True, help="Input FASTA file")
    parser.add_argument("--window", type=int, default=100, help="Sliding window size in bp")
    parser.add_argument("--outdir", default="output", help="Directory for results")
    args = parser.parse_args()
    
    analyze_fasta(args.input, args.window, args.outdir)