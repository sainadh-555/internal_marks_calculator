import streamlit as st

st.set_page_config(page_title="Marks Calculator", page_icon="🎓")

st.title("Internal Marks Scale Down Calculator 🎓")
st.write("Enter your marks below to calculate the scaled down internal marks.")

st.divider()

# --- Module 1 Inputs ---
st.header("Module 1")
col1, col2 = st.columns(2)
with col1:
    pre_t1_m1 = st.number_input("Pre-T1 Marks", min_value=0, step=1, key="m1_pre_t1")
with col2:
    t1_m1 = st.number_input("T1 (MID) Marks", min_value=0, step=1, key="m1_t1")

assignment_m1_input = st.text_input("Assignment Marks (separated by spaces)", placeholder="e.g. 18 19 20", key="m1_ass")

st.divider()

# --- Module 2 Inputs ---
st.header("Module 2")
col3, col4 = st.columns(2)
with col3:
    pre_t1_1_m2 = st.number_input("Pre-T1-1 Marks", min_value=0, step=1, key="m2_pre_t1_1")
    t1_m2 = st.number_input("T1 (MID) Marks", min_value=0, step=1, key="m2_t1")
    t3 = st.number_input("T3 Marks (Combined T3-1 & T3-2 out of 10)", min_value=0, step=1, key="m2_t3")
with col4:
    pre_t1_2_m2 = st.number_input("Pre-T1-2 Marks", min_value=0, step=1, key="m2_pre_t1_2")
    t2 = st.number_input("T2 Marks (Combined T2-1 & T2-2 out of 10)", min_value=0, step=1, key="m2_t2")
    t4 = st.number_input("T4 Marks (out of 40)", min_value=0, step=1, key="m2_t4")

assignment_m2_input = st.text_input("Assignment Marks (separated by spaces)", placeholder="e.g. 18 19 20", key="m2_ass")

st.divider()

# --- Calculation Button ---
if st.button("Calculate Scaled Marks", type="primary", use_container_width=True):
    try:
        # Process Assignments
        ass_m1 = [int(x) for x in assignment_m1_input.split()] if assignment_m1_input.strip() else []
        ass_m1_avg = sum(ass_m1) / len(ass_m1) if ass_m1 else 0

        ass_m2 = [int(x) for x in assignment_m2_input.split()] if assignment_m2_input.strip() else []
        ass_m2_avg = sum(ass_m2) / len(ass_m2) if ass_m2 else 0

        # Calculations
        module_1 = (pre_t1_m1 + t1_m1) * 0.5 + ass_m1_avg * (5 / 20)
        module_2 = ((pre_t1_1_m2 + pre_t1_2_m2) * 0.25)+ ((t1_m2) * 0.5) + ((t2 + t3) * 0.25) + (t4 / 8) + (ass_m2_avg * (10/20))
        
        scaled_marks = module_1 + module_2

        # Display Results
        st.subheader("Results 🎉")
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("Module 1", f"{module_1:.2f}")
        res_col2.metric("Module 2", f"{module_2:.2f}")
        res_col3.metric("Total Scaled Marks", f"{scaled_marks:.2f}")

    except ValueError:
        st.error("Please ensure all assignment marks are entered as numbers separated by spaces (e.g. '18 19 20').")
