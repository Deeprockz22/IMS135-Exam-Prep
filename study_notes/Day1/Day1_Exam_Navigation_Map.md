# 🗺️ DAY 1: EXAM PROBLEM → CODE LOCATION MAP
*Your Navigation Guide During the Exam*

---

## 📍 **QUICK REFERENCE TABLE**

| **Problem Type** | **Keywords in Problem** | **Code Location** | **Key Functions** |
|------------------|-------------------------|-------------------|-------------------|
| **Vector Ops** | "dot product", "cross product", "magnitude" | Lines 56-80 | `v@w`, `np.cross()`, `np.linalg.norm()` |
| **Matrix Basics** | "determinant", "trace", "eigenvalues" | Lines 81-139 | `np.linalg.det()`, `np.trace()`, `np.linalg.eig()` |
| **System Solving** | "solve Ax=b", "linear system" | Lines 130-139 | `np.linalg.solve()` |
| **SVD Analysis** | "singular values", "compress", "approximate" | Lines 288-303 | `np.linalg.svd()` |
| **PCA** | "principal components", "variance", "covariance" | Lines 329-355 | Mean centering + covariance |
| **Model Discovery** | "find equation", "sparse", "identify dynamics" | Lines 103-114, 208-264 | `sparsifyDynamics()`, `polynomial_library()` |
| **Data Loading** | "load csv", "load mat", "external data" | Lines 371-381 | `np.loadtxt()`, `sio.loadmat()` |

---

## 🎯 **PROBLEM RECOGNITION PATTERNS**

### **🔴 VECTOR PROBLEMS**
**Trigger words:** calculate, compute, find
**Objects:** two vectors v, w
**Tasks:** dot product, cross product, magnitude, angle
**→ Go to Lines 56-80**

### **🟠 MATRIX PROBLEMS**  
**Trigger words:** matrix, determinant, eigenvalue, trace
**Objects:** square matrix A
**Tasks:** properties, decomposition, analysis
**→ Go to Lines 81-139**

### **🟡 SVD PROBLEMS**
**Trigger words:** approximate, compress, rank, singular  
**Objects:** rectangular matrix, image data
**Tasks:** dimensionality reduction, compression
**→ Go to Lines 288-303**

### **🟢 PCA PROBLEMS**
**Trigger words:** principal, variance, components, covariance
**Objects:** data matrix with samples
**Tasks:** find main directions, reduce dimensions
**→ Go to Lines 329-355**

### **🔵 MODEL DISCOVERY PROBLEMS**
**Trigger words:** discover, equation, sparse, dynamics, SINDy
**Objects:** time series data, derivatives
**Tasks:** find governing equations
**→ Go to Lines 103-114 + 208-264**

---

## ⚡ **RAPID PROBLEM SOLVING WORKFLOW**

### **Step 1: SCAN (10 seconds)**
```
Read problem → Identify trigger words → Match to table above
```

### **Step 2: LOCATE (5 seconds)**  
```
Open notebook → Go to specified lines → Find code block
```

### **Step 3: ADAPT (2 minutes)**
```
Change variable names → Adjust parameters → Run code
```

### **Step 4: VERIFY (30 seconds)**
```
Check results make sense → Answer questions
```

---

## 🔧 **PARAMETER ADAPTATION CHEAT SHEET**

### **Common Parameters to Change:**

| **Function** | **Parameter** | **Common Values** | **What it Controls** |
|--------------|---------------|-------------------|----------------------|
| `polynomial_library()` | `degree` | 2, 3, 4 | Max polynomial degree |
| `sparsifyDynamics()` | `lamb` | 0.01, 0.1, 1.0 | Sparsification threshold |
| `svd()` | `full_matrices` | True/False | Complete vs economy SVD |
| SVD approximation | `r` | 1, 2, 5, 10 | Approximation rank |
| Data loading | `delimiter` | ',', ';', '\t' | CSV separator |

---

## 📝 **CODE ADAPTATION TEMPLATES**

### **Template 1: Vector Problem**
```python
# Replace these with your vectors
v = np.array([...])  # ← Your vector 1
w = np.array([...])  # ← Your vector 2

# Use provided operations (lines 56-80)
dot_result = v @ w
cross_result = np.cross(v, w)
magnitude = np.linalg.norm(v)
```

### **Template 2: Matrix Problem**
```python
# Replace with your matrix
A = np.array([[...], [...], [...]])  # ← Your matrix

# Use provided operations (lines 81-139)  
det_A = np.linalg.det(A)
trace_A = np.trace(A)
eigenvals, eigenvecs = np.linalg.eig(A)
```

### **Template 3: SVD Problem**
```python
# Replace X with your matrix name
X = your_matrix  # ← Your matrix

# Copy from lines 288-303, change r value
U, S, VT = np.linalg.svd(X, full_matrices=False)
r = 2  # ← Change this to desired rank
Xapprox = U[:,0:r] @ np.diag(S[0:r]) @ VT[0:r,:]
```

### **Template 4: Model Discovery Problem**  
```python
# Your data
X = your_state_data      # ← Your system states
Xdot = your_derivatives  # ← Time derivatives

# Create library (adapt degree as needed)
Theta, names = polynomial_library(X, degree=3)  # ← Change degree

# Discover model (adapt threshold)
Xi = sparsifyDynamics(Theta, Xdot, lamb=0.1, n=X.shape[1])  # ← Change lamb
```

---

## ⚠️ **COMMON EXAM MISTAKES TO AVOID**

### **❌ Don't Do:**
1. **Rewrite functions from scratch** → Use provided code!
2. **Memorize exact syntax** → Adapt from examples!
3. **Skip parameter adjustment** → Change values for your problem!
4. **Ignore variable names** → Match your data variable names!

### **✅ Do:**
1. **Identify problem type quickly** → Use trigger word matching
2. **Find relevant code block** → Use line number guide  
3. **Adapt parameters carefully** → Think about what values make sense
4. **Verify results** → Check if answers are reasonable

---

## 🏆 **EXAM DAY STRATEGY**

### **Before Exam:**
```
✅ Print this reference sheet
✅ Print python_help_notebook.ipynb  
✅ Practice problem type identification
✅ Review parameter meanings
```

### **During Exam:**
```
✅ Keep this sheet next to your computer
✅ Use table to quickly identify problem types
✅ Follow 4-step workflow for each problem
✅ Don't panic - the code is already written!
```

### **Time Management:**
```
Problem identification: 10 seconds
Code location: 5 seconds  
Parameter adaptation: 2 minutes
Result verification: 30 seconds
TOTAL per problem: ~3 minutes
```

---

## 🎯 **CONFIDENCE BOOSTERS**

### **Remember:**
- **90% of the code is already written for you**
- **Your job is navigation and adaptation, not creation**
- **Pattern recognition is more important than memorization**
- **Every problem type has a proven solution template**

### **You Are Ready When:**
- [ ] You can match any problem to the reference table in 10 seconds
- [ ] You know exactly which lines to go to for each problem type
- [ ] You can adapt parameters without fear
- [ ] You understand what each function accomplishes (not how it works)

---

## 🚀 **FINAL EXAM MANTRA**

**"I don't need to memorize code. I need to recognize patterns and navigate to solutions."**

**Your secret weapons:**
1. **Problem → Code mapping table**
2. **4-step solving workflow** 
3. **Parameter adaptation templates**
4. **Complete working code in notebook**

**You've got this! The hardest part (writing the code) is already done for you!** 💪

---

*Keep this sheet handy during your exam - it's your GPS for navigating to success!*