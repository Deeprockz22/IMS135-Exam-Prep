# 🎯 DAY 1: EXAM-FOCUSED STRATEGY GUIDE
*What You Must Know vs. What's Already Provided*

---

## 🎯 **THE BIG QUESTION: MEMORIZE OR UTILIZE?**

After analyzing your `python_help_notebook.ipynb`, here's the strategic breakdown:

---

## 📋 **SECTION 1: WHAT'S ALREADY PROVIDED (DON'T MEMORIZE)**

### 🟢 **COMPLETE CODE BLOCKS AVAILABLE:**

#### **Linear Algebra Operations (Lines 56-139)**
```python
# ✅ PROVIDED - Just understand what they do
v @ v                    # Dot product
v.dot(v)                
np.inner(v, v)          
np.einsum('i,i', v, v)  

np.cross(v,w)           # Cross product
np.outer(v, v)          # Outer product
np.einsum('i,j', v, v)  

A @ v                   # Matrix-vector mult
np.trace(A)             # Trace
np.linalg.det(A)        # Determinant
la, n = np.linalg.eig(A) # Eigenvalues
np.linalg.solve(A,v)    # System solving
```

#### **SVD Operations (Lines 288-303)**
```python
# ✅ PROVIDED - Complete SVD workflow
U, S, VT = np.linalg.svd(X, full_matrices=True)
Uec, Sec, VTec = np.linalg.svd(X, full_matrices=False)
Xapprox = Uec[:,0:r] @ np.diag(Sec[0:r]) @ VTec[0:r,:]
np.linalg.norm(X,2)     # L2 norm
A_pinv = np.linalg.pinv(A) # Pseudo inverse
```

#### **PCA Workflow (Lines 329-335)**
```python
# ✅ PROVIDED - Mean centering and covariance
Xavg = np.zeros(np.size(X,1))
for i in range(nPoints):
    Xavg = Xavg + X[i,:]
Xavg = Xavg/nPoints
Xbar = np.ones(np.size(X,0)).reshape(-1,1) @ Xavg.reshape(1,-1)
```

#### **SINDy Algorithm (Lines 103-114)**
```python
# ✅ PROVIDED - Complete sparsification function
def sparsifyDynamics(Theta,dXdt,lamb,n):
    Xi = np.linalg.lstsq(Theta,dXdt,rcond=None)[0]
    for k in range(10):
        smallinds = np.abs(Xi) < lamb
        Xi[smallinds] = 0
        for ind in range(n):
            biginds = smallinds[:,ind] == 0
            Xi[biginds,ind] = np.linalg.lstsq(Theta[:,biginds],dXdt[:,ind],rcond=None)[0]
    return Xi
```

#### **Polynomial Library Creation (Lines 208-264)**
```python
# ✅ PROVIDED - Complete polynomial feature generation
def polynomial_library(X, degree=3, include_bias=True, return_names=True):
    # Full implementation provided!
```

---

## 🔴 **SECTION 2: WHAT YOU MUST KNOW BY HEART**

### **1. CONCEPTUAL UNDERSTANDING (80% of exam success)**

#### **Linear Algebra Concepts**
```
• What is rank? → Number of independent columns/rows
• What does det=0 mean? → Matrix is singular (not invertible)
• Eigenvalue meaning? → λv = Av (stretching factor)
• SVD purpose? → A = UΣVᵀ (factor into rotations & scaling)
• When to use solve() vs inv()? → Always use solve() for Ax=b
```

#### **Model Discovery Logic**
```
• SINDy workflow: Data → Library → Sparse → Discover
• Why sparsification? → Real systems have few active terms
• Threshold role? → Removes noise, keeps important terms
• Library design? → Include all physically reasonable terms
```

### **2. PROBLEM RECOGNITION (Critical!)**

#### **When you see these problem types:**
```python
# 🎯 VECTOR PROBLEM → Use provided operations
"Calculate v·w, ||v||, v×w"  
→ Use: v@w, np.linalg.norm(v), np.cross(v,w)

# 🎯 MATRIX PROBLEM → Use provided operations  
"Find eigenvalues, determinant, trace"
→ Use: np.linalg.eig(A), np.linalg.det(A), np.trace(A)

# 🎯 SVD PROBLEM → Use provided template
"Compress/approximate matrix"
→ Use: SVD code block (lines 288-303)

# 🎯 MODEL DISCOVERY → Use provided functions
"Find equation from data"  
→ Use: sparsifyDynamics + polynomial_library
```

### **3. KEY SYNTAX & PARAMETERS (Must memorize)**

#### **Function Signatures**
```python
np.linalg.svd(X, full_matrices=True/False)  # full_matrices parameter!
np.linalg.lstsq(A, b, rcond=None)          # rcond parameter!
polynomial_library(X, degree=3)           # degree parameter!
sparsifyDynamics(Theta, dXdt, lamb, n)    # lamb threshold!
```

#### **Array Indexing (Critical for exam)**
```python
Uec[:,0:r]              # First r columns
VTec[0:r,:]            # First r rows  
Xi[smallinds] = 0       # Boolean indexing
X.reshape(-1,1)         # Column vector
```

---

## ⚡ **SECTION 3: EXAM STRATEGY BASED ON PROVIDED CODE**

### **🎯 Step 1: Identify Problem Type**
```
Matrix operations? → Use numpy linalg functions
Dimensionality reduction? → Use SVD block
Data to model? → Use SINDy workflow  
Statistics? → Use PCA block
```

### **🎯 Step 2: Locate Relevant Code Block**
```
Lines 56-139:  Basic linear algebra
Lines 288-303: SVD operations
Lines 329-335: PCA setup
Lines 103-114: SINDy algorithm
Lines 208-264: Polynomial library
```

### **🎯 Step 3: Adapt Parameters**
```python
# ✅ MODIFY THESE based on problem:
degree = ?          # Polynomial degree
lamb = ?           # Sparsification threshold  
r = ?             # Approximation rank
full_matrices = ? # True for complete, False for economy
```

---

## 🧠 **SECTION 4: MENTAL MODEL FOR EXAM SUCCESS**

### **The "Toolkit Approach"**
```
🔧 BASIC TOOLS: v@w, np.trace(), np.det(), solve()
⚙️  ADVANCED TOOLS: SVD, PCA, SINDy  
🎯 PROBLEM → TOOL SELECTION → CODE ADAPTATION
```

### **Memory Palace for Code Locations**
```
🏠 "Linear Algebra House" → Lines 56-139
🏭 "SVD Factory" → Lines 288-303  
📊 "PCA Office" → Lines 329-335
🔬 "Discovery Lab" → Lines 103-114 + 208-264
```

---

## 📝 **SECTION 5: WHAT TO ACTUALLY STUDY**

### **🔴 HIGH PRIORITY (Study deeply)**
1. **Conceptual understanding** of each operation
2. **Problem recognition** patterns
3. **Parameter meanings** and typical values
4. **When to use which tool**

### **🟡 MEDIUM PRIORITY (Understand flow)**
1. **Code block structure** and logic
2. **Input/output relationships**  
3. **Common error patterns**

### **🟢 LOW PRIORITY (Don't memorize)**
1. **Exact syntax** (it's provided!)
2. **Implementation details** (black box approach)
3. **Complex indexing** (adapt from examples)

---

## 🎯 **SECTION 6: PRACTICAL EXAM WORKFLOW**

### **Before Exam:**
```
1. Print python_help_notebook.ipynb
2. Create problem-type → code-location cheat sheet
3. Practice parameter adaptation (not memorization!)
4. Understand each function's PURPOSE
```

### **During Exam:**
```
1. Read problem → Identify type  
2. Locate relevant code block
3. Adapt parameters to problem
4. Verify conceptual understanding
5. Execute and interpret results
```

---

## 📊 **SECTION 7: SAMPLE EXAM PROBLEM WALKTHROUGH**

### **Problem: "Find rank-2 approximation of matrix A using SVD"**

#### **🎯 Step 1: Recognize** 
→ SVD problem (dimensionality reduction)

#### **🎯 Step 2: Locate**
→ Lines 288-303 in python_help_notebook.ipynb

#### **🎯 Step 3: Adapt**
```python
# Given code:
U, S, VT = np.linalg.svd(X, full_matrices=True)
Uec, Sec, VTec = np.linalg.svd(X, full_matrices=False)
r = 1  # ← CHANGE THIS!
Xapprox = Uec[:,0:r] @ np.diag(Sec[0:r]) @ VTec[0:r,:]

# Your adaptation:
U, S, VT = np.linalg.svd(A, full_matrices=False)  # Use A instead of X
r = 2  # ← Problem asks for rank-2
Aapprox = U[:,0:r] @ np.diag(S[0:r]) @ VT[0:r,:]
```

#### **🎯 Step 4: Verify**
```python
# Check: Aapprox should be close to A
error = np.linalg.norm(A - Aapprox)
print(f"Approximation error: {error}")
```

---

## 🏆 **SECTION 8: SUCCESS MANTRAS**

### **The Golden Rules:**
1. **"Don't memorize code, understand purpose"**
2. **"Recognize pattern, locate block, adapt parameters"**  
3. **"Conceptual > Syntactical"**
4. **"Your brain for logic, notebook for syntax"**
5. **"Practice adaptation, not memorization"**

---

## ✅ **DAY 1 EXAM-FOCUSED CHECKLIST**

### **Understanding Check:**
- [ ] I can identify the 5 main code block types
- [ ] I know what each numpy function DOES (not exact syntax)
- [ ] I can recognize which problems need which tools
- [ ] I understand parameter roles (degree, lamb, r, etc.)
- [ ] I can adapt provided code to new problems

### **Strategy Check:**
- [ ] I have problem-type → code-location mapping
- [ ] I understand the "toolkit approach"
- [ ] I can walkthrough sample problems
- [ ] I know what NOT to memorize
- [ ] I'm confident in code adaptation

---

## 🎊 **THE BOTTOM LINE**

**❌ DON'T DO THIS:**
- Memorize every line of code
- Try to recreate functions from scratch
- Focus on syntax details

**✅ DO THIS:**  
- Understand what each tool accomplishes
- Practice recognizing problem types
- Master parameter adaptation
- Know WHERE to find what you need

**🏆 Your exam success formula:**  
**Pattern Recognition + Code Adaptation + Conceptual Understanding = Success!**

---

*You have a treasure trove of working code. Your job is to become the master navigator, not the code memorizer!*