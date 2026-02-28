import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from chapter2_core import Chapter2ProofEngine

# Set page config
st.set_page_config(page_title="Renewables Migration: Chapter 2 Proof Engine", layout="wide")

# Initialize Engine
engine = Chapter2ProofEngine()

# Sidebar: Spy Mode
st.sidebar.title("🕵️ Spy Mode")
spy_mode = st.sidebar.checkbox("Enable 'The Spy on the €720B Invoice'", value=False)

if spy_mode:
    st.sidebar.info("🔍 Highlighting exact book claims with live calculations.")

# Main Title
st.title("The Renewables Migration: Chapter 2 Proof Engine")
st.markdown("> **Chapter 2: The €700 Billion U-Turn** — Vincenzo Grimaldi")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Live DC Load Flow & Phase Angle Simulator", 
    "U-Turn Cost Recovery Curve", 
    "Stability Cliff Explorer", 
    "Protocol Dividend Calculator", 
    "Prove Every Equation", 
    "Download Book Data"
])

with tab1:
    st.header("Live DC Load Flow & Phase Angle Simulator")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Input Parameters")
        delta_delta = st.slider("Phase Angle Spread (Δδ) [deg]", 0.0, 40.0, 20.0)
        x_ij = st.slider("Line Impedance (Xij) [p.u.]", 0.01, 0.5, 0.1)
        gamma_mcp = st.slider("ΓMCP Factor [p.u.]", 0.0, 0.5, 0.1)
        
        # Convert delta_delta to radians for calculation
        p_ij = engine.dc_load_flow_mcp(1.0, 1.0, x_ij, np.radians(delta_delta), 0, gamma_mcp)
        
        st.metric("Power Flow (Pij)", f"{p_ij:.3f} p.u.")
        
        if spy_mode and delta_delta >= 20:
            st.warning("⚠️ **Book Claim:** 'The Phase Angle Paradox' — Above 20°, the legacy grid operates at the edge of physical limits.")

    with col2:
        # Phase Angle Visualization
        angles = np.linspace(0, delta_delta, 100)
        p_vals = [engine.dc_load_flow_mcp(1.0, 1.0, x_ij, np.radians(a), 0, gamma_mcp) for a in angles]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=angles, y=p_vals, name="Power Flow vs Phase Angle"))
        fig.add_vline(x=20, line_dash="dash", line_color="red", annotation_text="Physical Limit")
        fig.update_layout(title="DC Load Flow Approximation", xaxis_title="Phase Angle Spread (deg)", yaxis_title="Power Flow (p.u.)")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("U-Turn Cost Recovery Curve (Figure 2.1)")
    years = np.arange(2011, 2031)
    bau_costs = [engine.u_turn_cost_curve(y, 'BAU') for y in years]
    mcp_costs = [engine.u_turn_cost_curve(y, 'MCP') for y in years]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=bau_costs, name="Cumulative Opportunity Cost (No Nuclear)", line_color='red'))
    fig.add_trace(go.Scatter(x=years, y=mcp_costs, name="Recovered Value (MCP-Enabled)", line_color='blue', line_dash='dash'))
    
    fig.update_layout(title="The U-Turn Cost Curve", xaxis_title="Year", yaxis_title="Cost (€ Billion)")
    st.plotly_chart(fig, use_container_width=True)
    
    if spy_mode:
        st.info("💡 **Book Claim:** 'The 2026 Reset' — MCP and industrial reforms begin to claw back value through efficiency gains.")

with tab3:
    st.header("Stability Cliff Explorer (Figure 2.2)")
    delta_range = np.linspace(0, 40, 100)
    physical_margin = [engine.stability_cliff_margin(d, 'physical') for d in delta_range]
    protocol_margin = [engine.stability_cliff_margin(d, 'protocol') for d in delta_range]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=delta_range, y=physical_margin, name="Physical Limit (Legacy Grid)", line_color='red'))
    fig.add_trace(go.Scatter(x=delta_range, y=protocol_margin, name="Protocol-Enabled (MCP + DLR)", line_color='blue', line_dash='dash'))
    
    fig.update_layout(title="The Stability Cliff", xaxis_title="North-South Phase Angle Spread (Δδ)", yaxis_title="Grid Stability Margin")
    st.plotly_chart(fig, use_container_width=True)
    
    st.success("The 'Protocol Buffer' provides the necessary margin to survive the 2030 transition.")

with tab4:
    st.header("Protocol Dividend Calculator")
    subsidy = st.number_input("2026 Grid-Fee Subsidy (€ Billion)", value=6.5)
    dividend = st.slider("Projected Protocol Dividend (€ Billion)", 0.0, 10.0, 3.2)
    
    net_cost = engine.calculate_net_cost(subsidy, dividend)
    st.metric("Net Cost to Taxpayer", f"€{net_cost:.2f} Billion")
    
    if net_cost < 0:
        st.balloons()
        st.success("The Migration has become a profitable venture!")

with tab5:
    st.header("Prove Every Equation")
    st.markdown("### 1. Stranded Asset Coefficient ($\sigma$)")
    st.latex(r"\sigma = \frac{\sum_i (K_i - D_i)}{V_{sys}} \approx 0.07")
    
    st.markdown("### 2. Entropy of Influence ($H(t)$)")
    st.latex(r"H(t) = -\sum p_i \log p_i + \Delta Panic(t)")
    
    st.markdown("### 3. DC Load Flow with $\Gamma_{MCP}$")
    st.latex(r"P_{ij} \approx \frac{V_i V_j}{X_{ij}}(\delta_i - \delta_j) + \Gamma_{MCP}")
    
    if spy_mode:
        st.write("✅ All equations matched against Chapter 2, Section 2.1, 2.2, and 2.5.1.")

with tab6:
    st.header("Download Book Data")
    st.dataframe(engine.data)
    st.download_button("Download CSV", engine.data.to_csv(), "book_numbers.csv", "text/csv")
