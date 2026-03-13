import streamlit as st
import pandas as pd

st.set_page_config(page_title="Consumer Search", layout="centered")

st.title("Genus Daily Billing Status")

# data load
df = pd.read_csv("data_for_web_from.csv")

search = st.text_input("**Search WFM_CONSUMER_NO / CCB_ACCT_ID / CCB_METER_NO**")
# st.markdown("**Search Consumer Number / RMS ACC / RMS MTR**")
# search = st.text_input("")

if search:

    result = df[
        df["Consumer Number"].astype(str).str.contains(search) |
        df["RMS ACC"].astype(str).str.contains(search) |
        df["RMS MTR"].astype(str).str.contains(search)
    ]

    if not result.empty:

        row = result.iloc[0]

        st.subheader("**Consumer Details**")

        # st.text_input("**WFM_COSNUMER_NO**", row["Consumer Number"], disabled=True)
        # st.text_input("**CCB_ACCT_ID**", int(row["RMS ACC"]), disabled=True)
        # st.text_input("**CCB_METER_NO**", row["RMS MTR"], disabled=True)

        # st.subheader("Consumer Details")

        # st.markdown(f"<b style='color:green;'>WFM_COSNUMER_NO: {row['Consumer Number']}</b>", unsafe_allow_html=True)
        # st.markdown(f"<b style='color:blue;'>CCB_ACCT_ID: {int(row['RMS ACC'])}</b>", unsafe_allow_html=True)
        # st.markdown(f"<b style='color:red;'>CCB_METER_NO: {row['RMS MTR']}</b>", unsafe_allow_html=True)


        # row = result.iloc[0]

        # st.subheader("Consumer Details")

        # st.markdown(
        #     f"<b>WFM_COSNUMER_NO</b><br><span style='color:red; font-weight:bold;'>{row['Consumer Number']}</span>",
        #     unsafe_allow_html=True
        # )

        # st.markdown(
        #     f"<b>CCB_ACCT_ID</b><br><span style='color:red; font-weight:bold;'>{int(row['RMS ACC'])}</span>",
        #     unsafe_allow_html=True
        # )

        # st.markdown(
        #     f"<b>CCB_METER_NO</b><br><span style='color:red; font-weight:bold;'>{row['RMS MTR']}</span>",
        #     unsafe_allow_html=True
        # )

        st.markdown("""
        <style>
        input[disabled] {
            color: green !important;
            font-weight: bold !important;
        }
        </style>
        """, unsafe_allow_html=True)


        st.markdown("**WFM_COSNUMER_NO**")
        st.text_input("WFM_COSNUMER_NO", row["Consumer Number"], disabled=True, label_visibility="collapsed")

        st.markdown("**CCB_ACCT_ID**")
        st.text_input("CCB_ACCT_ID", int(row["RMS ACC"]), disabled=True, label_visibility="collapsed")

        st.markdown("**CCB_METER_NO**")
        st.text_input("CCB_METER_NO", row["RMS MTR"], disabled=True, label_visibility="collapsed")
    
    
    else:
        st.error("Record Not Found")
