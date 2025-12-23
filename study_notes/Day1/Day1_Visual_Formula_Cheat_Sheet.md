# 📊 DAY 1: VISUAL FORMULA CHEAT SHEET
*Mathematical Reference for Quick Lookup*

---

## 🔢 **CORE VECTOR FORMULAS**

### **Dot Product (Scalar Result)**
```
v · w = v₁w₁ + v₂w₂ + v₃w₃

Example: [1,2,3] · [3,4,5] = 1×3 + 2×4 + 3×5 = 3 + 8 + 15 = 26
```
**Code:** `np.dot(v, w)` or `v @ w`

### **Cross Product (Vector Result, 3D Only)**  
```
v × w = [v₂w₃ - v₃w₂, v₃w₁ - v₁w₃, v₁w₂ - v₂w₁]

Example: [1,2,3] × [3,4,5] = [2×5-3×4, 3×3-1×5, 1×4-2×3] = [-2,4,-2]
```
**Code:** `np.cross(v, w)`

### **Vector Magnitude**
```
||v|| = √(v₁² + v₂² + v₃²)

Example: ||[1,2,3]|| = √(1² + 2² + 3²) = √14 ≈ 3.74
```
**Code:** `np.linalg.norm(v)` or `np.sqrt(v @ v)`

---

## 🔢 **CORE MATRIX FORMULAS**

### **Matrix-Vector Multiplication**
```
     [a b c]   [x]   [ax + by + cz]
A×v = [d e f] × [y] = [dx + ey + fz]
     [g h i]   [z]   [gx + hy + iz]
```
**Code:** `A @ v`

### **Trace (Sum of Diagonal)**
```
tr(A) = a₁₁ + a₂₂ + a₃₃ + ...

Example: tr([[1,2,3],[2,4,5],[3,5,6]]) = 1 + 4 + 6 = 11
```
**Code:** `np.trace(A)`

### **Determinant (2×2 and 3×3)**
```
2×2: det([a b]) = ad - bc
         [c d]

3×3: det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
```
**Code:** `np.linalg.det(A)`

---

## 🔢 **EIGENVALUE CONCEPTS**

### **Characteristic Equation**
```
det(A - λI) = 0

For 2×2: det([a-λ  b  ]) = (a-λ)(d-λ) - bc = 0
            [c   d-λ]
```

### **Eigenvalue Properties**
```
• Sum of eigenvalues = trace(A)
• Product of eigenvalues = det(A)  
• If λ is eigenvalue, then Av = λv for some vector v
```
**Code:** `la, v = np.linalg.eig(A)`

---

## 🔢 **EINSTEIN SUMMATION PATTERNS**

### **Common Einstein Notation**
```
Matrix multiplication: C_ik = A_ij B_jk  →  'ij,jk->ik'
Double contraction:    s = A_ij B_ij      →  'ij,ij->'  
Trace:                tr(A) = A_ii        →  'ii->'
Outer product:         C_ij = u_i v_j     →  'i,j->ij'
```

### **Einstein Rules**
```
• Repeated index = sum over it
• Free index = appears in output  
• Each index appears exactly twice or is free
```

---

## 🔢 **NUMERICAL EXAMPLES FOR MEMORIZATION**

### **Standard Test Vectors**
```python
v = [1, 2, 3]     # Easy mental math
w = [3, 4, 5]     # Consecutive numbers

Results to memorize:
v @ v = 14        # 1² + 2² + 3² = 1 + 4 + 9 = 14
v @ w = 26        # 1×3 + 2×4 + 3×5 = 3 + 8 + 15 = 26  
v × w = [-2,4,-2] # Cross product result
```

### **Standard Test Matrix**
```python
A = [[1, 2, 3],
     [2, 4, 5], 
     [3, 5, 6]]

Key results to memorize:
det(A) = -1       # Determinant
tr(A) = 11        # Trace (1 + 4 + 6)
rank(A) = 3       # Full rank
```

---

## 🔢 **SYSTEM SOLVING COMPARISON**

### **Method Speed Ranking (Fastest → Slowest)**
```
1. np.linalg.solve(A, b)     ⚡ FASTEST - Direct solving
2. Specialized solvers        🚀 Context dependent  
3. np.linalg.inv(A) @ b      🐌 SLOWEST - Avoid in exams!
```

### **When Each Method Fails**
```
solve(A, b):  Fails when A is singular (det(A) = 0)
inv(A):       Fails when A is singular 
pinv(A):      Always works (pseudoinverse)
```

---

## 🔢 **VISUAL GEOMETRY REMINDERS**

### **Dot Product Geometric Meaning**
```
v · w = ||v|| ||w|| cos(θ)

θ = 0°   → cos(θ) = 1  → parallel vectors
θ = 90°  → cos(θ) = 0  → perpendicular vectors  
θ = 180° → cos(θ) = -1 → antiparallel vectors
```

### **Cross Product Geometric Meaning**
```
||v × w|| = ||v|| ||w|| sin(θ)  (magnitude)
Direction: Right-hand rule (thumb = v, fingers = w, palm = v×w)

Applications:
• Area of parallelogram = ||v × w||
• Normal to plane containing v and w
```

---

## 🔢 **COMMON CALCULATION SHORTCUTS**

### **Powers of Small Integers**
```
1² = 1    2² = 4     3² = 9     4² = 16    5² = 25
1³ = 1    2³ = 8     3³ = 27    4³ = 64    5³ = 125
```

### **Square Roots to Remember**
```
√1 = 1    √4 = 2     √9 = 3     √16 = 4    √25 = 5
√14 ≈ 3.74    √26 ≈ 5.10    √50 ≈ 7.07
```

### **Mental Math for Dot Products**
```
[a,b] · [c,d] = ac + bd

Quick examples:
[1,2] · [3,4] = 1×3 + 2×4 = 3 + 8 = 11
[2,3] · [1,4] = 2×1 + 3×4 = 2 + 12 = 14
```

---

## 🔢 **ERROR CHECKING FORMULAS**

### **Verification Techniques**
```
Matrix multiplication check:
(AB)_ij should equal Σₖ A_ik B_kj

Eigenvalue check:  
If Av = λv, then ||Av - λv|| should be ≈ 0

Orthogonality check:
If v ⟂ w, then v · w = 0
```

### **Numerical Stability Checks**
```
Condition number: cond(A) = σ_max / σ_min
• cond(A) < 100     → Well conditioned
• cond(A) > 10⁶     → Poorly conditioned
• cond(A) = ∞       → Singular matrix
```

---

## 🎯 **EXAM-SPECIFIC FORMULAS**

### **Most Likely Exam Calculations**
```python
# These appear in 90% of exams:
1. v @ v (vector magnitude squared)
2. A @ v (matrix-vector product) 
3. np.trace(A) (trace calculation)
4. np.linalg.det(A) (determinant)
5. la, n = np.linalg.eig(A) (eigenvalues)
6. np.einsum('ij,ij', A, B) (double contraction)
```

### **Problem Types to Expect**
```
Type 1: Given vectors, compute dot/cross products
Type 2: Given matrix, find eigenvalues/trace/determinant
Type 3: Solve linear system Ax = b
Type 4: Use Einstein notation for tensor operations
Type 5: Analyze linear independence of vectors
```

---

## 📱 **MOBILE-FRIENDLY SUMMARY**

**Essential Memory List:**
```
• Four dot products: @, dot, inner, einsum
• Matrix ops: .T, trace, det, rank
• Eigenvalues FIRST: la, n = eig(A)  
• Solve don't invert: solve(A,b) not inv(A)@b
• Cross 3D only: np.cross needs 3D vectors
• Einstein: repeat=sum, free=output
```

**Speed Calculations:**
```
[1,2,3] @ [1,2,3] = 14
[1,2,3] @ [3,4,5] = 26  
[[1,2,3],[2,4,5],[3,5,6]] → det=-1, tr=11
```

---

*Perfect for phone screenshots! Keep this handy during commute study.*