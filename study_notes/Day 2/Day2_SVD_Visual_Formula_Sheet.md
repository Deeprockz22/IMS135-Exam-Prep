# 📊 DAY 2: SVD VISUAL FORMULA CHEAT SHEET
*Mathematical Reference with Working Examples*

---

## 🎯 **CORE SVD FORMULAS**

### **🔍 The Fundamental Decomposition:**
```
A = U × Σ × V^T

Where:
• A ∈ ℝ^(m×n) - Original matrix
• U ∈ ℝ^(m×r) - Left singular vectors (orthogonal columns)
• Σ ∈ ℝ^(r×r) - Diagonal singular values matrix  
• V^T ∈ ℝ^(r×n) - Right singular vectors (orthogonal rows)
• r = min(m,n) for economy SVD
```

### **📐 Matrix Dimensions:**
```
For A ∈ ℝ^(m×n):

Full SVD (full_matrices=True):
• U: m × m
• Σ: min(m,n) diagonal values
• V^T: n × n

Economy SVD (full_matrices=False):  
• U: m × min(m,n) ← Preferred for efficiency
• Σ: min(m,n) diagonal values
• V^T: min(m,n) × n
```

---

## ⚡ **APPROXIMATION FORMULAS**

### **🎯 Rank-r Approximation:**
```
A_r = Σ(i=1 to r) σᵢ × uᵢ × vᵢ^T

Matrix form:
A_r = U[:,0:r] × diag(Σ[0:r]) × V^T[0:r,:]

Python implementation:
A_r = U[:, 0:r] @ np.diag(S[0:r]) @ VT[0:r, :]
```

### **📊 Approximation Quality:**
```
Frobenius Error: ||A - A_r||_F = √(Σ(i=r+1 to min(m,n)) σᵢ²)

Spectral Error: ||A - A_r||_2 = σ_(r+1)

Relative Error: ||A - A_r||_F / ||A||_F
```

---

## 📈 **SINGULAR VALUES ANALYSIS**

### **🔢 Ordering Property:**
```
σ₁ ≥ σ₂ ≥ ... ≥ σᵣ ≥ 0

Where:
• σ₁ = largest singular value = ||A||₂ (spectral norm)
• σᵣ = smallest singular value  
• Condition number: κ(A) = σ₁/σᵣ
```

### **⚡ Energy/Information Content:**
```
Total Energy: E_total = Σ(i=1 to r) σᵢ²

Energy in first k components: E_k = Σ(i=1 to k) σᵢ²

Cumulative Energy Ratio: E_k / E_total

For good k-rank approximation: E_k / E_total > 0.9
```

---

## 🎨 **WORKED EXAMPLE: 3×2 MATRIX**

### **📋 Given Matrix:**
```
A = [1  2]
    [3  4] 
    [5  6]
```

### **🔍 SVD Computation:**
```python
U, S, VT = np.linalg.svd(A, full_matrices=False)

Results:
U = [-0.2298  0.8835]     S = [9.5255]     VT = [-0.6196 -0.7849]
    [-0.5247  0.2408]         [0.5143]          [-0.7849  0.6196]  
    [-0.8196 -0.4019]

Verification: A = U @ diag(S) @ VT ✓
```

### **📊 Rank-1 Approximation:**
```
A₁ = σ₁ × u₁ × v₁ᵀ = 9.5255 × [-0.2298] × [-0.6196 -0.7849]
                              [-0.5247]
                              [-0.8196]

A₁ = [1.3953  1.7661]
     [3.1915  4.0396] 
     [5.0196  6.3508]

Error: ||A - A₁||_F = 0.5143
```

---

## 💾 **COMPRESSION FORMULAS**

### **📦 Storage Requirements:**

#### **Original Storage:**
```
Original: m × n = mn elements
```

#### **SVD Storage:**
```
Full SVD: m² + min(m,n) + n² elements
Economy SVD: m×r + r + r×n = r(m + n + 1) elements
Rank-r approximation: r(m + n + 1) elements
```

#### **Compression Ratio:**
```
CR = r(m + n + 1) / (mn)

Good compression when CR < 0.5
Excellent compression when CR < 0.2
```

### **🎯 Example Compression Analysis:**
```
A ∈ ℝ^(1000×500), rank-50 approximation:

Original storage: 1000 × 500 = 500,000 elements
Compressed storage: 50 × (1000 + 500 + 1) = 75,050 elements
Compression ratio: 75,050 / 500,000 = 0.15 (85% reduction!)
```

---

## 🔧 **PSEUDO-INVERSE FORMULAS**

### **💡 SVD-based Pseudo-inverse:**
```
For A = UΣV^T:
A⁺ = V × Σ⁺ × U^T

Where Σ⁺ = diag(1/σ₁, 1/σ₂, ..., 1/σᵣ, 0, ..., 0)
```

### **🧮 Properties:**
```
1. AA⁺A = A
2. A⁺AA⁺ = A⁺  
3. (AA⁺)^T = AA⁺
4. (A⁺A)^T = A⁺A

For overdetermined systems Ax = b:
x = A⁺b (least squares solution)
```

---

## 📊 **PRACTICAL PARAMETER SELECTION**

### **🎯 Rank Selection Strategies:**

#### **Fixed Compression Ratio:**
```python
desired_ratio = 0.3  # 30% of original storage
r = int(mn * desired_ratio / (m + n + 1))
```

#### **Energy Threshold:**
```python
energy = S**2
cumulative_energy = np.cumsum(energy) / np.sum(energy)
r = np.argmax(cumulative_energy > 0.95) + 1  # 95% energy
```

#### **Elbow Method:**
```python
# Plot singular values, find "elbow" (bend in curve)
ratios = S[1:] / S[:-1]  # Consecutive ratios
r = np.argmin(ratios) + 1  # Sharp drop location
```

#### **Error Tolerance:**
```python
errors = [np.linalg.norm(A - reconstruct(A, k)) for k in range(1, rank+1)]
r = np.argmax(np.array(errors) < tolerance) + 1
```

---

## 🎨 **APPLICATION-SPECIFIC FORMULAS**

### **📷 Image Compression:**
```python
def compress_image(img, quality=0.9):
    U, S, VT = np.linalg.svd(img, full_matrices=False)
    
    # Find rank for desired quality
    energy = np.cumsum(S**2) / np.sum(S**2)
    r = np.argmax(energy >= quality) + 1
    
    # Compress
    compressed = U[:, :r] @ np.diag(S[:r]) @ VT[:r, :]
    
    return compressed, r

# Quality levels:
# 0.99 → Excellent quality, minimal compression
# 0.95 → Very good quality, good compression  
# 0.90 → Good quality, strong compression
# 0.80 → Acceptable quality, high compression
```

### **🔇 Denoising:**
```python
def denoise_svd(noisy_data, noise_level=0.1):
    U, S, VT = np.linalg.svd(noisy_data, full_matrices=False)
    
    # Threshold singular values
    threshold = noise_level * S[0]
    S_clean = S.copy()
    S_clean[S < threshold] = 0
    
    # Reconstruct
    clean = U @ np.diag(S_clean) @ VT
    
    return clean
```

---

## 🔢 **NUMERICAL EXAMPLES**

### **Example 1: Compression Analysis**
```
Matrix: 200×100, Original rank: 100

Rank-10 approximation:
• Storage: 10×(200+100+1) = 3,010 elements  
• Original: 200×100 = 20,000 elements
• Compression ratio: 3,010/20,000 = 0.15 (85% compression)
• Typical error: ~5-15% depending on data structure
```

### **Example 2: Singular Value Decay**
```
Typical decay patterns:

Exponential decay: σᵢ = σ₁ × e^(-αi)
• Good for compression (few large values)
• Example: σ = [10.0, 3.7, 1.4, 0.5, 0.2, ...]

Polynomial decay: σᵢ = σ₁ × i^(-α)  
• Moderate compression potential
• Example: σ = [10.0, 5.0, 3.3, 2.5, 2.0, ...]

Uniform values: σᵢ ≈ constant
• Poor compression (all components important)
• Example: σ = [10.0, 9.8, 9.5, 9.2, 9.0, ...]
```

---

## ⚠️ **COMMON FORMULA MISTAKES**

### **❌ Wrong Reconstruction:**
```
# WRONG:
A_approx = U[0:r, :] @ np.diag(S[0:r]) @ VT[:, 0:r]
A_approx = VT[0:r, :] @ np.diag(S[0:r]) @ U[:, 0:r]
A_approx = U[:, 0:r] @ S[0:r] @ VT[0:r, :]  # Missing diag!

# CORRECT:
A_approx = U[:, 0:r] @ np.diag(S[0:r]) @ VT[0:r, :]
```

### **❌ Wrong Error Calculation:**
```
# WRONG:
error = np.sum((A - A_approx)**2)  # Sum, not norm
error = np.max(np.abs(A - A_approx))  # Max, not Frobenius  

# CORRECT:
error = np.linalg.norm(A - A_approx, 'fro')  # Frobenius norm
error = np.linalg.norm(A - A_approx, 2)     # Spectral norm
```

---

## 🧮 **QUICK REFERENCE CALCULATIONS**

### **📏 Dimension Check:**
```python
# For A with shape (m, n):
assert U.shape == (m, min(m, n))  # Economy SVD
assert S.shape == (min(m, n),)
assert VT.shape == (min(m, n), n)

# For rank-r approximation:
assert U[:, 0:r].shape == (m, r)
assert np.diag(S[0:r]).shape == (r, r)  
assert VT[0:r, :].shape == (r, n)
```

### **⚡ Performance Estimates:**
```python
# Time complexity:
# Full SVD: O(min(m²n, mn²))
# Economy SVD: O(min(m,n) × m × n)
# Rank-r approximation: O(r × m × n)

# Space complexity:
# Original: mn
# Full SVD: m² + n² + min(m,n)  
# Economy SVD: m×min(m,n) + n×min(m,n) + min(m,n)
# Rank-r: r(m + n + 1)
```

---

## 🎯 **FORMULA SUMMARY FOR EXAMS**

### **🔥 Must-Know Formulas:**
```
1. A = UΣV^T (fundamental decomposition)
2. A_r = U[:,0:r] @ diag(S[0:r]) @ VT[0:r,:] (approximation)  
3. ||A - A_r||_F = √(Σ σᵢ² for i > r) (error)
4. CR = r(m+n+1)/(mn) (compression ratio)
5. σ₁ = ||A||₂ (largest singular value = spectral norm)
```

### **⚡ Quick Mental Calculations:**
```
• Rank-r storage ≈ r × (sum of dimensions)
• Good compression when r < min(m,n)/3
• Error decreases as singular values decrease
• Economy SVD almost always preferred
• Condition number = σ₁/σᵣ (large = ill-conditioned)
```

---

## 🏆 **MASTERY VERIFICATION**

### **✅ You Know SVD Formulas When You Can:**
- [ ] Write A = UΣV^T from memory with correct dimensions
- [ ] Derive rank-r approximation formula  
- [ ] Calculate compression ratios quickly
- [ ] Choose r based on energy or error requirements
- [ ] Recognize when SVD is applicable from problem context
- [ ] Avoid indexing mistakes in reconstruction

---

**📊 These formulas are your SVD mathematical foundation - understand the concepts, use the provided code!** ✨