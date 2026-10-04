import subprocess
import os

def run_pipeline():
    print("==========================================")
    print(" Step 1: Parsing Nirgam Simulation Logs ")
    print("==========================================")
    subprocess.run(["python", "scripts/parse_nirgam.py"])

    print("\n==========================================")
    print(" Step 2: Generating Stage 1 Simulation Graphs ")
    print("==========================================")
    subprocess.run(["python", "scripts/generate_graphs.py"])

    print("\n==========================================")
    print(" Step 3: Parsing Stage 2 Vivado Reports ")
    print("==========================================")
    subprocess.run(["python", "scripts/parse_vivado.py"])

    print("\n==========================================")
    print(" Step 4: Generating Stage 2 Hardware Graphs ")
    print("==========================================")
    subprocess.run(["python", "scripts/generate_stage2_graphs.py"])

    print("\n==========================================")
    print(" Pipeline Execution Complete! ")
    print(" Check results/processed/ and graphs/ ")
    print("==========================================")

if __name__ == "__main__":
    run_pipeline()