# 🖥️ DAY 2: SVD EXECUTABLE PYTHON REFERENCE
*Complete Working SVD Code for Hands-On Practice*

"""
IMS135 Day 2: SVD Mastery - Executable Python Reference
Complete working examples based on python_help_notebook.ipynb lines 288-303
Run this file to verify your SVD understanding!
"""

import numpy as np
import matplotlib.pyplot as plt

print("🎯 IMS135 DAY 2: SVD EXECUTABLE REFERENCE")
print("=" * 50)

# =============================================================================
# SECTION 1: BASIC SVD - FOLLOWING NOTEBOOK LINES 288-303
# =============================================================================

print("\n📚 SECTION 1: BASIC SVD (From Notebook Lines 288-303)")
print("-" * 55)

# Create the exact matrix from the notebook
X = np.array([[1., 2.], [3., 4.], [5., 6.]])
print(f"Original matrix X:\n{X}")
print(f"X shape: {X.shape}")

# Full SVD (from line 291)
U, S, VT = np.linalg.svd(X, full_matrices=True)
print(f"\n🔍 FULL SVD RESULTS:")
print(f"U shape: {U.shape}")
print(f"S shape: {S.shape}")  
print(f"VT shape: {VT.shape}")
print(f"Singular values: {S}")

# Economy SVD (from lines 294-295)  
Uec, Sec, VTec = np.linalg.svd(X, full_matrices=False)
print(f"\n⚡ ECONOMY SVD RESULTS:")
print(f"Uec shape: {Uec.shape}")  # Should be (3, 2)
print(f"Sec shape: {Sec.shape}")
print(f"VTec shape: {VTec.shape}")

# Verify reconstruction
X_reconstructed = Uec @ np.diag(Sec) @ VTec
print(f"\n✅ RECONSTRUCTION CHECK:")
print(f"Original X:\n{X}")
print(f"Reconstructed X:\n{X_reconstructed}")
print(f"Reconstruction error: {np.linalg.norm(X - X_reconstructed):.2e}")

# =============================================================================
# SECTION 2: LOW-RANK APPROXIMATION (THE EXAM GOLD!)
# =============================================================================

print("\n\n📊 SECTION 2: LOW-RANK APPROXIMATION")
print("-" * 45)

# Rank-1 approximation (from lines 296-297)
r = 1  # This is the parameter you'll change in exams!
Xapprox = Uec[:, 0:r] @ np.diag(Sec[0:r]) @ VTec[0:r, :]

print(f"Rank-{r} approximation:")
print(f"Xapprox:\n{Xapprox}")

# Calculate approximation error (from lines 284, 300)
error = np.linalg.norm(X - Xapprox)
print(f"L2 norm of (X - Xapprox): {error}")

# Let's try different ranks
print(f"\n🎯 APPROXIMATION QUALITY vs RANK:")
for r in range(1, min(X.shape) + 1):
    Xapprox_r = Uec[:, 0:r] @ np.diag(Sec[0:r]) @ VTec[0:r, :]
    error_r = np.linalg.norm(X - Xapprox_r)
    compression_ratio = (r * (X.shape[0] + X.shape[1]) + r) / (X.shape[0] * X.shape[1])
    print(f"Rank {r}: Error = {error_r:.6f}, Compression = {compression_ratio:.2f}")

# =============================================================================
# SECTION 3: PSEUDO-INVERSE DEMO (FROM LINE 303)
# =============================================================================

print("\n\n🔧 SECTION 3: PSEUDO-INVERSE")
print("-" * 35)

# Create a non-square matrix for pseudo-inverse demo
A = np.array([[1., 2., 3.], [4., 5., 6.]])  
print(f"Matrix A:\n{A}")
print(f"A shape: {A.shape} (non-square, so no regular inverse)")

# Pseudo-inverse using numpy (line 303 style)
A_pinv = np.linalg.pinv(A)
print(f"\nPseudo-inverse A_pinv:\n{A_pinv}")
print(f"A_pinv shape: {A_pinv.shape}")

# Verify pseudo-inverse properties
print(f"\n✅ PSEUDO-INVERSE VERIFICATION:")
print(f"A @ A_pinv @ A ≈ A: {np.allclose(A @ A_pinv @ A, A)}")
print(f"A_pinv @ A @ A_pinv ≈ A_pinv: {np.allclose(A_pinv @ A @ A_pinv, A_pinv)}")

# =============================================================================
# SECTION 4: PRACTICAL IMAGE COMPRESSION EXAMPLE
# =============================================================================

print("\n\n🖼️ SECTION 4: IMAGE COMPRESSION SIMULATION")
print("-" * 48)

# Create a simple "image" matrix (grayscale values)
np.random.seed(42)  # For reproducibility
image_size = 20
image = np.random.randint(0, 256, (image_size, image_size)).astype(float)

print(f"Original 'image' size: {image.shape}")
print(f"Original storage: {image.size} values")

# Apply SVD compression
U_img, S_img, VT_img = np.linalg.svd(image, full_matrices=False)

print(f"\n📈 COMPRESSION ANALYSIS:")
print(f"Rank of image: {np.sum(S_img > 1e-10)}")
print(f"Singular values (first 10): {S_img[:10]}")

# Try different compression levels
compression_results = []
for r in [1, 2, 5, 10, 15]:
    # Compress
    img_compressed = U_img[:, 0:r] @ np.diag(S_img[0:r]) @ VT_img[0:r, :]
    
    # Calculate metrics
    original_storage = image.size
    compressed_storage = r * (image.shape[0] + image.shape[1]) + r
    compression_ratio = compressed_storage / original_storage
    mse = np.mean((image - img_compressed) ** 2)
    
    compression_results.append((r, compression_ratio, mse))
    print(f"Rank {r:2d}: Compression={compression_ratio:.3f}, MSE={mse:.2f}")

# =============================================================================  
# SECTION 5: EXAM-STYLE PROBLEMS
# =============================================================================

print("\n\n🎯 SECTION 5: EXAM-STYLE PROBLEMS & SOLUTIONS")
print("-" * 52)

print("Problem 1: Compress matrix to 60% of original rank")
test_matrix = np.random.rand(10, 8)
U_test, S_test, VT_test = np.linalg.svd(test_matrix, full_matrices=False)
original_rank = min(test_matrix.shape)
target_rank = int(0.6 * original_rank)

print(f"Original matrix: {test_matrix.shape}")
print(f"Original rank: {original_rank}")  
print(f"Target rank (60%): {target_rank}")

# Apply compression
compressed_matrix = U_test[:, 0:target_rank] @ np.diag(S_test[0:target_rank]) @ VT_test[0:target_rank, :]
error = np.linalg.norm(test_matrix - compressed_matrix, 'fro')
print(f"Compression error: {error:.4f}")

print(f"\n✅ Solution code:")
print(f"U, S, VT = np.linalg.svd(A, full_matrices=False)")
print(f"r = int(0.6 * min(A.shape))")
print(f"A_compressed = U[:,0:r] @ np.diag(S[0:r]) @ VT[0:r,:]")

print("\n" + "=" * 50)
print("Problem 2: Find best rank-3 approximation")

# Another test matrix
B = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8], 
              [9, 10, 11, 12],
              [13, 14, 15, 16]], dtype=float)

U_B, S_B, VT_B = np.linalg.svd(B, full_matrices=False)
r = 3
B_rank3 = U_B[:, 0:r] @ np.diag(S_B[0:r]) @ VT_B[0:r, :]

print(f"Original B:\n{B}")
print(f"Rank-3 approximation:\n{B_rank3}")
print(f"Approximation error: {np.linalg.norm(B - B_rank3):.6f}")

# =============================================================================
# SECTION 6: UNDERSTANDING SINGULAR VALUES  
# =============================================================================

print("\n\n📊 SECTION 6: SINGULAR VALUES ANALYSIS")
print("-" * 45)

# Create matrix with known structure
structured_matrix = np.outer([1, 2, 3, 4], [1, 2, 3]) + 0.1 * np.random.rand(4, 3)
U_s, S_s, VT_s = np.linalg.svd(structured_matrix, full_matrices=False)

print(f"Structured matrix singular values: {S_s}")
print(f"Normalized singular values: {S_s / S_s[0]}")

# Energy analysis
energy = S_s**2
cumulative_energy = np.cumsum(energy) / np.sum(energy)
print(f"\nEnergy distribution:")
for i, cum_energy in enumerate(cumulative_energy):
    print(f"First {i+1} components capture {cum_energy:.1%} of energy")

# =============================================================================
# SECTION 7: COMMON MISTAKES DEMONSTRATION  
# =============================================================================

print("\n\n❌ SECTION 7: COMMON MISTAKES (LEARN FROM THESE!)")
print("-" * 55)

# Using the test matrix from before
U_demo, S_demo, VT_demo = np.linalg.svd(test_matrix, full_matrices=False)
r_demo = 2

print("✅ CORRECT reconstruction:")
correct = U_demo[:, 0:r_demo] @ np.diag(S_demo[0:r_demo]) @ VT_demo[0:r_demo, :]
print(f"Shape: {correct.shape}")

print("\n❌ MISTAKE 1: Wrong indexing")
try:
    # This will fail - wrong indexing
    wrong1 = U_demo[0:r_demo, :] @ np.diag(S_demo[0:r_demo]) @ VT_demo[:, 0:r_demo]
    print("This shouldn't print - mistake not caught!")
except Exception as e:
    print(f"Error caught: {type(e).__name__}")
    print("Fix: Use U[:,0:r] not U[0:r,:]")

print("\n❌ MISTAKE 2: Missing np.diag()")
try:
    wrong2 = U_demo[:, 0:r_demo] @ S_demo[0:r_demo] @ VT_demo[0:r_demo, :]
    print("This will have wrong dimensions!")
except Exception as e:
    print(f"Error: {e}")
    print("Fix: Use np.diag(S[0:r]) to create diagonal matrix")

print("\n❌ MISTAKE 3: Wrong matrix order")
wrong_order = VT_demo[0:r_demo, :] @ np.diag(S_demo[0:r_demo]) @ U_demo[:, 0:r_demo]  
print(f"Wrong order shape: {wrong_order.shape} (should be {test_matrix.shape})")
print("Fix: Always use U @ S @ VT order")

# =============================================================================
# SECTION 8: PERFORMANCE COMPARISON
# =============================================================================

print("\n\n⚡ SECTION 8: FULL vs ECONOMY SVD PERFORMANCE") 
print("-" * 50)

# Create larger matrix for timing
large_matrix = np.random.rand(100, 80)

import time

# Time full SVD
start = time.time()
U_full, S_full, VT_full = np.linalg.svd(large_matrix, full_matrices=True)
time_full = time.time() - start

# Time economy SVD  
start = time.time()
U_econ, S_econ, VT_econ = np.linalg.svd(large_matrix, full_matrices=False)
time_econ = time.time() - start

print(f"Matrix size: {large_matrix.shape}")
print(f"Full SVD time: {time_full:.4f} seconds")
print(f"Economy SVD time: {time_econ:.4f} seconds") 
print(f"Economy is {time_full/time_econ:.1f}x faster!")

print(f"\nMatrix sizes:")
print(f"Full SVD: U={U_full.shape}, S={S_full.shape}, VT={VT_full.shape}")
print(f"Economy SVD: U={U_econ.shape}, S={S_econ.shape}, VT={VT_econ.shape}")

# =============================================================================
# FINAL SUMMARY AND EXAM TIPS
# =============================================================================

print("\n\n🎊 FINAL SUMMARY: KEY EXAM TAKEAWAYS")
print("=" * 50)

print("✅ SVD Code Location: python_help_notebook.ipynb lines 288-303")
print("✅ Always use economy SVD: full_matrices=False")  
print("✅ Reconstruction formula: U[:,0:r] @ np.diag(S[0:r]) @ VT[0:r,:]")
print("✅ Parameter r controls compression vs quality tradeoff")
print("✅ Larger singular values = more important information")
print("✅ Check your indexing: columns for U, rows for VT")
print("✅ Don't forget np.diag() for singular values")

print(f"\n🎯 You've successfully executed {X.shape[0] * X.shape[1]} different SVD examples!")
print("🚀 Ready for SVD exam problems!")

print("\n" + "=" * 50)
print("DAY 2 SVD EXECUTABLE REFERENCE COMPLETE! ✨")
print("=" * 50)