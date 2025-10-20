import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from logic_behavior import logic_behavior
from promoter_hill import hill_expression
from enzyme_kinetics import enzyme_model
from system_logic import system_dynamics


st.set_page_config(page_title="Biospray Simulations", layout="wide")
st.title("🧬 Interactive Models for PAH Detecting and Degrading Biospray")

tab0, tab1, tab2, tab3 = st.tabs(["Logic Gate Behavior", "Promoter Activation", "Enzyme Kinetics", "System-Level Logic"])

#0. Logic Gate Behavior
with tab0:
    st.subheader("Logic Gate Behavior Simulation")

    col1, col2 = st.columns([1,2])
    with col1:
        st.write("This simulation shows Boolean interactions between the pollutant (P), kill-switch (K), and degradation module (D).")
        st.write("1 = ON, 0 = OFF. The biosafety circuit ensures degradation activates only when pollutant is present, and the kill-switch activates when pollutant is absent.")

    with col2:
        t, P, K, D = logic_behavior()
        fig, ax = plt.subplots(figsize=(4.5,2))
        ax.step(t, P, label='Pollutant (P)', linewidth=2)
        ax.step(t, D, label='Degradation (D)', linewidth=2)
        ax.step(t, K, label='Kill-switch (K)', linewidth=2)
        ax.set_xlabel("Time (arbitrary units)", fontsize=9)
        ax.set_ylabel("Logic state (0/1)", fontsize=9)
        ax.set_title("Genetic Circuit Logic Behavior", fontsize=10, pad=4)
        ax.tick_params(labelsize=8)
        ax.set_yticks([0,1])
        ax.legend(fontsize=8, frameon=False)
        ax.grid(True, linewidth=0.4)
        st.pyplot(fig, use_container_width=True)

# 1. Promoter activation
with tab1:
    st.subheader("Promoter activation (Hill function)")
    col1, col2 = st.columns([1, 2])

    with col1:
        Emax = st.slider('Emax (max expression)', 0.5, 2.0, 1.0, 0.1)
        Kd = st.slider('Kd (half activation constant)', 0.5, 5.0, 2.0, 0.1)
        n = st.slider('Hill coefficient (n)', 1.0, 4.0, 2.0, 0.5)

    with col2:
        PAH, Expr = hill_expression(Emax, Kd, n)
        fig, ax = plt.subplots(figsize=(4.5,2.5))   
        ax.plot(PAH, Expr, linewidth=2, color='royalblue')
        ax.set_xlabel("PAH concentration (a.u.)", fontsize=9)
        ax.set_ylabel("Normalized output", fontsize=9)
        ax.set_title("Promoter activation curve", fontsize=10, pad=4)
        ax.tick_params(labelsize=8)
        ax.grid(True, linewidth=0.4)
        st.pyplot(fig, use_container_width=True)


#  2. Enzyme kinetics
with tab2:
    st.subheader("Enzyme kinetics: multi-step PAH degradation")
    col1, col2 = st.columns([1, 2])

    with col1:
        V1 = st.slider("Vmax₁ (laccase)", 0.1, 2.0, 1.0, 0.1)
        Km1 = st.slider("Km₁", 0.1, 1.0, 0.5, 0.1)
        V2 = st.slider("Vmax₂ (RHD)", 0.1, 2.0, 0.8, 0.1)
        Km2 = st.slider("Km₂", 0.1, 1.0, 0.3, 0.1)
        S0 = st.slider("Initial PAH concentration", 5.0, 20.0, 10.0, 1.0)

    with col2:
        t, S, I, P = enzyme_model(V1, Km1, V2, Km2, S0)
        fig, ax = plt.subplots(figsize=(4.5,2.5))
        ax.plot(t, S, label='PAH (S)', linewidth=2)
        ax.plot(t, I, '--', label='Intermediate (I)', linewidth=2)
        ax.plot(t, P, ':', label='Product (P)', linewidth=2)
        ax.set_xlabel("Time (h)", fontsize=9)
        ax.set_ylabel("Concentration (a.u.)", fontsize=9)
        ax.set_title("Multi-step PAH degradation", fontsize=10, pad=4)
        ax.tick_params(labelsize=8)
        ax.legend(fontsize=8, frameon=False)
        ax.grid(True, linewidth=0.4)
        st.pyplot(fig, use_container_width=True)


# 3. System-level logic
with tab3:
    st.subheader("System-level pollutant / kill-switch dynamics")
    col1, col2 = st.columns([1, 2])

    with col1:
        decay = st.slider("PAH decay rate", 0.1, 1.0, 0.3, 0.05)
        threshold = st.slider("Kill-switch threshold", 0.01, 0.5, 0.1, 0.01)

    with col2:
        t, PAH, Enz, Kill = system_dynamics(decay, threshold)
        fig, ax = plt.subplots(figsize=(4.5,2.5))
        ax.plot(t, PAH, label='PAH', linewidth=2)
        ax.plot(t, Enz, label='Enzyme', linewidth=2)
        ax.plot(t, Kill, label='Kill-switch', linewidth=2)
        ax.set_xlabel("Time (h)", fontsize=9)
        ax.set_ylabel("Normalized level", fontsize=9)
        ax.set_title("Integrated system response", fontsize=10, pad=4)
        ax.tick_params(labelsize=8)
        ax.legend(fontsize=8, frameon=False)
        ax.grid(True, linewidth=0.4)
        st.pyplot(fig, use_container_width=True)



st.markdown("---")
st.caption("Built with Streamlit • Models simplified from the synthetic biology project by [Syeda Afia Shah]")
