import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from models.promoter_hill import hill_expression
from models.enzyme_kinetics import enzyme_model
from models.system_logic import system_dynamics

st.set_page_config(page_title="Biospray Simulations", layout="wide")
st.title("🧬 PAH-Detecting & Degrading Biospray — Interactive Models")

tab1, tab2, tab3 = st.tabs(["Promoter Activation", "Enzyme Kinetics", "System-Level Logic"])

# ── 1. Promoter activation ─────────────────────────────────────────────────────
with tab1:
    st.subheader("Promoter activation (Hill function)")
    Emax = st.slider('Emax (max expression)', 0.5, 2.0, 1.0, 0.1)
    Kd = st.slider('Kd (half activation constant)', 0.5, 5.0, 2.0, 0.1)
    n = st.slider('Hill coefficient (n)', 1.0, 4.0, 2.0, 0.5)

    PAH, Expr = hill_expression(Emax, Kd, n)
    fig, ax = plt.subplots()
    ax.plot(PAH, Expr, linewidth=2, color='royalblue')
    ax.set_xlabel("PAH concentration (a.u.)")
    ax.set_ylabel("Normalized promoter output")
    ax.set_title("Promoter activation curve")
    ax.grid(True)
    st.pyplot(fig)

# ── 2. Enzyme kinetics ─────────────────────────────────────────────────────────
with tab2:
    st.subheader("Enzyme kinetics: multi-step PAH degradation")
    V1 = st.slider("Vmax₁ (laccase)", 0.1, 2.0, 1.0, 0.1)
    Km1 = st.slider("Km₁", 0.1, 1.0, 0.5, 0.1)
    V2 = st.slider("Vmax₂ (RHD)", 0.1, 2.0, 0.8, 0.1)
    Km2 = st.slider("Km₂", 0.1, 1.0, 0.3, 0.1)
    S0 = st.slider("Initial PAH concentration", 5.0, 20.0, 10.0, 1.0)

    t, S, I, P = enzyme_model(V1, Km1, V2, Km2, S0)
    fig, ax = plt.subplots()
    ax.plot(t, S, label='PAH (S)', linewidth=2)
    ax.plot(t, I, '--', label='Intermediate (I)', linewidth=2)
    ax.plot(t, P, ':', label='Product (P)', linewidth=2)
    ax.set_xlabel("Time (h)")
    ax.set_ylabel("Concentration (a.u.)")
    ax.set_title("Simulated multi-step PAH degradation")
    ax.legend(); ax.grid(True)
    st.pyplot(fig)

# ── 3. System-level logic ──────────────────────────────────────────────────────
with tab3:
    st.subheader("System-level pollutant / kill-switch dynamics")
    decay = st.slider("PAH decay rate", 0.1, 1.0, 0.3, 0.05)
    threshold = st.slider("Kill-switch threshold", 0.01, 0.5, 0.1, 0.01)
    t, PAH, Enz, Kill = system_dynamics(decay, threshold)

    fig, ax = plt.subplots()
    ax.plot(t, PAH, label='PAH', linewidth=2)
    ax.plot(t, Enz, label='Enzyme', linewidth=2)
    ax.plot(t, Kill, label='Kill-switch', linewidth=2)
    ax.set_xlabel("Time (h)")
    ax.set_ylabel("Normalized level")
    ax.set_title("Integrated system response")
    ax.legend(); ax.grid(True)
    st.pyplot(fig)

st.markdown("---")
st.caption("Built with Streamlit • Models simplified from the synthetic biology project by [Your Name]")
