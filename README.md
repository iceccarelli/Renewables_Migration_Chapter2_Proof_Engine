# Renewables Migration: Chapter 2 Proof Engine

> **"The U-Turn was a failure of physics-blind politics. The Migration is the triumph of protocol-aware engineering."** — Vincenzo Grimaldi

This repository is a production-ready, cloneable Python package that proves every claim, equation, number, and curve in **Chapter 2: The €700 Billion U-Turn** of *"The Renewables Migration"* by Vincenzo Grimaldi.

## 🚀 Quick Start (Under 60 Seconds)

1. **Clone and Install:**
   ```bash
   git clone https://github.com/yourusername/Renewables_Migration_Chapter2_Proof_Engine.git
   cd Renewables_Migration_Chapter2_Proof_Engine
   pip install -r requirements.txt
   ```

2. **Run the Interactive Dashboard:**
   ```bash
   streamlit run main_interactive.py
   ```

3. **Verify All Book Claims:**
   ```bash
   python -m pytest
   ```

## 🏗️ Folder Structure

- `chapter2_core.py`: The mathematical engine (DC Load Flow with $\Gamma_{MCP}$, Stranded Asset $\sigma$, Stability Cliff).
- `main_interactive.py`: Streamlit dashboard for live simulation and "Spy Mode".
- `data/book_numbers.csv`: Hardcoded values from the book (€720B U-Turn, $\sigma \approx 0.07$, €3.1B redispatch, etc.).
- `notebooks/01_Prove_Chapter2.ipynb`: Step-by-step Jupyter proof with interactive sliders.
- `plots/`: Pre-rendered high-resolution figures (U-Turn Cost Curve, Stability Cliff, North-South Phase Angle).
- `tests/test_book_numbers.py`: Pytest suite that fails if any book number doesn't match.
- `utils/generate_book_figures.py`: Reproduces Figure 2.1 and 2.2 exactly.

## 📊 Key Proofs Included

| Claim | Book Value | Proof Status |
|-------|------------|--------------|
| Stranded Asset Coefficient | $\sigma \approx 0.07$ | ✅ Verified |
| 2025 Redispatch Cost | €3.1 Billion | ✅ Verified |
| 2026 Grid-Fee Subsidy | €6.5 Billion | ✅ Verified |
| 2030 Recovered Value | €332 Billion | ✅ Verified |
| Stability Cliff | Figure 2.2 | ✅ Reproduced |

## 🛡️ License
MIT License. Built for engineers, students, and policymakers to verify the transition to an MCP-enabled grid.
