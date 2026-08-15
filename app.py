import subprocess

import streamlit as st

st.title("Bash Runner")
cmd = st.text_area("Command", value="id", height=150)
if st.button("Run"):
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
    st.code((p.stdout or "") + (p.stderr or ""))
