import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_hardware_graphs():
    csv_path = 'results/processed/stage2_hardware_summary.csv'
    if not os.path.exists(csv_path):
        print(f"Summary CSV not found at {csv_path}. Run parse_vivado.py first.")
        return

    df = pd.read_csv(csv_path)
    output_dir = 'graphs'
    os.makedirs(output_dir, exist_ok=True)

    # 1. LUT & Flip-Flop Resource Comparison
    plt.figure(figsize=(8, 5))
    x = range(len(df['Algorithm']))
    plt.bar([a - 0.2 for a in x], df['LUTs'], width=0.4, label='LUTs', color='#2b5c8f')
    plt.bar([a + 0.2 for a in x], df['FlipFlops'], width=0.4, label='Flip-Flops', color='#d95f02')
    plt.xticks(x, df['Algorithm'])
    plt.ylabel('Count')
    plt.title('Hardware Resource Utilization (LUTs vs FFs)')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'Hardware_Resource_Utilization.png'))
    plt.close()

    # 2. Maximum Operating Frequency (Fmax) Comparison
    plt.figure(figsize=(7, 4.5))
    plt.bar(df['Algorithm'], df['Fmax_MHz'], color='#2ca02c', width=0.5)
    plt.ylabel('Fmax (MHz)')
    plt.title('Maximum Operating Frequency Comparison')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'Fmax_Comparison.png'))
    plt.close()

    print("Stage 2 hardware visualization graphs successfully saved to graphs/")

if __name__ == '__main__':
    generate_hardware_graphs()