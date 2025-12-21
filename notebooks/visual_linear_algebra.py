import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

out_dir = os.path.join(os.path.dirname(__file__), "visuals")
os.makedirs(out_dir, exist_ok=True)

def plot_vector(ax, v, color="C0", label=None):
    ax.arrow(0, 0, v[0], v[1], head_width=0.08, head_length=0.12, fc=color, ec=color, linewidth=2)
    if label:
        ax.text(v[0]*1.05, v[1]*1.05, label, fontsize=12, color=color)

# 1) Single vector and its span (a line)
def example_span():
    v = np.array([2.0, 1.0])
    t = np.linspace(-3, 3, 200)
    line = np.outer(t, v)

    fig, ax = plt.subplots(figsize=(5,5))
    ax.plot(line[:,0], line[:,1], color="C1", linestyle='--', label='span{v}')
    plot_vector(ax, v, color='C0', label='v')
    ax.set_title('Span of a single vector (a line through origin)')
    ax.set_xlim(-6,6); ax.set_ylim(-6,6); ax.set_aspect('equal')
    ax.grid(True)
    plt.legend()
    path = os.path.join(out_dir, 'span_single_vector.png')
    fig.savefig(path)
    print('Saved', path)

# 2) Two independent vectors: linear combinations fill the plane
def example_independent():
    v1 = np.array([1.0, 0.5])
    v2 = np.array([-0.6, 1.0])
    a = np.linspace(-2, 2, 9)
    b = np.linspace(-2, 2, 9)
    A, B = np.meshgrid(a, b)
    combos = A.reshape(-1,1)*v1 + B.reshape(-1,1)*v2

    fig, ax = plt.subplots(figsize=(5,5))
    ax.scatter(combos[:,0], combos[:,1], s=15, color='gray', alpha=0.7)
    plot_vector(ax, v1, color='C0', label='v1')
    plot_vector(ax, v2, color='C1', label='v2')
    ax.set_title('Linear combinations of two independent vectors (fill the plane)')
    ax.set_xlim(-4,4); ax.set_ylim(-4,4); ax.set_aspect('equal')
    ax.grid(True)
    path = os.path.join(out_dir, 'linear_combinations_independent.png')
    fig.savefig(path)
    print('Saved', path)

# 3) Two dependent vectors: combinations lie on a line
def example_dependent():
    v1 = np.array([1.0, 0.5])
    v2 = 2.0*v1  # dependent
    a = np.linspace(-2, 2, 41)
    b = np.linspace(-2, 2, 41)
    A, B = np.meshgrid(a, b)
    combos = A.reshape(-1,1)*v1 + B.reshape(-1,1)*v2

    fig, ax = plt.subplots(figsize=(5,5))
    ax.scatter(combos[:,0], combos[:,1], s=10, color='gray', alpha=0.6)
    plot_vector(ax, v1, color='C0', label='v1')
    plot_vector(ax, v2, color='C1', label='v2 (2*v1)')
    ax.set_title('Dependent vectors: combinations lie on the same line')
    ax.set_xlim(-6,6); ax.set_ylim(-6,6); ax.set_aspect('equal')
    ax.grid(True)
    path = os.path.join(out_dir, 'linear_combinations_dependent.png')
    fig.savefig(path)
    print('Saved', path)

# 4) Basis check and rank demonstration
def example_basis_check():
    V = np.array([[1.0, -0.6], [0.5, 1.0]])
    rank = np.linalg.matrix_rank(V)
    det = np.linalg.det(V)
    print('\nMatrix V columns are v1 and v2:\n', V)
    print('Rank(V) =', rank)
    print('Determinant (2x2) =', det)
    print('If rank == 2 then the two columns form a basis of R^2 (they are independent).')

    # plot the two column vectors
    v1 = V[:,0]; v2 = V[:,1]
    fig, ax = plt.subplots(figsize=(5,5))
    a = np.linspace(-2,2,13); b = np.linspace(-2,2,13)
    A, B = np.meshgrid(a,b)
    combos = A.reshape(-1,1)*v1 + B.reshape(-1,1)*v2
    ax.scatter(combos[:,0], combos[:,1], s=12, color='gray', alpha=0.6)
    plot_vector(ax, v1, color='C0', label='v1')
    plot_vector(ax, v2, color='C1', label='v2')
    ax.set_title('Basis check: if rank==2, columns span R^2')
    ax.set_xlim(-4,4); ax.set_ylim(-4,4); ax.set_aspect('equal')
    ax.grid(True)
    path = os.path.join(out_dir, 'basis_check.png')
    fig.savefig(path)
    print('Saved', path)

if __name__ == '__main__':
    print('Visual Linear Algebra examples — generated at', datetime.utcnow().isoformat() + 'Z')
    example_span()
    example_independent()
    example_dependent()
    example_basis_check()
    print('\nPlots saved to:', out_dir)
    print('Open the PNG files or run this script inside a notebook to display inline.')
