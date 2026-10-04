# Stage 1 Performance Evaluation Report: NAFTR Routing Algorithm

## 1. Executive Summary
This report presents the Stage 1 comparative performance analysis of the **NAFTR** (Non-minimal Adaptive Fault-Tolerant Routing) algorithm against benchmark routing algorithms, namely **FTXY** and **EDAR**, in Network-on-Chip (NoC) architectures. The primary objective is to evaluate NAFTR's performance in terms of packet latency, fault tolerance under varying link failure rates, and total network power efficiency.

Key evaluation findings:
* **Fault-Free Operations:** NAFTR consistently maintains lower latency at elevated Packet Injection Rates (PIR) compared to FTXY and EDAR[cite: 13].
* **Fault Tolerance:** NAFTR achieves higher Flit Delivery Ratio (FDR) under severe fault conditions (up to 12% link failures), outperforming EDAR by up to 18%[cite: 1, 14].
* **Power Efficiency:** NAFTR reduces total network power consumption by ~41% compared to EDAR in faultless scenarios[cite: 15] and ~5% in faulty scenarios[cite: 15].

---

## 2. Experimental Setup
All simulations were conducted using the **Nirgam NoC Simulator** environment under uniform and synthetic traffic distribution parameters.

| Simulation Parameter | Value / Configuration |
| :--- | :--- |
| **Network Topology** | $5 \times 5$ 2D Mesh[cite: 13] |
| **Routing Algorithms** | FTXY, EDAR, NAFTR[cite: 13] |
| **Traffic Patterns** | Bit-Reversal, Bit-Shuffle, Butterfly, Transpose[cite: 13] |
| **Warm-up Cycles** | 5 cycles[cite: 13] |
| **Simulation Cycles** | 5000 cycles[cite: 13] |
| **Link Fault Rates** | 0% (Fault-free), 3%, 6%, 9%, 12%[cite: 13] |

---

## 3. Fault-Free Evaluation (Latency vs. PIR)
In fault-free networks, average packet latency was evaluated across increasing Packet Injection Rates (PIR)[cite: 13].

### Observations:
* **Low PIR (< 0.10):** All three algorithms display low latency across `Bit-Reversal`, `Bit-Shuffle`, `Butterfly`, and `Transpose` traffic patterns.
* **High PIR (> 0.10):** As network contention increases, FTXY experiences rapid saturation due to its deterministic path assignment. EDAR experiences moderate path delays due to adaptive deflection. NAFTR achieves the lowest average latency by dynamically distributing flits through uncongested non-minimal routes[cite: 13].

*(Refer to generated visual plots: `graphs/Latency_vs_PIR_Bit-Reversal.png`, `graphs/Latency_vs_PIR_Bit-Shuffle.png`, `graphs/Latency_vs_PIR_Butterfly.png`, and `graphs/Latency_vs_PIR_Transpose.png`)*

---

## 4. Faulty Network Evaluation (Flit Delivery Ratio)
To test fault tolerance, link failures were injected at rates of 3%, 6%, 9%, and 12%[cite: 13].

### Observations:
* **0% to 3% Fault Rate:** All routing schemes maintain high Flit Delivery Ratios (> 95%)[cite: 13].
* **6% to 12% Fault Rate:** 
  * **FTXY** drops significant packets as routing paths become blocked by dead links[cite: 13, 14].
  * **EDAR** degrades due to potential livelock scenarios during path deflection[cite: 13].
  * **NAFTR** maintains up to an **18% higher FDR than EDAR** at a 12% fault rate due to priority-based routing rules that eliminate livelocks[cite: 1, 13, 14].

*(Refer to generated visual plots: `graphs/FDR_vs_FaultRate_Bit-Reversal.png`, `graphs/FDR_vs_FaultRate_Bit-Shuffle.png`, `graphs/FDR_vs_FaultRate_Butterfly.png`, and `graphs/FDR_vs_FaultRate_Transpose.png`)*

---

## 5. Power Analysis
Total network power consumption was recorded across fault-free and faulty scenarios[cite: 15].

### Observations:
* **Fault-Free Power:** NAFTR consumes **~41% less power than EDAR** due to reduced routing table overhead and optimal path selection[cite: 15].
* **Faulty Power:** In faulty conditions, NAFTR yields **~5% lower power consumption than EDAR**[cite: 15].

*(Refer to generated bar chart: `graphs/Power_Comparison.png`)*

---

## 6. Stage 1 Conclusion & Next Steps
Stage 1 simulation results validate NAFTR as a highly scalable, fault-tolerant, and power-efficient routing solution for NoC architectures[cite: 1, 13, 15]. 

### Next Steps for Stage 2:
1. Obtain Verilog RTL designs from Member 2 for Hardware Synthesis in Xilinx Vivado.
2. Evaluate Hardware Resource Utilization (LUTs, FFs, $F_{max}$, Dynamic Power).
3. Evaluate system throughput impact following the integration of Packet Collision Detection mechanisms.