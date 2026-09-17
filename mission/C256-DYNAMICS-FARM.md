# CEREBRON OMEGA — COLLATZ DYNAMICS FARM — CHECKPOINT 2026-09-17

MISSION: attack the arbitrary-N cycle problem through exact inter-run dynamics. Do not restart; do not claim solution without universal contradiction.

Exact state:
- Binary critical runs 1^{u_j}2^{r_j}; U=sum u_j, R=sum r_j, delta=R ln(4/3)-U ln(3/2)>0.
- H-factorization: 3^{u_j}t_j-1=4^{r_j}h_j; 2^{u_{j+1}}t_{j+1}-1=3^{r_j}h_j.
- H-COUPLING: 2^{u_{j+1}+2r_{j+1}}h_{j+1}-3^{u_{j+1}+r_j}h_j=3^{u_{j+1}}-2^{u_{j+1}}.
- H-LOG: delta=sum ln[(1+(3^{r_j}h_j)^(-1))/(1+(4^{r_j}h_j)^(-1))].

Primary target: study the transition map (u_j,r_j,h_j)->(u_{j+1},r_{j+1},h_{j+1}). Seek exact monotonicity, forbidden transitions, Lyapunov-like resources, regeneration obstructions, or a collective cost preventing cyclic closure.

Mandatory tests: u=1, r=1, h=5,11,17; imprimitive words; negative/positive block compensation; counterexamples to any claimed uniform monotonicity.

Firewall: if a derivation merely reconstructs Dx=C or D|C, classify EQUIVALENT-HARDNESS.

ARITHMETIC COMPRESSION: SYMBOLIC REDUCTION BEFORE MULTIPLICATION. Use recurrence/caching for powers, factor common terms, eliminate variables before expansion, modular filters before big integers, and exact/logarithmic stable forms where justified. Report arithmetic cost before/after and proof of equivalence.

Output: ESTABLISHED / NEW DYNAMIC LEMMA / COUNTEREXAMPLE / AUDIT / RESIDUAL / NEXTLOCK / STATUS. COMPUTATION != PROOF; FINITE TEST != UNIVERSAL PROOF.