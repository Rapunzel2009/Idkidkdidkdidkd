import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data.csv")

print(df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x = df.groupby("level")["attempt"].mean(),
    y = ["Level1","Level2","Level3","Level4"],
    orientation = "f"
))
fig.show()
