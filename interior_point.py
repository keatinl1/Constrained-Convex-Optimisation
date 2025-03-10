import matplotlib.pyplot as plt
import numpy as np

# Parameters
x1 = 2.5
x2 = 1.5
nu_mult = 0.1
lambda_mult = 0.1
s = 0.1

alpha = 0.1

# Lists to store iteration values
x1_list = [x1]
x2_list = [x2]
nu_list = [nu_mult]
lambda_list = [lambda_mult]
s_list = [s]

for k in range(250):

    J = np.matrix([[2, 0, 0, -1, 0], 
                   [0, 2, 1,  0, 0], 
                   [0, 1, 0, 0, 0], 
                   [-1, 0, 0, 0, 1], 
                   [0, 0, 0, s, lambda_mult]])

    f = np.matrix([[2*x1-lambda_mult], 
                   [2*x2+nu_mult], 
                   [x2-1.25], 
                   [1-x1+s], 
                   [s*lambda_mult]])
    
    delta_x = (np.linalg.inv(J)@f)

    # Update the optimization variables using a step size alpha
    x1 = x1 - alpha * delta_x[0, 0]
    x2 = x2 - alpha * delta_x[1, 0]
    nu_mult = nu_mult - alpha * delta_x[2, 0]
    lambda_mult = lambda_mult - alpha * delta_x[3, 0]
    s = s - alpha * delta_x[4, 0]

    x1_list.append(x1)
    x2_list.append(x2)
    nu_list.append(nu_mult)
    lambda_list.append(lambda_mult)
    s_list.append(s)

# =============================KKT=CONDITIONS=====================================
gradient = (2 * x1 - lambda_mult) + (2 * x2 + nu_mult) + lambda_mult*(-x1) + nu_mult*(x2)
print(f"\nGradient of Lagrangian at x*: {gradient:.2f}")
print(f"Primal values: x1 = {x1:.2f}, x2 = {x2:.2f}")
print(f"Primal feasibility: g(x) = {1-x1:.2f}, h(x) = {x2-1.25:.2f}")
print(f"Dual values: lambda = {lambda_mult:.4f}, nu = {nu_mult:.4f}")
print(f"Complimentray slackness (lambda*g(x)):  = {lambda_mult*(x1 - 1):.2f}\n")

# =============================PLOTTING========================================
fig, ax = plt.subplots(figsize=(10, 8))
feature_x = np.linspace(-5.0, 3.0, 70)
feature_y = np.linspace(-5.0, 3.0, 70)

[X, Y] = np.meshgrid(feature_x, feature_y)
Z = X ** 2 + Y ** 2  # Objective function

ax.contourf(X, Y, Z, levels=50, cmap="viridis", alpha=0.6)
ax.plot(x1_list, x2_list, linestyle='--', marker='o', label="Optimization Path")

# Add arrows to show direction
for i in range(0, len(x1_list) - 1, 5):  # Add arrows every 10 steps
    ax.annotate("", xy=(x1_list[i + 1], x2_list[i + 1]), xytext=(x1_list[i], x2_list[i]),
                arrowprops=dict(arrowstyle="->", color="white", lw=2))

# Plot equality constraints (solid lines)
ax.axvline(x=1, color='firebrick', linestyle='-', linewidth=2, label="Equality Constraint x1 = 1")
ax.axhline(y=1.25, color='lime', linestyle='-', linewidth=2, label="Equality Constraint x2 = 1.25")

# Plot inequality constraints (shaded regions)
ax.fill_betweenx(np.linspace(-5, 5, 100), -2, 2, color="gray", alpha=0.2, label="Inequality x1 ∈ [-2,2]")
ax.fill_between(np.linspace(-5, 5, 100), -1, 3, color="gray", alpha=0.2, label="Inequality x2 ∈ [-1,3]")
ax.fill_betweenx(np.linspace(-5, 5, 100), -5, 1, color="firebrick", alpha=0.4, label="Infeasible Region (x1 < 1)")

# Adjust axis limits to make the plot more spread out
ax.set_xlim(min(x1_list) - 0.5, max(x1_list) + 0.5)
ax.set_ylim(min(x2_list) - 0.5, max(x2_list) + 0.5)

# Labels and title
ax.set_xlabel("x1")
ax.set_ylabel("x2")
plt.show()
# ===========================================================================


