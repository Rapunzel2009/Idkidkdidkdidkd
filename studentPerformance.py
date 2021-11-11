import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data.csv")

student_df = df.loc[df["student_id"] == "TRL_xsl"]

print(student_df.groupby("level")["attempt"].mean())
