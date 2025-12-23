# 🎴 DAY 2: SVD QUICK REFERENCE CARDS
*Flash Cards for Rapid SVD Mastery*

---

## 📱 **CARD 1: SVD DEFINITION**

### **Front:**
**What does SVD stand for and what does it do?**

### **Back:**
```
SVD = Singular Value Decomposition
Decomposes ANY matrix A into: A = U × Σ × V^T
• U = Input space directions  
• Σ = Importance rankings (diagonal)
• V^T = Output space patterns
Purpose: Find best low-rank approximations
```

---

## 📱 **CARD 2: SVD CODE LOCATION**

### **Front:**  
**Where is the SVD code in python_help_notebook.ipynb?**

### **Back:**
```
Lines 288-303: Complete SVD workflow
Key code:
• Full: U, S, VT = np.linalg.svd(X, full_matrices=True)
• Economy: U, S, VT = np.linalg.svd(X, full_matrices=False)  
• Approximation: Xapprox = U[:,0:r] @ np.diag(S[0:r]) @ VT[0:r,:]
```

---

## 📱 **CARD 3: PROBLEM RECOGNITION**

### **Front:**
**What keywords trigger SVD solutions?**

### **Back:**
```
Trigger Words:
• "approximate matrix"     • "compress data"
• "reduce rank"           • "denoise"  
• "singular values"       • "low-rank"
• "dimensionality reduce" • "image compression"
→ ALL lead to SVD solution (Lines 288-303)
```

---

## 📱 **CARD 4: THE r PARAMETER**

### **Front:**
**What is r in SVD and how do you choose it?**

### **Back:**
```
r = Approximation rank (most important parameter!)

Choose r based on:
• Problem requirement: "rank-5 approximation" → r=5
• Compression ratio: "compress by 50%" → r = original_rank/2  
• Quality vs size: Smaller r = more compression, less accuracy
• Elbow method: Plot singular values, find bend
```

---

## 📱 **CARD 5: MATRIX DIMENSIONS**

### **Front:**
**If A is m×n, what are the dimensions of U, Σ, V^T?**

### **Back:**
```
Full SVD (full_matrices=True):
• U: m × m
• Σ: min(m,n) diagonal values  
• V^T: n × n

Economy SVD (full_matrices=False):
• U: m × min(m,n) ← Usually want this!
• Σ: min(m,n) diagonal values
• V^T: min(m,n) × n
```

---

## 📱 **CARD 6: SVD RECONSTRUCTION**

### **Front:**
**How do you reconstruct a rank-r approximation?**

### **Back:**
```python
# Step 1: SVD  
U, S, VT = np.linalg.svd(A, full_matrices=False)

# Step 2: Choose rank
r = 5  # Example

# Step 3: Reconstruct
A_approx = U[:,0:r] @ np.diag(S[0:r]) @ VT[0:r,:]

# Key: U columns, S diagonal, VT rows!
```

---

## 📱 **CARD 7: SINGULAR VALUES MEANING**

### **Front:**
**What do singular values tell you?**

### **Back:**
```
Singular Values (S array):
• Ordered: σ₁ ≥ σ₂ ≥ ... ≥ σᵣ ≥ 0
• Meaning: Importance/energy of each component
• Large σᵢ → Important information
• Small σᵢ → Noise or unimportant  
• Rapid decrease → Good compression possible
• Matrix rank = number of non-zero σᵢ
```

---

## 📱 **CARD 8: COMMON MISTAKES**

### **Front:**
**What are the most common SVD exam mistakes?**

### **Back:**
```
❌ Wrong indexing: U[0:r,:] instead of U[:,0:r]
❌ Wrong order: VT @ S @ U instead of U @ S @ VT  
❌ Missing np.diag(): Using S[0:r] instead of np.diag(S[0:r])
❌ Full when economy better: full_matrices=True wasteful
✅ Correct: U[:,0:r] @ np.diag(S[0:r]) @ VT[0:r,:]
```

---

## 📱 **CARD 9: SVD APPLICATIONS**

### **Front:**
**Name 5 applications of SVD in exams:**

### **Back:**
```
1. Image Compression: Reduce file size, keep quality
2. Data Denoising: Remove noise, keep signal  
3. Dimensionality Reduction: Simplify high-D data
4. Matrix Approximation: Find best low-rank version
5. Recommendation Systems: Find user-item patterns
6. Principal Component Analysis: Statistical analysis
```

---

## 📱 **CARD 10: EXAM STRATEGY**

### **Front:**
**What's the 4-step SVD exam approach?**

### **Back:**
```
Step 1: RECOGNIZE (10s) - Keywords → SVD
Step 2: LOCATE (5s) - Lines 288-303  
Step 3: ADAPT (2min) - Change A, set r, choose economy
Step 4: EXECUTE (1min) - Run code, interpret results

Total: ~3 minutes per SVD problem
Key: Pattern recognition + parameter adaptation
```

---

## 📱 **CARD 11: COMPRESSION RATIO**

### **Front:**
**How do you calculate SVD compression ratio?**

### **Back:**
```python
# Original storage: m × n elements
original_size = m * n

# Compressed storage: U[:,0:r] + S[0:r] + VT[0:r,:]  
compressed_size = m*r + r + r*n

# Compression ratio
ratio = compressed_size / original_size

# For good compression: ratio should be < 0.5
```

---

## 📱 **CARD 12: QUALITY MEASUREMENT**

### **Front:**
**How do you measure SVD approximation quality?**

### **Back:**
```python
# Frobenius norm (most common)
error = np.linalg.norm(A - A_approx, 'fro')

# Relative error  
relative_error = error / np.linalg.norm(A, 'fro')

# L2 norm (spectral norm)
spectral_error = np.linalg.norm(A - A_approx, 2)

# Good approximation: relative_error < 0.1
```

---

## 🎯 **QUICK SELF-TEST**

### **Test 1: Pattern Recognition (30 seconds)**
*"Compress this 1000×500 image matrix to 50% original size"*
**Answer:** SVD problem, r ≈ 250, use economy SVD

### **Test 2: Parameter Setting (30 seconds)**  
*"Find rank-10 approximation of matrix A"*
**Answer:** r=10, lines 294-297, U[:,0:10] @ np.diag(S[0:10]) @ VT[0:10,:]

### **Test 3: Dimension Check (30 seconds)**
*"If A is 100×30, what size is U in economy SVD?"*  
**Answer:** U is 100×30 (m × min(m,n))

---

## 📱 **MEMORY TRICKS**

### **🎭 SVD Story:**
*"**U**nderstand **S**ignificant **V**ariations **T**horoughly"*

### **🔄 Matrix Order:**
*"**U**sually **S**tart **V**ery **T**houghtfully"* → U @ S @ VT

### **📏 Dimension Memory:**
*"**U** goes with **m**, **V** goes with **n**, **S** is always diagonal"*

### **🎯 Parameter Memory:**
*"**r** = **r**ank = **r**educed = **r**econstruction quality"*

---

## 🚀 **FLASH CARD STUDY TIPS**

### **📱 Mobile Study (Commute):**
- Review 2-3 cards per commute  
- Focus on problem recognition first
- Practice parameter adaptation second

### **⚡ Quick Review (5 minutes):**
- Cards 1, 2, 3, 6 (essentials)
- Test yourself on code location and recognition

### **🧠 Deep Review (15 minutes):**
- All 12 cards + self-tests
- Focus on mistakes and dimensions  
- Practice mental parameter setting

### **🎯 Pre-Exam (2 minutes):**
- Cards 3, 4, 6, 8 (recognition + avoid mistakes)
- Quick mantra: "Keywords → Lines 288-303 → Set r → Execute"

---

## 🏆 **MASTERY INDICATORS**

### **✅ You've Mastered SVD Flash Cards When:**
- [ ] Can define SVD in 10 seconds (Card 1)
- [ ] Instantly know code location (Card 2)  
- [ ] Recognize problems from keywords (Card 3)
- [ ] Set r parameter confidently (Card 4)
- [ ] Avoid common mistakes (Card 8)
- [ ] Execute 4-step strategy smoothly (Card 10)

---

## 🎊 **CARD DECK COMPLETE!**

**These 12 cards contain 80% of what you need for SVD exam success!**

**Carry them mentally into your exam for instant SVD mastery!**

---

*Quick cards, quick wins, quick SVD success!* ⚡✨