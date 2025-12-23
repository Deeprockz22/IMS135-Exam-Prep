# 🎴 DAY 1: QUICK REFERENCE CARDS
*Perfect for Last-Minute Review & Commute Study*

---

## 📇 **CARD 1: ESSENTIAL IMPORTS**
```python
import numpy as np                    # Your calculator
from numpy import linalg as LA        # Your ruler & compass  
import matplotlib.pyplot as plt       # Your canvas
import scipy.optimize                 # Your GPS
from scipy.integrate import odeint    # Your time machine
```
**Memory:** NumPy=Numbers, SciPy=Science, MatPlotLib=Math+Plot

---

## 📇 **CARD 2: VECTOR OPERATIONS**
```python
v = np.array([1., 2., 3.])
w = np.array([3., 4., 5.])

# DOT PRODUCT (4 ways - all identical)
v @ v                    # Modern (fastest)
v.dot(v)                # Classic
np.inner(v, v)          # Inner
np.einsum('i,i', v, v)  # Einstein (most powerful)

# OTHER OPERATIONS
np.cross(v, w)          # Cross (3D only!) → [-2, 4, -2]  
np.outer(v, w)          # Outer → 3×3 matrix
```
**Memory:** Cross=3D only, Dot=similarity, Outer=rank-1 matrix

---

## 📇 **CARD 3: MATRIX ESSENTIALS**
```python
A = np.array([[1., 2., 3.], [2., 4., 5.], [3., 5., 6.]])

# BASIC OPS
A.T                     # Transpose (flip)
np.trace(A)            # Trace = diagonal sum = 11.0
np.linalg.det(A)       # Determinant ≈ -1.0
np.linalg.matrix_rank(A) # Rank (independence check)

# MATRIX-VECTOR
A @ v                  # Matrix × vector
v @ A                  # Vector × matrix
```
**Memory:** det≠0 → invertible, trace = eigenvalue sum

---

## 📇 **CARD 4: EIGENVALUES & SOLVING**
```python
# EIGENVALUE DECOMPOSITION  
la, n = np.linalg.eig(A)    # λ first, then eigenvectors!

# SYSTEM SOLVING
np.linalg.solve(A, v)       # ✅ FAST way
np.linalg.inv(A) @ v        # ❌ SLOW way (avoid!)

# SVD PREVIEW
U, s, Vt = np.linalg.svd(A) # Coming Day 2!
```
**Memory:** "Ladies first" → λ before n, "Solve don't invert"

---

## 📇 **CARD 5: EINSTEIN SUMMATION MAGIC**
```python
# DOUBLE CONTRACTION (exam frequent!)
np.einsum('ij,ij', A, A)    # A:A → single number

# MATRIX MULTIPLICATION  
np.einsum('ij,jk', A, B)    # A×B → standard product

# TRACE
np.einsum('ii', A)          # Diagonal sum
```
**Memory:** Repeated index = sum over it, free index = keep in output

---

## 📇 **CARD 6: COMMON EXAM TRAPS**
```python
# ❌ WRONG ORDER
n, la = np.linalg.eig(A)    # NO! Eigenvectors first is wrong

# ✅ CORRECT ORDER  
la, n = np.linalg.eig(A)    # YES! Eigenvalues first

# ❌ SLOW SOLVING
x = np.linalg.inv(A) @ b    # Numerically unstable

# ✅ FAST SOLVING
x = np.linalg.solve(A, b)   # Stable and faster
```
**Memory:** Remember the traps to avoid them!

---

## 📇 **CARD 7: MODEL DISCOVERY CONCEPT**
```python
# SINDy ALGORITHM OVERVIEW
# 1. Create library: Theta = [1, x, x², xy, ...]
# 2. Solve: Theta × ξ = Ẋ  
# 3. Sparsify: Set small coefficients to zero
# 4. Repeat until converged

# SPARSIFICATION STEP
smallinds = np.abs(Xi) < threshold
Xi[smallinds] = 0    # Zero out small terms
```
**Memory:** Data → Library → Solve → Sparsify → Discover!

---

## 📇 **CARD 8: PRACTICE PROBLEM ANSWERS**
```python
v = [1, 2, 3], w = [3, 4, 5]

# ANSWERS
||v||² = 14.0           # v @ v
v·w = 26.0              # dot product  
v×w = [-2, 4, -2]       # cross product
det(A) = -1.0           # determinant
tr(A) = 11.0            # trace
eigenvalues ≈ [11.34, -0.52, 0.17]
```
**Memory:** Practice these until automatic!

---

## 📇 **CARD 9: VISUAL CONCEPTS**
```python
# SPAN CONCEPT
# 1 vector → line through origin
# 2 independent → plane  
# 3 independent → 3D space

# BASIS CHECK
rank = np.linalg.matrix_rank(V)
if rank == n_cols:
    print("Columns form a basis!")
```
**Memory:** Span=reach, Basis=minimal spanning set, Independent=can't combine

---

## 📇 **CARD 10: EXAM SUCCESS MANTRAS**
1. **"Double-dot → einsum"** → A:B = `np.einsum('ij,ij', A, B)`
2. **"Solve-don't-invert"** → `np.linalg.solve(A, b)` 
3. **"Ladies-first"** → `la, n = np.linalg.eig(A)`
4. **"Cross-3D-only"** → `np.cross()` needs 3D vectors
5. **"Speed-over-style"** → Use `@`, `einsum`, `solve`

---

## ⚡ **10-SECOND DRILL**
*Test yourself - can you answer instantly?*

1. Four ways to compute v@v? 
2. What's faster: `solve()` or `inv()@`?
3. Order of eigenvalue decomposition?
4. Einstein notation for A:A?
5. Cross product dimension requirement?

**Answers:** 1) `@`, `dot`, `inner`, `einsum` 2) `solve()` 3) λ then eigenvectors 4) `'ij,ij'` 5) 3D only

---

## 🏁 **DAY 1 COMPLETE!**

**✅ You now master:**
- Python scientific computing basics
- Vector & matrix operations  
- Einstein summation notation
- System solving techniques
- Model discovery foundations

**📈 Tomorrow:** SVD (Singular Value Decomposition) mastery

**🚀 Confidence Level:** SOLID FOUNDATION! 💪

---

*Print these cards for offline study! Perfect for subway, bus, or walking commute.*