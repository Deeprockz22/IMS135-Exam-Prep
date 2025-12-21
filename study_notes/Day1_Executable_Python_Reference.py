# 🖥️ DAY 1: EXECUTABLE PYTHON REFERENCE
*Copy-paste ready code for hands-on learning*

```python
# ======================================
# DAY 1: COMPLETE PYTHON REFERENCE CODE  
# Run this code to see all concepts in action
# ======================================

import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

print("🎯 IMS135 DAY 1: PYTHON FUNDAMENTALS DEMONSTRATION")
print("=" * 60)

# ======================================
# SECTION 1: VECTOR OPERATIONS
# ======================================

print("\n📊 SECTION 1: VECTOR OPERATIONS")
print("-" * 40)

# Define test vectors
v = np.array([1., 2., 3.])
w = np.array([3., 4., 5.])

print(f"Vector v: {v}")  
print(f"Vector w: {w}")

# Four ways to compute dot product (all identical!)
print(f"\n🔴 DOT PRODUCT - Four identical ways:")
print(f"v @ v =           {v @ v}")
print(f"v.dot(v) =        {v.dot(v)}")  
print(f"np.inner(v,v) =   {np.inner(v, v)}")
print(f"np.einsum('i,i',v,v) = {np.einsum('i,i', v, v)}")

print(f"\n🔵 OTHER VECTOR OPERATIONS:")
print(f"v @ w (different vectors) = {v @ w}")
print(f"||v|| (magnitude) = {np.linalg.norm(v):.3f}")
print(f"v × w (cross product) = {np.cross(v, w)}")
print(f"v ⊗ w (outer product):")
print(np.outer(v, w))

# ======================================  
# SECTION 2: MATRIX OPERATIONS
# ======================================

print("\n📊 SECTION 2: MATRIX OPERATIONS")
print("-" * 40)

# Standard test matrix
A = np.array([[1., 2., 3.], 
              [2., 4., 5.], 
              [3., 5., 6.]])

print("Matrix A:")
print(A)

print(f"\n🔴 BASIC MATRIX OPERATIONS:")
print(f"A.T (transpose):")
print(A.T)
print(f"np.trace(A) = {np.trace(A)}")
print(f"np.linalg.det(A) = {np.linalg.det(A):.6f}")
print(f"np.linalg.matrix_rank(A) = {np.linalg.matrix_rank(A)}")

print(f"\n🔵 MATRIX-VECTOR OPERATIONS:")
print(f"A @ v = {A @ v}")
print(f"v @ A = {v @ A}")

# ======================================
# SECTION 3: EIGENVALUE DECOMPOSITION  
# ======================================

print("\n📊 SECTION 3: EIGENVALUE DECOMPOSITION")
print("-" * 40)

# Remember: eigenvalues FIRST, then eigenvectors
la, n = np.linalg.eig(A)
print(f"Eigenvalues (λ): {la}")
print(f"Eigenvectors (columns of n):")
print(n)

print(f"\n🔍 VERIFICATION:")  
print(f"Sum of eigenvalues: {np.sum(la):.6f}")
print(f"Trace of A: {np.trace(A):.6f}")
print(f"Should be equal! ✓" if abs(np.sum(la) - np.trace(A)) < 1e-10 else "❌ Error!")

# ======================================
# SECTION 4: SYSTEM SOLVING COMPARISON
# ======================================

print("\n📊 SECTION 4: SYSTEM SOLVING COMPARISON")
print("-" * 40)

# Create a simple 2x2 system for clarity
A_small = np.array([[2., 1.], 
                    [1., 3.]])
b = np.array([1., 2.])

print(f"System: A @ x = b")
print(f"A = \n{A_small}")
print(f"b = {b}")

# Method 1: Direct solving (PREFERRED)
x_solve = np.linalg.solve(A_small, b)
print(f"\n✅ FAST METHOD - np.linalg.solve:")
print(f"x = {x_solve}")
print(f"Verification: A @ x = {A_small @ x_solve}")

# Method 2: Matrix inversion (AVOID)
x_inv = np.linalg.inv(A_small) @ b  
print(f"\n❌ SLOW METHOD - matrix inversion:")
print(f"x = {x_inv}")
print(f"Same result? {np.allclose(x_solve, x_inv)}")

# ======================================
# SECTION 5: EINSTEIN SUMMATION MAGIC
# ======================================

print("\n📊 SECTION 5: EINSTEIN SUMMATION EXAMPLES")
print("-" * 40)

# Double contraction (very common in exams!)
double_contract = np.einsum('ij,ij', A, A)
print(f"A:A (double contraction) = {double_contract}")

# Compare with traditional method
traditional = np.trace(A.T @ A) 
print(f"Traditional A:A = {traditional}")
print(f"Same result? {abs(double_contract - traditional) < 1e-10}")

# Matrix multiplication using Einstein
B = np.array([[1., 0., 1.], 
              [0., 1., 0.], 
              [1., 0., 1.]])
              
AB_einstein = np.einsum('ij,jk->ik', A, B)
AB_traditional = A @ B
print(f"\nMatrix multiplication comparison:")
print(f"A @ B using Einstein notation:")
print(AB_einstein)
print(f"Same as A @ B? {np.allclose(AB_einstein, AB_traditional)}")

# ======================================
# SECTION 6: MODEL DISCOVERY PREVIEW
# ======================================

print("\n📊 SECTION 6: MODEL DISCOVERY PREVIEW")
print("-" * 40)

# Simple example: x' = 2x (exponential growth)
print("Example: Discover dynamics from data")
print("True model: x' = 2x (exponential growth)")

# Generate synthetic data
t = np.linspace(0, 1, 10)
x_true = 3 * np.exp(2 * t)  # x(t) = 3*exp(2*t)
x_dot_true = 6 * np.exp(2 * t)  # x'(t) = 6*exp(2*t) = 2*x(t)

# Create library matrix (polynomial terms)
Theta = np.column_stack([np.ones(len(t)), x_true, x_true**2])
print(f"\nLibrary matrix Theta shape: {Theta.shape}")
print("Columns: [1, x, x²]")

# Solve for coefficients  
Xi = np.linalg.lstsq(Theta, x_dot_true, rcond=None)[0]
print(f"Discovered coefficients: {Xi}")
print("Expected: [0, 2, 0] (since x' = 0*1 + 2*x + 0*x²)")
print(f"Discovery successful? {abs(Xi[1] - 2) < 0.1 and abs(Xi[0]) < 0.1 and abs(Xi[2]) < 0.1}")

# ======================================
# SECTION 7: COMMON EXAM PATTERNS
# ======================================

print("\n📊 SECTION 7: COMMON EXAM PATTERNS")
print("-" * 40)

# Pattern 1: Compute various norms and products
vectors = [[1, 0, 0], [0, 1, 0], [1, 1, 0]]
print("Orthogonality check for standard basis vectors:")
for i in range(len(vectors)):
    for j in range(i+1, len(vectors)):
        vi = np.array(vectors[i])
        vj = np.array(vectors[j])
        dot_prod = vi @ vj
        print(f"v{i+1} · v{j+1} = {dot_prod} {'(orthogonal ✓)' if abs(dot_prod) < 1e-10 else ''}")

# Pattern 2: Check linear independence
print(f"\nLinear independence check:")
V = np.array([[1, 2, 3], [0, 1, 2], [0, 0, 1]])  # Upper triangular -> independent
rank_V = np.linalg.matrix_rank(V)
print(f"Matrix V rank: {rank_V}")
print(f"Number of columns: {V.shape[1]}")
print(f"Linearly independent? {'✓' if rank_V == V.shape[1] else '❌'}")

# ======================================
# SECTION 8: PERFORMANCE COMPARISON
# ======================================

print("\n📊 SECTION 8: PERFORMANCE INSIGHTS")
print("-" * 40)

# Create larger system for timing
import time
n = 100
A_big = np.random.randn(n, n)
A_big = A_big @ A_big.T  # Make positive definite
b_big = np.random.randn(n)

# Time solve() method
start = time.time()
x_solve_big = np.linalg.solve(A_big, b_big)
time_solve = time.time() - start

# Time inversion method  
start = time.time()
x_inv_big = np.linalg.inv(A_big) @ b_big
time_inv = time.time() - start

print(f"Timing comparison (n={n}):")
print(f"solve() method: {time_solve*1000:.2f} ms")
print(f"inverse method: {time_inv*1000:.2f} ms")  
print(f"Speedup factor: {time_inv/time_solve:.1f}x faster")
print(f"Results match? {np.allclose(x_solve_big, x_inv_big)}")

# ======================================
# SECTION 9: MEMORY AIDS & FINAL SUMMARY
# ======================================

print("\n📊 SECTION 9: FINAL SUMMARY & MEMORY AIDS")
print("-" * 40)

memory_aids = [
    "1. 'Ladies first' → eigenvalues (λ) before eigenvectors (n)",
    "2. 'Solve don't invert' → use solve() not inv()@",  
    "3. 'Cross 3D only' → cross product needs 3D vectors",
    "4. 'Double-dot einsum' → A:B = einsum('ij,ij', A, B)",
    "5. 'Speed over style' → use @, einsum, solve for speed"
]

for aid in memory_aids:
    print(f"✓ {aid}")

print(f"\n🎯 QUICK NUMERICAL CHECK:")
test_results = {
    "[1,2,3] @ [1,2,3]": v @ v,
    "[1,2,3] @ [3,4,5]": v @ w, 
    "trace(test_matrix)": np.trace(A),
    "det(test_matrix)": np.linalg.det(A)
}

for desc, result in test_results.items():
    print(f"{desc:20} = {result:.6f}")

print(f"\n🏆 DAY 1 MASTERY COMPLETE!")
print("Ready for Day 2: SVD (Singular Value Decomposition)")
print("=" * 60)
```

# 🚀 **HOW TO USE THIS CODE**

## **Option 1: Copy-Paste Sections**
Copy individual sections to test specific concepts:
```python
# Just vector operations
import numpy as np
v = np.array([1., 2., 3.])
print(f"v @ v = {v @ v}")  # Should output: 14.0
```

## **Option 2: Run Complete Script** 
Save as `day1_demo.py` and run:
```bash
python day1_demo.py
```

## **Option 3: Interactive Testing**
Use in Python/Jupyter notebook for step-by-step exploration.

## 📱 **Mobile-Friendly Quick Tests**
For commute study, memorize these key results:
```python
# Essential calculations to remember:
v = [1,2,3]; v@v = 14.0
v = [1,2,3], w = [3,4,5]; v@w = 26.0  
A = [[1,2,3],[2,4,5],[3,5,6]]; trace(A) = 11.0, det(A) = -1.0
```

---

*This code demonstrates every concept from Day 1. Run it whenever you need hands-on reinforcement!*