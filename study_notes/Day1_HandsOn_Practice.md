# Day 1 - HANDS-ON PRACTICE SESSION
*December 21, 2024*

## 🎯 Python Fundamentals for IMS135

Based on `python_help_notebook.ipynb`, here are the ESSENTIAL operations you need to master:

### 1. Essential Library Imports
```python
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import scipy.optimize
from scipy.optimize import minimize
from scipy.integrate import odeint
# import torch  # (we'll set this up later)
```

### 2. Vector Operations (CRITICAL for exam)
```python
v = np.array([1., 2., 3.])
w = np.array([3., 4., 5.])

# Four ways to compute dot product (all equivalent)
v @ v                    # Modern Python way
v.dot(v)                # Classic numpy
np.inner(v, v)          # Inner product
np.einsum('i,i', v, v)  # Einstein summation (POWERFUL!)

# Cross product
c = np.cross(v, w)      # Result: [-2.  4. -2.]
```

### 3. Matrix Operations (HIGH PRIORITY)
```python
A = np.array([[1., 2., 3.], [2., 4., 5.], [3., 5., 6.]])

# Matrix-vector multiplication
A @ v                   # Matrix times vector
v @ A                   # Vector times matrix

# Essential matrix operations
np.trace(A)             # Trace (sum of diagonal)
np.linalg.det(A)        # Determinant  
np.linalg.inv(A)        # Inverse
A.T                     # Transpose

# Eigenvalue decomposition (VERY IMPORTANT)
la, n = np.linalg.eig(A)   # eigenvalues and eigenvectors
```

### 4. Einstein Summation (EXAM SUPERPOWER)
```python
# Double contraction A:A (frequently used in exams)
np.tensordot(A, A, 2)   # Traditional way
np.einsum('ij,ij', A, A)  # Einstein way (faster)

# Outer product  
np.outer(v, v)          # Traditional
np.einsum('i,j', v, v)  # Einstein way

# Matrix multiplication
A @ A                   # Traditional
np.einsum('ij,jk', A, A)  # Einstein way
```

### 5. System Solving (CRUCIAL)
```python
# Solve Ax = v
np.linalg.inv(A) @ v    # SLOW way (avoid!)
np.linalg.solve(A, v)   # FAST way (preferred!)
```

### 6. Advanced Operations for Model Discovery
```python
# Polynomial library creation (SINDy algorithm)
from itertools import combinations_with_replacement

def polynomial_library(X, degree=3, include_bias=True):
    \"\"\"Create polynomial features for SINDy\"\"\"
    # Implementation creates [1, x, x^2, xy, x^3, ...]
    # Critical for model discovery problems
```

### 7. Sparse Regression (Model Discovery)
```python
def sparsifyDynamics(Theta, dXdt, lamb, n):
    \"\"\"Sequential least squares for sparse regression\"\"\"
    Xi = np.linalg.lstsq(Theta, dXdt, rcond=None)[0]
    
    for k in range(10):
        smallinds = np.abs(Xi) < lamb    # Threshold small coefficients
        Xi[smallinds] = 0                # Set them to zero
        # ... iterative refinement
    return Xi
```

## 🧠 KEY INSIGHTS FOR EXAM SUCCESS

### Memory Tricks:
1. **`np.einsum('ij,ij', A, A)`** = Double contraction A:A
2. **`np.linalg.solve(A, v)`** is faster than `np.linalg.inv(A) @ v`
3. **Eigenvalues** come first in `la, n = np.linalg.eig(A)`
4. **Cross product** only works in 3D: `np.cross(v, w)`

### Common Exam Operations:
- **SVD**: `U, s, Vt = np.linalg.svd(A)`
- **Matrix power**: `np.linalg.matrix_power(A, 3)`
- **Identity matrix**: `np.eye(3)`
- **Zero matrix**: `np.zeros((3,3))`

## 🎯 Day 1 PRACTICE PROBLEMS

### Problem 1: Vector Analysis
```python
v = np.array([1., 2., 3.])
w = np.array([3., 4., 5.])

# Calculate:
# a) ||v||^2 (squared magnitude)
# b) v · w (dot product)  
# c) v × w (cross product)
# d) Outer product v ⊗ w
```

### Problem 2: Matrix Operations
```python
A = np.array([[1., 2., 3.], [2., 4., 5.], [3., 5., 6.]])

# Calculate:
# a) det(A)
# b) tr(A) 
# c) eigenvalues of A
# d) A^3 (matrix power)
# e) A:A (double contraction)
```

### Problem 3: System Solving
```python
A = np.array([[2., 1.], [1., 3.]])
b = np.array([1., 2.])

# Solve Ax = b using:
# a) np.linalg.solve()
# b) Compare timing with inverse method
```

## ✅ Day 1 CHECKLIST

- [x] Set up Python environment
- [x] Master numpy vector operations  
- [x] Understand matrix decomposition basics
- [x] Practice Einstein summation notation
- [x] Learn efficient system solving
- [x] Understand sparse regression basics
- [ ] **NEXT**: Apply to SVD problems (Day 2)

## 🔮 Tomorrow's Preview (Day 2)
- **SVD fundamentals** from `lecture_SVD1_nonotes.pdf`
- **Image compression** applications
- **Hands-on with** `lecture-SVD-1.ipynb`
- **Visual linear algebra** concepts

**Time invested today: ~2 hours**  
**Confidence level: Foundation solid! 💪**