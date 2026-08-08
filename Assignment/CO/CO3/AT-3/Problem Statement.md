# Debugging Convex Hull Logic (Incorrect Inclusion of Interior Points)

**Student Name:** Raghul. D  
**Register Number:** 192425328  
**Question Number:** Q26

---

# Problem Statement

The given brute force Convex Hull algorithm incorrectly identifies some interior edges as Convex Hull edges because its validation condition is incomplete. The objective is to analyze the hull-checking logic, identify why non-boundary segments are being included, apply systematic debugging to ensure that only valid outer boundary edges are selected, optimize the checking process by avoiding unnecessary repeated evaluations where possible, analyze the time complexity of the corrected brute force solution, and present a clean and structured version of the improved logic.

## Given Code

```python
def is_hull_edge(p1, p2, points):
    for p in points:
        val = orientation(p1, p2, p)
        if val < 0:
            return False
    return True
```

---

# 1. Problem Analysis

The given function checks whether every point lies on the same side of the line formed by two points `p1` and `p2`. If any point is found on the negative side of the line, the edge is rejected. Otherwise, the edge is accepted as a Convex Hull edge.

Although this seems reasonable, the validation is incomplete because it only checks one direction of the orientation. As a result, some interior edges are incorrectly accepted as hull edges.

---

# 2. Why Interior Edges Are Included

The algorithm only verifies the following condition:

```python
if val < 0:
    return False
```

This means:

- It rejects an edge only if a point lies on the negative side.
- It never checks whether points exist on both sides of the line.
- It cannot distinguish between an outer boundary edge and an interior edge.
- Some interior line segments satisfy this condition and are mistakenly included in the Convex Hull.

Therefore, the algorithm produces incorrect Convex Hull edges.

---

# 3. Root Cause of the Bug

The validation condition is incomplete.

The algorithm assumes that if no point lies on the negative side of the candidate edge, then the edge must belong to the Convex Hull.

However, it should verify that:

- all points lie on only one side of the line,
- no points exist on both sides,
- collinear points are handled correctly.

Since these conditions are not checked, interior edges are accepted.

---

# 4. Systematic Debugging Process

## Step 1: Select a Candidate Edge

Choose every pair of points as a possible Convex Hull edge.

---

## Step 2: Compute Orientation

For every remaining point, calculate the orientation.

```python
orientation(p1, p2, p)
```

Possible results:

- Positive
- Negative
- Zero (Collinear)

---

## Step 3: Record the Side of Every Point

Maintain two Boolean variables.

```python
positive = False
negative = False
```

If

```python
val > 0
```

then

```python
positive = True
```

If

```python
val < 0
```

then

```python
negative = True
```

---

## Step 4: Reject Invalid Edges

If both variables become True,

```python
positive == True
negative == True
```

then points exist on both sides of the candidate edge.

Therefore,

```python
return False
```

The edge is not part of the Convex Hull.

---

## Step 5: Accept Valid Hull Edges

If all points lie on one side (or are collinear), then the edge belongs to the Convex Hull.

Return

```python
True
```

---

# 5. Corrected Brute Force Algorithm

```python
def orientation(p1, p2, p):
    return (p2[0]-p1[0])*(p[1]-p1[1]) - (p2[1]-p1[1])*(p[0]-p1[0])

def is_hull_edge(p1, p2, points):

    positive = False
    negative = False

    for p in points:

        if p == p1 or p == p2:
            continue

        val = orientation(p1, p2, p)

        if val > 0:
            positive = True

        elif val < 0:
            negative = True

        if positive and negative:
            return False

    return True
```

---

# 6. Optimization Applied

The original implementation checks every point even after discovering that an edge is invalid.

The improved implementation uses **early termination**.

```python
if positive and negative:
    return False
```

As soon as points are found on both sides of the candidate edge, the function immediately returns `False` without checking the remaining points.

This reduces unnecessary computations and improves practical execution time.

---

# 7. Improved Logic Flow

```text
Select Two Points
        │
        ▼
Assume Candidate Edge
        │
        ▼
Check Every Remaining Point
        │
        ▼
Compute Orientation
        │
        ▼
Positive Side?
        │
Negative Side?
        │
        ▼
Points on Both Sides?
        │
   ┌────┴────┐
   │         │
  YES        NO
   │         │
Reject     Accept
 Edge       Edge
```

---

# 8. Corrected Algorithm

1. Select every pair of points.
2. Assume the pair is a candidate Convex Hull edge.
3. Compute the orientation of every remaining point.
4. Record whether a point lies on the positive side.
5. Record whether a point lies on the negative side.
6. If points appear on both sides of the line, reject the edge immediately.
7. Otherwise, accept the edge as part of the Convex Hull.
8. Repeat the process for all possible pairs.

---

# 9. Time Complexity Analysis

Let **n** be the number of points.

### Selecting all pairs of points

```
O(n²)
```

### Checking all remaining points

```
O(n)
```

### Overall Time Complexity

```
O(n² × n)

= O(n³)
```

### Space Complexity

```
O(1)
```

Only two Boolean variables (`positive` and `negative`) are used, so the extra memory required is constant.

---

# 10. Comparison Between Original and Corrected Logic

| Original Logic | Corrected Logic |
|---------------|-----------------|
| Checks only one side of the line | Checks both sides of the line |
| Accepts some interior edges | Rejects interior edges |
| No side tracking | Uses positive and negative flags |
| Incomplete validation | Complete validation |
| Less reliable | More accurate |
| No optimization | Uses early termination |

---

# 11. Advantages of the Corrected Solution

- Correctly identifies only Convex Hull boundary edges.
- Eliminates incorrect inclusion of interior edges.
- Properly handles points on both sides of the candidate edge.
- Supports collinear points correctly.
- Uses early termination to reduce unnecessary computations.
- Requires only constant extra memory.
- Produces a more reliable Convex Hull.

---

# 12. Conclusion

The original brute force Convex Hull logic incorrectly accepted certain interior edges because it only checked whether points were on one side of a candidate edge. It failed to verify whether points existed on both sides of the line, resulting in incorrect hull formation. The corrected implementation tracks both positive and negative orientations, rejects edges that have points on opposite sides, and uses early termination to avoid unnecessary computations. Although the corrected brute force algorithm still has a time complexity of **O(n³)**, it produces an accurate Convex Hull and demonstrates systematic debugging and optimization of the original logic.
