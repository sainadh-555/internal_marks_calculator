import streamlit as st

st.set_page_config(page_title="Marks Calculator", page_icon="🎓")

st.title("Internal Marks Scale Down Calculator 🎓")

st.divider()

# --- Mode Selection using Tabs ---
tab1, tab2 = st.tabs(["Regular Sem Based", "Practice Based (Assignments Only)"])

with tab1:
    st.write("Enter your marks below to calculate the scaled down internal marks.")
    # --- Module 1 Inputs ---
    st.header("Module 1")
    col1, col2 = st.columns(2)
    with col1:
        pre_t1_m1 = st.text_input("Pre-T1 Marks", key="m1_pre_t1")
    with col2:
        t1_m1 = st.text_input("T1 (MID) Marks", key="m1_t1")

    assignment_m1_input = st.text_input("Assignment Marks (separated by spaces)", placeholder="e.g. 18 19 20", key="m1_ass")

    st.divider()

    # --- Module 2 Inputs ---
    st.header("Module 2")
    col3, col4 = st.columns(2)
    with col3:
        pre_t1_1_m2 = st.text_input("Pre-T1-1 Marks", key="m2_pre_t1_1")
        t1_m2 = st.text_input("T1 (MID) Marks", key="m2_t1")
        t3 = st.text_input("T3 Marks (Combined T3-1 & T3-2 out of 10)", key="m2_t3")
    with col4:
        pre_t1_2_m2 = st.text_input("Pre-T1-2 Marks", key="m2_pre_t1_2")
        t2 = st.text_input("T2 Marks (Combined T2-1 & T2-2 out of 10)", key="m2_t2")
        t4 = st.text_input("T4 Marks (out of 40)", key="m2_t4")

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
            val_pre_t1_m1 = int(pre_t1_m1 or 0)
            val_t1_m1 = int(t1_m1 or 0)
            val_pre_t1_1_m2 = int(pre_t1_1_m2 or 0)
            val_pre_t1_2_m2 = int(pre_t1_2_m2 or 0)
            val_t1_m2 = int(t1_m2 or 0)
            val_t2 = int(t2 or 0)
            val_t3 = int(t3 or 0)
            val_t4 = int(t4 or 0)

            module_1 = (val_pre_t1_m1 + val_t1_m1) * 0.5 + ass_m1_avg * (5 / 20)
            module_2 = (val_pre_t1_1_m2 + val_pre_t1_2_m2) * 0.25 + (val_t1_m2) * 0.5 + (val_t2 + val_t3) * 0.5 + (val_t4 * 5) / 8 + ass_m2_avg * (10 / 20)
            
            scaled_marks = module_1 + module_2

            # Display Results
            st.subheader("Results 🎉")
            res_col1, res_col2, res_col3 = st.columns(3)
            res_col1.metric("Module 1", f"{module_1:.2f}")
            res_col2.metric("Module 2", f"{module_2:.2f}")
            res_col3.metric("Total Scaled Marks", f"{scaled_marks:.2f}")
            
            # Show celebration animation
            st.balloons()

        except ValueError:
            st.error("Please ensure all marks are entered as valid numbers.")

with tab2:
    st.header("Practice Based Subjects")
    
    prac_ass_m1_input = st.text_input("Module 1 Assignment Marks (separated by spaces)", placeholder="e.g. 18 19 20", key="prac_m1_ass")
    max_marks_m1 = st.number_input("Max Marks for each assignment in Module 1",min_value=20, step=1,key="m1_max_marks")

    prac_ass_m2_input = st.text_input("Module 2 Assignment Marks (separated by spaces)", placeholder="e.g. 18 19 20", key="prac_m2_ass")
    max_marks_m2 = st.number_input("Max Marks for each assignment in Module 2",min_value=20, step=1, key="m2_max_marks")
    
    st.divider()
    
    if st.button("Calculate Practice Marks", type="primary", use_container_width=True):
        try:
            ass_m1 = [int(x) for x in prac_ass_m1_input.split()] if prac_ass_m1_input.strip() else []
            ass_m1_avg = sum(ass_m1) / len(ass_m1) if ass_m1 else 0

            ass_m2 = [int(x) for x in prac_ass_m2_input.split()] if prac_ass_m2_input.strip() else []
            ass_m2_avg = sum(ass_m2) / len(ass_m2) if ass_m2 else 0

            # Calculations
            module_1 = ass_m1_avg * (25 / max_marks_m1) if max_marks_m1 else 0
            module_2 = ass_m2_avg * (35 / max_marks_m2) if max_marks_m2 else 0
            
            scaled_marks = module_1 + module_2
            
            # Display Results
            st.subheader("Results 🎉")
            res_col1, res_col2, res_col3 = st.columns(3)
            res_col1.metric("Module 1", f"{module_1:.2f}")
            res_col2.metric("Module 2", f"{module_2:.2f}")
            res_col3.metric("Total Scaled Marks", f"{scaled_marks:.2f}")
            
            # Show celebration animation
            st.snow()

        except ValueError:
            st.error("Please ensure all marks are entered as valid numbers.")
