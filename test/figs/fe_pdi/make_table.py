import pandas as pd

df = pd.read_csv("1_A.csv", index_col=0)
cols = [
    "DFT Opt. Strategy",
    "UHF Opt. Strategy",
    "Stable",
    "Energy (Ha)",
    "Fe Spin Density",
    "<S^2>",
    "HONO-1",
    "HONO",
    "LUNO",
    "LUNO+1",
]
df = df[cols]
df = df[df["Stable"] == True]
print(df)
formatters = {
    "Energy (Ha)": lambda x: f"{x:.6f}",
    "Fe Spin Density": lambda x: f"{x:.2f}",
    "<S^2>": lambda x: f"{x:.2f}",
    "HONO-1": lambda x: f"{x:.2f}",
    "HONO": lambda x: f"{x:.2f}",
    "LUNO": lambda x: f"{x:.2f}",
    "LUNO+1": lambda x: f"{x:.2f}",
}
df.to_html("1_A.html", index=False, formatters=formatters)
