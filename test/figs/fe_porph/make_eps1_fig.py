import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


plt.figure()
# sns.set_style("darkgrid")
sns.set_context("talk")
sns.set_palette("muted")

err_scf = [0.0136, 0.0193, 0.0334]
err_shci = [0, 1e-4, 1e-4]

plt.plot(err_scf, "o-", label="MCSCF")

plt.title("Energy Error")
plt.ylabel("Error (Ha)")
plt.xticks(
    [0, 1, 2],
    [
        "HCISCF\n($\epsilon_1=5e-5)$",
        "vHCISCF\n($\epsilon_1=5e-5)$",
        "vHCISCF\n($\epsilon_1=1e-4)$",
    ],
)
plt.ylim((-0.002, 0.035))
plt.legend()
plt.tight_layout()
plt.savefig("fe_p_eps1.png", dpi=600)


plt.plot(err_shci, "o-", label="Final SHCI")
plt.legend()
plt.savefig("fe_p_eps2.png", dpi=600)
