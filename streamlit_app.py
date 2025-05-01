import streamlit as st
import time
backgroundColor= "#000000"
on = st.toggle("Sigma")
if on:
  st.image("960.webp")

st.write("Smurfik Kombat")
left, middle, right = st.columns(3)


if left.button("Кликнуть", type = "primary"):
   left.markdown("Ты же не думал, что я что то сделал?")