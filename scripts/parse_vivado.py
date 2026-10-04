import os
import re
import pandas as pd

def parse_vivado_reports(utilization_rpt, timing_rpt, power_rpt):
    """
    Parses Vivado utilization, timing, and power text reports to extract hardware metrics.
    """
    metrics = {
        'LUTs': None,
        'FlipFlops': None,
        'Fmax_MHz': None,
        'Dynamic_Power_W': None,
        'Total_Power_W': None
    }

    # 1. Parse Utilization Report (.rpt)
    if os.path.exists(utilization_rpt):
        with open(utilization_rpt, 'r') as f:
            content = f.read()
            lut_match = re.search(r'LUT as Logic\s*\|\s*(\d+)', content)
            ff_match = re.search(r'Register as Flip Flop\s*\|\s*(\d+)', content)
            
            if lut_match:
                metrics['LUTs'] = int(lut_match.group(1))
            if ff_match:
                metrics['FlipFlops'] = int(ff_match.group(1))

    # 2. Parse Timing Report (.rpt)
    if os.path.exists(timing_rpt):
        with open(timing_rpt, 'r') as f:
            content = f.read()
            wns_match = re.search(r'Worst Negative Slack \(WNS\):\s*(-?[0-9.]+)\s*ns', content)
            period_match = re.search(r'Requirement:\s*([0-9.]+)\s*ns', content)
            
            if wns_match and period_match:
                wns = float(wns_match.group(1))
                period = float(period_match.group(1))
                actual_period = period - wns
                if actual_period > 0:
                    metrics['Fmax_MHz'] = round(1000.0 / actual_period, 2)

    # 3. Parse Power Report (.rpt)
    if os.path.exists(power_rpt):
        with open(power_rpt, 'r') as f:
            content = f.read()
            dyn_match = re.search(r'Dynamic \(W\)\s*\|\s*([0-9.]+)', content)
            tot_match = re.search(r'Total On-Chip Power \(W\)\s*\|\s*([0-9.]+)', content)
            
            if dyn_match:
                metrics['Dynamic_Power_W'] = float(dyn_match.group(1))
            if tot_match:
                metrics['Total_Power_W'] = float(tot_match.group(1))

    return metrics

def process_stage2_results():
    reports_dir = 'results/raw/stage2_vivado'
    
    if not os.path.exists(reports_dir):
        print(f"Directory {reports_dir} does not exist yet. Create it or wait for Member 2's synthesis reports.")
        return

    records = []
    # Scanning subfolders in results/raw/stage2_vivado/ for algorithm implementations
    for algo_dir in os.listdir(reports_dir):
        full_path = os.path.join(reports_dir, algo_dir)
        if os.path.isdir(full_path):
            util_rpt = os.path.join(full_path, 'utilization.rpt')
            time_rpt = os.path.join(full_path, 'timing.rpt')
            pwr_rpt = os.path.join(full_path, 'power.rpt')
            
            metrics = parse_vivado_reports(util_rpt, time_rpt, pwr_rpt)
            metrics['Algorithm'] = algo_dir
            records.append(metrics)

    if records:
        df = pd.DataFrame(records)
        output_dir = 'results/processed'
        os.makedirs(output_dir, exist_ok=True)
        out_csv = os.path.join(output_dir, 'stage2_hardware_summary.csv')
        df.to_csv(out_csv, index=False)
        print(f"Stage 2 Hardware Metrics parsed successfully -> Saved to {out_csv}")
    else:
        print("No synthesis subfolders found inside results/raw/stage2_vivado/.")

if __name__ == '__main__':
    process_stage2_results()