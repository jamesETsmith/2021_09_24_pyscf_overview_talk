import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

fermi = 4
levels = [x / 10 for x in range(-fermi, 6)]

x = np.linspace(1, 3, 10)

fig = plt.figure(figsize=(6, 9))
ax = plt.axes()

for i in range(len(levels)):
    # Plot energy levels
    plt.plot(x, [levels[i]] * 10, c="k", lw=2)

    # Plot electron arrow (leave valence orbital partially occupied)
    if levels[i] < 0:
        ax.arrow(
            1.5,
            levels[i] - 0.025,
            0,
            0.05,
            lw=4,
            head_width=0.1,
            head_length=0.01,
            fc="k",
            ec="k",
        )

    if i < fermi - 1:
        ax.arrow(
            2.5,
            levels[i] + 0.035,
            0,
            -0.05,
            lw=4,
            head_width=0.1,
            head_length=0.01,
            fc="k",
            ec="k",
        )

# Highlight active space
active = plt.Rectangle((0, -0.25), 4, 0.5, lw=4, ec="r", fc="w", label="Active")
plt.gca().add_patch(active)

# # Highlight inactive orbitals
# inactive = plt.Rectangle((0, -0.45), 4, 0.18, lw=4, ec="b", fc="w", label="Inactive")
# plt.gca().add_patch(inactive)

# # Highlight virtual orbitals
# virtual = plt.Rectangle((0, 0.27), 4, 0.3, lw=4, ec="g", fc="w", label="Virtual")
# plt.gca().add_patch(virtual)

# Axis ticks and labels
plt.gca().get_xaxis().set_visible(False)
plt.ylabel("Energy", fontsize=18)

# Axis limits and layout
plt.xlim(-4, 9)
plt.ylim(-0.5, 0.6)
plt.tight_layout()
plt.legend(fontsize=16)

# plt.show()
plt.savefig("mo.png", dpi=900)
