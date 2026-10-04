# NAFTR vs. FTXY and EDAR Performance Metrics Comparison

This table outlines the expected target metrics based on the base paper evaluation findings.

| Evaluation Aspect | FTXY | EDAR | NAFTR (Target Results) |
| :--- | :--- | :--- | :--- |
| **Fault-Free Latency** | Baseline | Moderate | Lowest under high injection rates |
| **Livelock Prevention** | No | Susceptible | Guaranteed via priority rules |
| **High Fault FDR (%)** | Low | Moderate | Up to **18% higher** than EDAR |
| **Fault-Free Power** | Baseline | High | **~41% lower** than EDAR |
| **Faulty Power** | Baseline | High | **~5% lower** than EDAR |

## Target Verification Checklist
- [ ] Confirm NAFTR maintains lower average flit latency compared to FTXY at high Packet Injection Rates (PIR)[cite: 13].
- [ ] Verify Flit Delivery Ratio (FDR) under 3%, 6%, 9%, and 12% link fault rates[cite: 13, 14].
- [ ] Validate power consumption reduction across all traffic patterns (`Bit-Reversal`, `Bit-Shuffle`, `Butterfly`, `Transpose`)[cite: 13, 15].