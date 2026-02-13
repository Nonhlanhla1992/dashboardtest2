import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Democracy Trends Dashboard")

# Load data
df = pd.read_csv("VDEM_small.csv")

# Measures to show
measures = [
    "electoral_democracy_index",
    "liberal_democracy_index",
    "electoral_fairness_index",
    "vote_buying",
    "freedom_of_expression_index"
]

# Country selector
country = st.selectbox("Select Country", sorted(df["country"].unique()))

# Filter country
c = df[df["country"] == country].sort_values("year")

# ---- Plot Trends ----
st.subheader("Trends Over Time")

fig, ax = plt.subplots(figsize=(9,5))

for m in measures:
    ax.plot(c["year"], c[m], label=m)

ax.legend()
ax.set_xlabel("Year")
ax.set_ylabel("Index Value")
st.pyplot(fig)

# ---- Summary Statistics ----
st.subheader("Summary Statistics")

stats = c[measures].describe().T
st.dataframe(stats)

# ---- Recent Change (last 5 years) ----
st.subheader("Recent 5-Year Change")

recent = c.tail(5)
change = recent[measures].iloc[-1] - recent[measures].iloc[0]
st.write(change.sort_values())

