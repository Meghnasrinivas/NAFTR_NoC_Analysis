import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 11})

# Create graphs directory if it doesn't exist
os.makedirs('graphs', exist_ok=True)

# Load processed data
csv_path = 'results/processed/summary_results.csv'

if not os.path.exists(csv_path):
    print(f"Error: {csv_path} not found. Run parse_nirgam.py first!")
    exit()

df = pd.read_csv(csv_path)

# ==========================================
# 1. LATENCY VS PIR (Fault-Free Scenario)
# ==========================================
fault_free_df = df[df['FaultRate'] == 0]

if not fault_free_df.empty:
    traffics = fault_free_df['Traffic'].unique()
    for traffic in traffics:
        plt.figure(figsize=(7, 5))
        sub_df = fault_free_df[fault_free_df['Traffic'] == traffic]
        
        sns.lineplot(
            data=sub_df, 
            x='PIR', 
            y='Latency', 
            hue='Algorithm', 
            marker='o', 
            linewidth=2
        )
        
        plt.title(f'Average Latency vs Packet Injection Rate ({traffic} - Fault Free)')
        plt.xlabel('Packet Injection Rate (PIR)')
        plt.ylabel('Average Latency (Cycles/Flit)')
        plt.tight_layout()
        
        save_path = f'graphs/Latency_vs_PIR_{traffic}.png'
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"Saved: {save_path}")

# ==========================================
# 2. FLIT DELIVERY RATIO (FDR) VS FAULT RATE
# ==========================================
if not df.empty:
    traffics = df['Traffic'].unique()
    for traffic in traffics:
        plt.figure(figsize=(7, 5))
        sub_df = df[df['Traffic'] == traffic]
        
        sns.lineplot(
            data=sub_df, 
            x='FaultRate', 
            y='FDR', 
            hue='Algorithm', 
            marker='s', 
            linewidth=2
        )
        
        plt.title(f'Flit Delivery Ratio (FDR) vs Fault Rate ({traffic})')
        plt.xlabel('Fault Rate (%)')
        plt.ylabel('Flit Delivery Ratio (%)')
        plt.tight_layout()
        
        save_path = f'graphs/FDR_vs_FaultRate_{traffic}.png'
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"Saved: {save_path}")

# ==========================================
# 3. POWER CONSUMPTION COMPARISON
# ==========================================
if 'Power' in df.columns and not df['Power'].isnull().all():
    plt.figure(figsize=(8, 5))
    
    sns.barplot(
        data=df, 
        x='Algorithm', 
        y='Power', 
        hue='FaultRate', 
        ci=None
    )
    
    plt.title('Total Network Power Consumption Comparison')
    plt.xlabel('Routing Algorithm')
    plt.ylabel('Power (Watts)')
    plt.tight_layout()
    
    save_path = 'graphs/Power_Comparison.png'
    plt.savefig(save_path, dpi=300)
    plt.close()
    print(f"Saved: {save_path}")

print("All graphs successfully generated in graphs/ directory.")