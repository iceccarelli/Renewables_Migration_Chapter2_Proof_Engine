import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import sys

# Add parent directory to path to import chapter2_core
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from chapter2_core import Chapter2ProofEngine

def generate_plots():
    engine = Chapter2ProofEngine(data_path='data/book_numbers.csv')
    os.makedirs('plots', exist_ok=True)

    # 1. U-Turn Cost Curve (Figure 2.1)
    years = np.arange(2011, 2031)
    bau_costs = [engine.u_turn_cost_curve(y, 'BAU') for y in years]
    mcp_costs = [engine.u_turn_cost_curve(y, 'MCP') for y in years]

    plt.figure(figsize=(10, 6))
    plt.plot(years, bau_costs, color='red', linewidth=2, label='Cumulative Opportunity Cost (No Nuclear)')
    plt.plot(years, mcp_costs, color='blue', linewidth=2, linestyle='--', label='Recovered Value (MCP-Enabled)')
    plt.xlabel('Year')
    plt.ylabel('Cost (€ Billion)')
    plt.title('Figure 2.1: The U-Turn Cost Curve')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('plots/u_turn_cost_curve.png', dpi=300)
    plt.close()

    # 2. Stability Cliff (Figure 2.2)
    delta_range = np.linspace(0, 40, 100)
    physical_margin = [engine.stability_cliff_margin(d, 'physical') for d in delta_range]
    protocol_margin = [engine.stability_cliff_margin(d, 'protocol') for d in delta_range]

    plt.figure(figsize=(10, 6))
    plt.plot(delta_range, physical_margin, color='red', linewidth=2, label='Physical Limit (Legacy Grid)')
    plt.plot(delta_range, protocol_margin, color='blue', linewidth=2, linestyle='--', label='Protocol-Enabled (MCP + DLR)')
    plt.xlabel('North-South Phase Angle Spread (Δδ)')
    plt.ylabel('Grid Stability Margin')
    plt.title('Figure 2.2: The Stability Cliff')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('plots/stability_cliff_2d.png', dpi=300)
    plt.close()

    # 3. North-South Phase Angle
    x_ij = 0.1
    gamma_mcp = 0.1
    p_vals = [engine.dc_load_flow_mcp(1.0, 1.0, x_ij, np.radians(d), 0, gamma_mcp) for d in delta_range]
    
    plt.figure(figsize=(10, 6))
    plt.plot(delta_range, p_vals, color='green', linewidth=2)
    plt.axvline(x=20, color='red', linestyle='--', label='Physical Limit (20°)')
    plt.xlabel('Phase Angle Spread (Δδ) [deg]')
    plt.ylabel('Power Flow (Pij) [p.u.]')
    plt.title('North-South Phase Angle vs Power Flow')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('plots/north_south_phase_angle.png', dpi=300)
    plt.close()

    print("All book figures generated in 'plots/' directory.")

if __name__ == "__main__":
    generate_plots()
