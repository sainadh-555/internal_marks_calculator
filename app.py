import streamlit as st

st.set_page_config(page_title="Internal Marks Calculator", page_icon="🎓")

st.title("🎓 Internal Marks Calculator")

# Module 1
st.header("Module 1")

pre_t1_m1 = st.number_input("Pre-T1 (out of 10)", 0.0, 10.0)
t1_m1 = st.number_input("T1 (out of 30)", 0.0, 30.0)
ass_m1 = st.number_input("T5 Assignment Average (out of 20)", 0.0, 20.0)

st.divider()

# Module 2
st.header("Module 2")

pre_t1_1 = st.number_input("Pre-T1-1 (out of 10)", 0.0, 10.0)
pre_t1_2 = st.number_input("Pre-T1-2 (out of 10)", 0.0, 10.0)
t1_m2 = st.number_input("T1 (out of 20)", 0.0, 20.0)
t2 = st.number_input("T2 (out of 10)", 0.0, 10.0)
t3 = st.number_input("T3 (out of 10)", 0.0, 10.0)
t4 = st.number_input("T4 (out of 40)", 0.0, 40.0)
ass_m2 = st.number_input("T5 Assignment Average (out of 20)", 0.0, 20.0)

if st.button("Calculate"):

    module_1 = (
        pre_t1_m1 * (5 / 10)
        + t1_m1 * (15 / 30)
        + ass_m1 * (5 / 20)
    )

    module_2 = (
        (pre_t1_1 + pre_t1_2) * (5 / 20)
        + t1_m2 * (10 / 20)
        + t2 * (2.5 / 10)
        + t3 * (2.5 / 10)
        + t4 * (5 / 40)
        + ass_m2 * (10 / 20)
    )

    total = module_1 + module_2

    st.success("Calculation Complete!")

    st.metric("Module 1", f"{module_1:.2f}/25")
    st.metric("Module 2", f"{module_2:.2f}/35")
    st.metric("Total Scaled Marks", f"{total:.2f}/60")
