import numpy as np
import plotly.graph_objects as go
import plotly.express as px


# Make fake exp convergence data
x = np.array(
    [10.0 ** (x) for x in range(6)] + [10.0 ** (x / 4.0) for x in range(20, 27)]
)
y = -np.log(x) / 10


# Create figure
fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y))

# Add traces, one for each slider step
for step in np.arange(0, 5, 0.1):
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=6),
            name="𝜈 = " + str(step),
            x=np.arange(0, 10, 0.01),
            y=np.sin(step * np.arange(0, 10, 0.01)),
        )
    )

# Make 10th trace visible
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[
            {"visible": [False] * len(fig.data)},
            {"title": "Slider switched to step: " + str(i)},
        ],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [
    dict(active=10, currentvalue={"prefix": "Frequency: "}, pad={"t": 50}, steps=steps)
]

fig.update_layout(sliders=sliders)

fig.show()
