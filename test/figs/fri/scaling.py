import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio


pio.templates.default = "plotly_white"
scaling_exp = [3, 5, 6, 7]

# actual_data = [[15 + 884, 620.82], [15 + 1631, 6887.41], [25 + 1472, 8354.81]]
conversion_factor = 620 / 811.0e6

N = 20
x = np.logspace(1, 3, num=N)

data = {
    "Method": ["HF/DFT"] * N
    + ["FRI-CCSD (?)"] * N
    + ["MP2"] * N
    + ["CCSD"] * N
    + ["CCSD(T)"] * N,
    "System Size": np.concatenate((x, x, x, x, x)),
    "Computational Time": np.concatenate(
        (
            np.power(x, 3),
            100 * np.power(x, 5),
            np.power(x, 5),
            np.power(x, 6),
            np.power(x, 7),
        )
    )
    * conversion_factor,
}
print(len(data["Method"]), data["System Size"].size, data["Computational Time"].size)


df = pd.DataFrame(data)
fig = px.scatter(
    df, x="System Size", y="Computational Time", color="Method", log_x=True, log_y=True
).update_traces(mode="lines+markers")

# Formatting
fig.update_layout(
    font=dict(size=20),
    yaxis=dict(showexponent="all", exponentformat="e"),
    xaxis=dict(showexponent="all", exponentformat="e"),
    font_family="DejaVu Sans",
    colorway=[  # Matplotlib colors
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
    ],
)
fig.update_xaxes(showline=True, linewidth=2, linecolor="black", mirror=True)
fig.update_yaxes(showline=True, linewidth=2, linecolor="black", mirror=True)

fig.update_traces(marker=dict(size=12))

fig.data[1]["visible"] = "legendonly"
fig.data[1]["marker_symbol"] = "cross"
fig.data[1]["marker_color"] = "#AB63FA"

# fig.show()
fig.write_html("scaling.html")
