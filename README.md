# Constrained convex optimisation

## Why?
Constrained convex optimisation appears in multiple areas of control engineering. From predictive and optimal controllers (MPC), to robust controllers (LPV, $H_{\infty}$) to control barrier and control Lyapunov functions. Constrained convex optimisation is a useful tool to understand and to be able to use. 

## How?
I obtained the optimal solution two ways for the convex constrained problem below,

$$
\begin{aligned}
    \min_{x} \quad & x_1^2 + x_2^2\\
    \textrm{s.t.} \quad & x_1 \geq 1, \\
    & x_2 = 1.25
\end{aligned}
$$

Firstly by solving the dual problem, minimising decision variables and maximising Lagrange multipliers. The [explanation](https://github.com/keatinl1/Constrained-Convex-Optimisation/blob/main/writeup.pdf) might be helpful if you are unfamiliar. 

Secondly by solving a relaxed version of the KKT conditions using Newtons method, this is called the primal-dual interior point method, again see [explanation](https://github.com/keatinl1/Constrained-Convex-Optimisation/blob/main/writeup.pdf).

## Results
The results firstly for the solving of the dual problem are shown in figure 1. The optimiser goes to the true minima, before constraint violations are penalised by the multipliers and the optimal solution is brought back toward the feasible area. 

![alt text](https://raw.githubusercontent.com/keatinl1/Constrained-Convex-Optimisation/blob/main/solve_dual.png
<p align="center">
Figure 1
</p>

The results for the interior point method is shown in figure 2. The optimal solution is alway in the feasible area (hence the name) and it too eventually reaches the optimal solution also.

![alt text](https://raw.githubusercontent.com/keatinl1/Constrained-Convex-Optimisation/blob/main/interior_point.png
<p align="center">
Figure 2
</p>
