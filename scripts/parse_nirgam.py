import os
import re
import glob
import pandas as pd

def parse_single_log(filepath):
    latency = None
    fdr = None
    power = None
    
    with open(filepath, 'r') as file:
        content = file.read()
        
        lat_match = re.search(r'Average\s+latency\s*=\s*([0-9.]+)', content, re.IGNORECASE)
        fdr_match = re.search(r'Flit\s+delivery\s+ratio\s*=\s*([0-9.]+)', content, re.IGNORECASE)
        pwr_match = re.search(r'Total\s+power\s*=\s*([0-9.]+)', content, re.IGNORECASE)
        
        if lat_match:
            latency = float(lat_match.group(1))
        if fdr_match:
            fdr = float(fdr_match.group(1))
        if pwr_match:
            power = float(pwr_match.group(1))
            
    return latency, fdr, power

def process_all_results():
    records = []
    log_files = glob.glob('results/raw/**/*.log', recursive=True)
    
    if not log_files:
        print("No raw log files found in results/raw/ yet.")
        return

    for file_path in log_files:
        filename = os.path.basename(file_path).replace('.log', '')
        parts = filename.split('_')
        
        if len(parts) >= 4:
            traffic, fault, algo, pir = parts[0], parts[1], parts[2], parts[3]
            latency, fdr, power = parse_single_log(file_path)
            
            records.append({
                'Traffic': traffic,
                'FaultRate': float(fault),
                'Algorithm': algo,
                'PIR': float(pir),
                'Latency': latency,
                'FDR': fdr,
                'Power': power
            })
            
    df = pd.DataFrame(records)
    
    output_dir = 'results/processed'
    os.makedirs(output_dir, exist_ok=True)
    
    output_csv = os.path.join(output_dir, 'summary_results.csv')
    df.to_csv(output_csv, index=False)
    print(f"Successfully processed {len(records)} log files -> Saved to {output_csv}")

if __name__ == '__main__':
    process_all_results()