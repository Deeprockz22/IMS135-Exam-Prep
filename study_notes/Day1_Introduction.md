# Day 1: Course Introduction & Python Fundamentals
*Date: December 21, 2024*

## 📚 Materials Covered
- `lecture_intro.pdf` - Course overview
- `python_help_notebook.ipynb` - Essential Python libraries

## 🎯 Key Learning Objectives
1. **Master Essential Python Libraries**
   - NumPy for linear algebra operations
   - Matplotlib for visualization 
   - SciPy for scientific computing
   - PyTorch for neural networks

2. **Understand Course Structure**
   - 17 days until exam (Jan 7, 2025)
   - 30 points total (80-100%: Grade 5, 60-80%: Grade 4, 40-60%: Grade 3)
   - 4-hour exam duration

## 🔧 Python Essentials Review

### NumPy Linear Algebra Operations
```python
import numpy as np

# Vector operations
v = np.array([1., 2., 3.])
A = np.array([[1., 2., 3.], [2., 4., 5.], [3., 5., 6.]])

# Dot product (multiple ways)
v @ v
v.dot(v) 
np.inner(v, v)
np.einsum('i,i', v, v)

# Cross product
w = np.array([3.,4.,5.])
c = np.cross(v,w)

# Matrix operations
A @ v                    # Matrix-vector multiplication
np.trace(A)              # Trace
np.linalg.det(A)         # Determinant
np.linalg.inv(A)         # Inverse
np.linalg.solve(A,v)     # Solve Ax=v (preferred over inv(A)@v)

# Eigenvalues/eigenvectors
la, n = np.linalg.eig(A)
```

### Key Tensor Operations with Einstein Notation
```python
# Double contraction A:A
np.tensordot(A, A, 2)
np.einsum('ij,ij', A, A)

# Outer product
np.outer(v, v)
np.einsum('i,j', v, v)

# Matrix power
np.linalg.matrix_power(A, 3)
```

### Matplotlib Basics
```python
import matplotlib.pyplot as plt

# Basic plotting
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Function')
plt.show()
```

### SciPy Integration
```python
import scipy.optimize
from scipy.optimize import minimize
from scipy.integrate import odeint
```

### PyTorch Setup
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import grad
```

## ✅ Today's Achievements
- [x] Reviewed essential Python libraries
- [x] Set up development environment
- [x] Created Git repository for tracking progress
- [x] Understood numpy linear algebra operations
- [x] Familiar with matplotlib plotting basics

## 🎯 Tomorrow's Focus (Day 2)
- Linear Algebra & SVD fundamentals
- Work through `lecture_SVD1_nonotes.pdf`
- Practice with `lecture-SVD-1.ipynb`
- Visual linear algebra concepts

## 📝 Notes & Questions
- Focus on einsum notation - very useful for tensor operations
- Remember: `np.linalg.solve(A,v)` is faster than `np.linalg.inv(A)@v`
- PyTorch will be crucial for neural networks (Days 5-6)

## 🏆 Progress Tracker
- Day 1: ✅ COMPLETE
- Day 2: 📅 Scheduled
- Days remaining: 16