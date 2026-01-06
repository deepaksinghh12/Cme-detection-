# Composite Index Backend Implementation - Complete Explanation

## 📍 Location: `backend/main.py` (Lines 2895-3135)

## 🎯 What is Composite Index?

**Composite Index** = Ek single number jo 4 space weather parameters (Dst, Kp, Ap, Sunspot) ko combine karke dikhata hai. Yeh **Principal Component Analysis (PCA)** use karta hai.

---

## 🔬 Step-by-Step Backend Process

### **STEP 1: Import Libraries** (Lines 2899-2900)
```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
```
**Kya ho raha hai:**
- `PCA`: Principal Component Analysis - data ko reduce karne ke liye
- `StandardScaler`: Z-score normalization - sab parameters ko same scale pe lane ke liye

**Kyun zaroori:**
- Dst: -200 to +50 nT
- Kp: 0 to 9
- Ap: 0 to 400 nT  
- Sunspot: 0 to 300
- **Problem:** Different scales = ek parameter dominate kar sakta hai
- **Solution:** Normalize karke sabko equal weight dena

---

### **STEP 2: Prepare Parameters** (Lines 2902-2913)
```python
composite_params = ['Dst_Index_nT', 'ap_index_nT', 'Sunspot_Number', 'Kp_10']
available_params = [p for p in composite_params if p in df.columns]
```
**Kya ho raha hai:**
- 4 parameters ki list banayi
- Check kiya ki yeh parameters DataFrame me available hain
- Logging: Konsi parameters mili, konsi nahi

**Example:**
- Expected: `['Dst_Index_nT', 'ap_index_nT', 'Sunspot_Number', 'Kp_10']`
- Available: `['Dst_Index_nT', 'ap_index_nT', 'Sunspot_Number', 'Kp_10']` ✅

---

### **STEP 3: Create Data Matrix** (Lines 2915-2927)
```python
if len(available_params) >= 2:  # Need at least 2 parameters
    data_matrix = df[available_params].values
    valid_mask = ~np.isnan(data_matrix).any(axis=1)
    data_matrix_clean = data_matrix[valid_mask]
```
**Kya ho raha hai:**
- **Line 2917:** DataFrame se sirf 4 parameters ka data extract kiya
  - Shape: `(168 rows, 4 columns)` - 168 hours × 4 parameters
- **Line 2923:** NaN values wale rows ko identify kiya
- **Line 2924:** Sirf valid rows (no NaN) ko rakha

**Example Data Matrix:**
```
Row 1: [Dst=-20, Ap=15, Sunspot=45, Kp=2.5]
Row 2: [Dst=-25, Ap=18, Sunspot=47, Kp=2.7]
...
Row 168: [Dst=-15, Ap=12, Sunspot=43, Kp=2.3]
```

---

### **STEP 4: Z-Score Normalization** (Lines 2930-2932)
```python
scaler = StandardScaler()
data_normalized = scaler.fit_transform(data_matrix_clean)
```
**Kya ho raha hai:**
- **StandardScaler:** Har column ko normalize karta hai
- **Formula:** `z = (x - mean) / std_dev`
- **Result:** Har column ka mean = 0, std_dev = 1

**Example Transformation:**
```
Before Normalization:
Dst: [-20, -25, -15, ...]  (mean=-20, std=5)
Kp:  [2.5, 2.7, 2.3, ...]  (mean=2.5, std=0.2)

After Normalization:
Dst: [0.0, -1.0, 1.0, ...]  (mean=0, std=1)
Kp:  [0.0, 1.0, -1.0, ...]  (mean=0, std=1)
```

**Kyun zaroori:**
- Ab sab parameters same scale pe hain
- Koi bhi parameter dominate nahi karega
- PCA properly kaam karega

---

### **STEP 5: Apply PCA** (Lines 2937-2939)
```python
pca = PCA(n_components=1)
pc1 = pca.fit_transform(data_normalized)
```
**Kya ho raha hai:**
- **PCA:** Principal Component Analysis
- **n_components=1:** Sirf first principal component (PC1) chahiye
- **fit_transform:** 
  1. Data ko analyze karta hai
  2. PC1 calculate karta hai (jo maximum variance capture karta hai)
  3. Har row ko PC1 me convert karta hai

**Mathematical Process:**
1. **Covariance Matrix:** 4×4 matrix banata hai (4 parameters ke beech correlation)
2. **Eigenvalues & Eigenvectors:** Calculate karta hai
3. **PC1:** First eigenvector (jo maximum variance explain karta hai)
4. **Transform:** Har row ko PC1 me project karta hai

**Example:**
```
Input (Normalized): 168 rows × 4 columns
↓ PCA
Output (PC1): 168 rows × 1 column
[0.5, -1.2, 2.3, -0.8, 1.5, ...]  ← Composite Index values
```

**Variance Explained:**
- PC1 typically 70-90% variance capture karta hai
- Matlab: PC1 me 4 parameters ka 70-90% information hai

---

### **STEP 6: Extract Composite Index** (Lines 2944-2948)
```python
composite_full = np.full(len(df), np.nan)
composite_full[valid_mask] = pc1.flatten()
composite_index = [float(x) if not np.isnan(x) else 0.0 for x in composite_full]
```
**Kya ho raha hai:**
- **Line 2946:** Full length ka array banaya (NaN se fill)
- **Line 2947:** Valid rows me PC1 values daale
- **Line 2948:** NaN ko 0.0 se replace kiya, baaki ko float me convert

**Result:**
- 168 values ka array
- Har value = composite index for that time point
- Range: typically -3 to +3 (normalized)

---

### **STEP 7: Calculate Statistics** (Lines 2953-2966)
```python
composite_stats = {
    'min': float(composite_array.min()),
    'max': float(composite_array.max()),
    'mean': float(composite_array.mean()),  # ≈ 0 (normalized)
    'std': float(composite_array.std()),
    'variance_explained': float(pca.explained_variance_ratio_[0]),
    'method': 'PCA (First Principal Component)',
    'normalized_params': available_params
}
```
**Kya ho raha hai:**
- Min, Max, Mean, Std calculate kiya
- **Variance Explained:** PC1 kitna % variance capture karta hai (70-90%)
- **Method:** Documentation ke liye
- **Normalized Params:** Konsi parameters use kiye

---

### **STEP 8: Add to Response** (Lines 3093-3114)
```python
if composite_index is not None and len(composite_index) > 0:
    response['composite_index'] = {
        'values': composite_index,  # 168 values
        'statistics': composite_stats,
        'label': 'Composite Space Weather Index',
        'unit': 'PC1 (Normalized)',
        'description': 'Combined waveform using PCA'
    }
    parameters['Composite_Index'] = composite_index  # Frontend ke liye
```
**Kya ho raha hai:**
- Composite index ko response me add kiya
- `parameters` dict me bhi add kiya (frontend access ke liye)
- Statistics bhi add kiye

---

## 📊 Complete Flow Diagram

```
1. Forecast Model Output
   ↓
   DataFrame with 4 columns: [Dst, Ap, Sunspot, Kp]
   Shape: (168 rows, 4 columns)

2. Extract Parameters
   ↓
   data_matrix = df[['Dst_Index_nT', 'ap_index_nT', 'Sunspot_Number', 'Kp_10']].values
   Shape: (168, 4)

3. Remove NaN
   ↓
   data_matrix_clean
   Shape: (168, 4) [assuming no NaN]

4. Normalize (Z-Score)
   ↓
   StandardScaler.fit_transform()
   Result: Mean=0, Std=1 for each column
   Shape: (168, 4)

5. Apply PCA
   ↓
   PCA(n_components=1).fit_transform()
   Result: PC1 (First Principal Component)
   Shape: (168, 1)

6. Extract Values
   ↓
   composite_index = [0.5, -1.2, 2.3, ...]
   Length: 168 values

7. Add to Response
   ↓
   JSON Response:
   {
     "parameters": {
       "Composite_Index": [0.5, -1.2, 2.3, ...]
     },
     "composite_index": {
       "values": [0.5, -1.2, 2.3, ...],
       "statistics": {...}
     }
   }
```

---

## 🔑 Key Points

1. **Why PCA?**
   - 4 parameters ko 1 me combine karta hai
   - Maximum variance capture karta hai
   - Data-driven (no arbitrary weights)

2. **Why Normalize?**
   - Different scales ko same pe lane ke liye
   - Equal contribution ensure karne ke liye

3. **Why PC1?**
   - First principal component = maximum variance
   - Best single summary of all 4 parameters

4. **What does value mean?**
   - **Positive:** Elevated space weather activity
   - **Negative:** Low space weather activity
   - **Magnitude:** How strong the activity is

---

## 📝 Code Summary

**Total Lines:** ~240 lines (2895-3135)
**Key Functions:**
- `StandardScaler.fit_transform()` - Normalization
- `PCA.fit_transform()` - Dimensionality reduction
- `np.isnan()` - NaN detection
- `np.full()` - Array creation

**Output:**
- 168 composite index values (one per hour)
- Statistics (min, max, mean, std, variance explained)
- Added to API response for frontend

---

## ✅ Verification

Check logs for:
```
🔍 Composite Index Calculation:
   Expected params: ['Dst_Index_nT', 'ap_index_nT', 'Sunspot_Number', 'Kp_10']
   Available in df: ['Dst_Index_nT', 'ap_index_nT', 'Sunspot_Number', 'Kp_10']
   Data matrix shape: (168, 4)
   Valid rows: 168 / 168
   Normalized data shape: (168, 4)
   PC1 shape: (168, 1), variance explained: 0.75
   Composite index length: 168
✓ Composite Index calculated using PCA
✅ Composite Index added to response: 168 values
```

