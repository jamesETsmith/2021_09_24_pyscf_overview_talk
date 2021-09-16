#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle
import matplotlib.ticker as mtick

# Make fake exp convergence data
x = np.array(
    [10.0 ** (x) for x in range(6)] + [10.0 ** (x / 4.0) for x in range(20, 27)]
)
y = -np.log(x) / 10

for xi in x:
    print(xi)
for yi in y:
    print(yi)

# Plotting
plt.figure()
sns.set_palette("muted")
plt.plot(x, y, "o-")

# Tick formatting and limits
plt.xticks([x * 10 ** 6 for x in range(4)])
plt.gca().xaxis.set_major_formatter(mtick.FormatStrFormatter("%.0e"))
plt.xlim(-(10 ** 5), 3.2 * 10 ** 6)
plt.ylim(-1.6, 0.1)

# Save
plt.xlabel("Number of Configurations", fontsize=16)
plt.ylabel("Correlation Energy", fontsize=16)
plt.tight_layout()
# plt.savefig("e_v_dets_1.pdf", dpi=900)

# Highlight regions
variational = plt.Rectangle(
    (-(10 ** 5), -1.6),
    3 * 10 ** 5,
    1.7,
    lw=4,
    fc="r",
    label="Treat Exactly",
    alpha=0.4,
)
plt.gca().add_patch(variational)

# Save
plt.legend(fontsize=16)
plt.tight_layout()
# plt.savefig("e_v_dets_2.pdf", dpi=900)

perturbative = plt.Rectangle(
    (2 * 10 ** 5, -1.6),
    3 * 10 ** 6,
    0.5,
    lw=4,
    fc="c",
    label="Treat Approximately",
    alpha=0.40,
)
plt.gca().add_patch(perturbative)

# Labels and layout
plt.xlabel("Number of Configurations", fontsize=16)
plt.ylabel("Correlation Energy", fontsize=16)
plt.legend(fontsize=16)
plt.tight_layout()
plt.savefig("e_v_dets.png", dpi=900)
