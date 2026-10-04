# Stage 2: Packet Collision Detection Integration & FPGA Synthesis Plan

## 1. Stage 2 Overview
In Stage 2, Member 2 will provide Verilog RTL implementations of NAFTR with integrated **Packet Collision Detection** logic. The objective is to evaluate hardware overhead and performance impact.

---

## 2. Hardware Resource & Timing Tracking

When Member 2 synthesizes the designs in Vivado, collect the `.rpt` files under `results/raw/stage2_vivado/<Algorithm>/`:
* `utilization.rpt`
* `timing.rpt`
* `power.rpt`

### Metrics to Track:
| Algorithm Configuration | LUTs | Flip-Flops (FF) | $F_{max}$ (MHz) | Dynamic Power (W) | Total Power (W) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FTXY (Baseline)** | -- | -- | -- | -- | -- |
| **EDAR** | -- | -- | -- | -- | -- |
| **NAFTR (Standard)** | -- | -- | -- | -- | -- |
| **NAFTR + Collision Detection** | -- | -- | -- | -- | -- |

---

## 3. Collision Detection Evaluation Criteria
Evaluating the impact of adding Packet Collision Detection to NAFTR:
1. **Throughput Comparison:** Check if collision detection prevents packet drop retries under heavy traffic contention.
2. **Hardware Area Overhead:** Calculate the percentage increase in LUTs and Flip-Flops.
3. **Frequency Scaling:** Ensure maximum frequency ($F_{max}$) meets timing closure without negative slack (WNS).