# 🗺️ DAY 2: SVD EXAM NAVIGATION MAP
*Your GPS for SVD Problems During Exams*

---

## 🎯 **SVD PROBLEM RECOGNITION TABLE**

| **Problem Keywords** | **Problem Type** | **Code Location** | **Key Parameters** | **Execution Time** |
|---------------------|------------------|-------------------|-------------------|-------------------|
| "approximate matrix", "compress" | Matrix Approximation | Lines 294-297 | `r` (rank), `full_matrices=False` | 2-3 min |
| "singular values", "rank" | SVD Analysis | Lines 289-291 | `full_matrices=True/False` | 1-2 min |
| "denoise", "filter noise" | Noise Reduction | Lines 294-297 + threshold | `r` (threshold), custom logic | 3-4 min |
| "image compression" | Data Compression | Lines 294-297 | `r` (quality), compression ratio | 2-3 min |
| "pseudo-inverse", "least squares" | Linear Systems | Line 303 | Matrix size check | 1-2 min |
| "low-rank", "reduce dimensions" | Dimensionality Reduction | Lines 294-297 | `r` (target dimensions) | 2-3 min |

---

## ⚡ **RAPID PROBLEM SOLVING WORKFLOW**

### **Step 1: SCAN (10 seconds)**
```
Read problem statement → Identify trigger words → Match to table above
```

### **Step 2: LOCATE (5 seconds)**
```
Open python_help_notebook.ipynb → Navigate to lines 288-303
Find the relevant code block for your problem type
```

### **Step 3: ADAPT (2 minutes)**
```
• Change matrix name (X → A, data, img, etc.)
• Set rank parameter r based on problem requirements
• Choose full_matrices=True/False appropriately
• Add any problem-specific calculations
```

### **Step 4: EXECUTE (30 seconds)**
```
Run the adapted code → Verify results make sense → Answer questions
```

**🎯 Total Time per SVD Problem: ~3 minutes**

---

## 🔍 **DETAILED PROBLEM PATTERNS**

### **🎨 Pattern 1: Matrix Approximation Problems**

#### **Trigger Words:**
- "Find rank-k approximation"
- "Approximate matrix with rank r"  
- "Compress matrix to rank..."
- "Best low-rank approximation"

#### **Solution Template:**
```python
# Step 1: Load the code from lines 294-297
U, S, VT = np.linalg.svd(A, full_matrices=False)

# Step 2: Set rank (problem will specify or you calculate)
r = 5  # ← ADAPT THIS based on problem

# Step 3: Reconstruct  
A_approx = U[:,0:r] @ np.diag(S[0:r]) @ VT[0:r,:]

# Step 4: Calculate error if requested
error = np.linalg.norm(A - A_approx)
```

#### **Parameter Adaptation Examples:**
```
"rank-3 approximation" → r = 3
"compress by 60%" → r = int(0.4 * min(A.shape))
"keep 95% energy" → r = find_energy_threshold(S, 0.95)
"storage under 1000 elements" → solve r(m+n+1) < 1000
```

---

### **📊 Pattern 2: Compression Analysis Problems**

#### **Trigger Words:**
- "Compression ratio"
- "Storage requirements"
- "Memory savings"  
- "File size reduction"

#### **Solution Template:**
```python
# Step 1: Apply SVD
U, S, VT = np.linalg.svd(A, full_matrices=False)

# Step 2: Calculate storage requirements
original_storage = A.shape[0] * A.shape[1]
compressed_storage = r * (A.shape[0] + A.shape[1] + 1)

# Step 3: Calculate compression metrics
compression_ratio = compressed_storage / original_storage
space_savings = 1 - compression_ratio
```

#### **Common Calculations:**
```python
# Compression percentage
compression_percent = (1 - compression_ratio) * 100

# Storage reduction
storage_reduction = original_storage - compressed_storage

# Efficiency (quality per storage)
efficiency = (1 - relative_error) / compression_ratio
```

---

### **🔇 Pattern 3: Denoising/Filtering Problems**

#### **Trigger Words:**
- "Remove noise"
- "Filter out noise"
- "Denoise the signal/image"
- "Clean the data"

#### **Solution Template:**
```python
# Step 1: Apply SVD  
U, S, VT = np.linalg.svd(noisy_data, full_matrices=False)

# Step 2: Threshold small singular values (noise)
threshold = 0.1 * S[0]  # ← ADAPT threshold based on problem
S_clean = S.copy()
S_clean[S < threshold] = 0

# Step 3: Reconstruct clean data
clean_data = U @ np.diag(S_clean) @ VT
```

#### **Threshold Selection Strategies:**
```
"Remove 10% noise" → threshold = 0.1 * S[0]
"Keep top k components" → S_clean = [S[0:k], zeros]  
"Energy-based" → threshold = find_noise_level(S)
```

---

### **🧮 Pattern 4: Mathematical Analysis Problems**

#### **Trigger Words:**
- "Find singular values"
- "What is the rank?"
- "Condition number"
- "Matrix properties"

#### **Solution Template:**
```python
# Step 1: Full SVD for complete analysis
U, S, VT = np.linalg.svd(A, full_matrices=True)

# Step 2: Extract properties
rank = np.sum(S > 1e-10)  # Effective rank
condition_number = S[0] / S[-1]  # Condition number  
spectral_norm = S[0]  # Largest singular value

# Step 3: Additional analysis if needed
frobenius_norm = np.linalg.norm(A, 'fro')
nuclear_norm = np.sum(S)  # Sum of singular values
```

---

### **🔧 Pattern 5: Pseudo-Inverse Problems**

#### **Trigger Words:**
- "Pseudo-inverse"
- "Solve overdetermined system"
- "Least squares solution"
- "Moore-Penrose inverse"

#### **Solution Template:**
```python
# Direct approach using line 303
A_pinv = np.linalg.pinv(A)

# For overdetermined system Ax = b:
x = A_pinv @ b  # Least squares solution

# Verify solution quality  
residual = np.linalg.norm(A @ x - b)
```

---

## 🔧 **PARAMETER ADAPTATION GUIDE**

### **🎯 The r Parameter (Most Critical)**

#### **How to Set r Based on Problem Type:**

| **Problem Statement** | **r Value** | **Code** |
|----------------------|-------------|----------|
| "rank-k approximation" | `r = k` | Direct from problem |
| "compress by X%" | `r = int((1-X/100) * min(A.shape))` | Calculate compression |
| "keep Y% energy" | `r = find_energy_rank(S, Y/100)` | Energy threshold |
| "storage limit N" | `r = solve_storage_equation(A.shape, N)` | Storage constraint |
| "error tolerance ε" | `r = find_error_rank(A, ε)` | Error constraint |

#### **Energy-Based r Selection:**
```python
def find_energy_rank(S, energy_threshold=0.95):
    energy = S**2
    cumulative_energy = np.cumsum(energy) / np.sum(energy)
    return np.argmax(cumulative_energy >= energy_threshold) + 1

# Usage: r = find_energy_rank(S, 0.90)  # 90% energy
```

### **🔧 full_matrices Parameter**

#### **When to Use Each Setting:**
```python
full_matrices=False  # ← Use 95% of the time
# Best for: approximation, compression, most practical problems

full_matrices=True   # ← Use only when specifically needed  
# Best for: theoretical analysis, when you need complete U and V
```

---

## 📊 **QUALITY VERIFICATION CHECKLIST**

### **✅ After Running SVD Code, Check:**

#### **Dimension Verification:**
```python
# Original matrix A: m×n
# Economy SVD results should have:
assert U.shape == (m, min(m,n))
assert S.shape == (min(m,n),)  
assert VT.shape == (min(m,n), n)

# Rank-r approximation should have:
assert A_approx.shape == A.shape
```

#### **Reconstruction Accuracy:**
```python
# Perfect reconstruction (r = full rank):
full_reconstruction = U @ np.diag(S) @ VT
assert np.allclose(A, full_reconstruction)

# Approximation error should be reasonable:
error = np.linalg.norm(A - A_approx)
relative_error = error / np.linalg.norm(A)
# Should be: relative_error < 0.1 for good approximation
```

#### **Compression Metrics:**
```python
# Compression ratio should make sense:
compression_ratio = r * (m + n + 1) / (m * n)
# Should be: compression_ratio < 1.0 (otherwise no compression!)
```

---

## ⚠️ **COMMON PITFALLS & QUICK FIXES**

### **❌ Mistake 1: Wrong Array Indexing**
```python
# WRONG:
A_approx = U[0:r, :] @ np.diag(S[0:r]) @ VT[:, 0:r]

# RIGHT:  
A_approx = U[:, 0:r] @ np.diag(S[0:r]) @ VT[0:r, :]
```
**🔧 Fix:** Columns for U, rows for VT

### **❌ Mistake 2: Forgetting np.diag()**
```python
# WRONG:
A_approx = U[:, 0:r] @ S[0:r] @ VT[0:r, :]

# RIGHT:
A_approx = U[:, 0:r] @ np.diag(S[0:r]) @ VT[0:r, :]
```
**🔧 Fix:** S is a vector, need diagonal matrix

### **❌ Mistake 3: Wrong Matrix Order**
```python
# WRONG:
A_approx = VT[0:r, :] @ np.diag(S[0:r]) @ U[:, 0:r]

# RIGHT:
A_approx = U[:, 0:r] @ np.diag(S[0:r]) @ VT[0:r, :]
```
**🔧 Fix:** Always U × S × VT order

### **❌ Mistake 4: Using Full SVD Unnecessarily**
```python
# WASTEFUL:
U, S, VT = np.linalg.svd(A, full_matrices=True)  # Usually overkill

# EFFICIENT:
U, S, VT = np.linalg.svd(A, full_matrices=False)  # Almost always better
```
**🔧 Fix:** Use economy SVD by default

---

## 🚀 **SPEED OPTIMIZATION TIPS**

### **⚡ Fastest Path to Solution:**

#### **For Standard Approximation Problems:**
```
1. Copy lines 294-297 directly
2. Change X → your matrix name  
3. Set r = problem requirement
4. Run → Done in 30 seconds!
```

#### **For Compression Analysis:**
```
1. Use approximation template above
2. Add storage calculation:
   compression_ratio = r * (m + n + 1) / (m * n)
3. Done in 1 minute!
```

#### **For Matrix Properties:**
```
1. Use line 291: U, S, VT = np.linalg.svd(A, full_matrices=False)
2. Extract: rank = np.sum(S > 1e-10)
3. Done in 30 seconds!
```

---

## 🎯 **EXAM TIME MANAGEMENT**

### **📊 Time Budget per Problem Type:**

| **Problem Type** | **Recognition** | **Code Setup** | **Execution** | **Total** |
|-----------------|----------------|----------------|---------------|-----------|
| Basic Approximation | 10s | 30s | 30s | **70s** |
| Compression Analysis | 10s | 60s | 30s | **100s** |
| Denoising | 15s | 90s | 30s | **135s** |
| Matrix Properties | 10s | 30s | 15s | **55s** |
| Pseudo-inverse | 5s | 15s | 15s | **35s** |

### **🔥 If Running Short on Time:**
1. **Focus on recognition** - 50% of points come from using the right approach
2. **Copy code directly** - don't try to write from scratch
3. **Set r reasonably** - even wrong r gets partial credit if approach is right
4. **Skip error analysis** - focus on getting the approximation first

---

## 🏆 **MASTERY INDICATORS**

### **✅ You've Mastered SVD Navigation When:**
- [ ] You recognize SVD problems in 10 seconds from keywords
- [ ] You know exactly which lines (288-303) to use
- [ ] You can set the r parameter appropriately in different contexts  
- [ ] You avoid the common indexing and matrix order mistakes
- [ ] You can verify your results quickly with dimension checks
- [ ] You finish SVD problems in under 3 minutes consistently

---

## 🎊 **FINAL NAVIGATION WISDOM**

### **🧭 Your SVD GPS Mantra:**
*"Keywords → Lines 288-303 → Set r → U[:,0:r] @ diag(S[0:r]) @ VT[0:r,:] → Verify"*

### **🚀 The SVD Success Formula:**
**Pattern Recognition (10s) + Code Location (5s) + Parameter Adaptation (2min) + Execution (30s) = SVD Mastery**

---

**🗺️ Your SVD navigation is now complete! You can find any SVD solution in under 3 minutes!** 🎯✨