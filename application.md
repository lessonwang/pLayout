### 片段函數
---
```
#定義左大括號
def lfence(height):
  height = int(height)
  height = height if height % 2 else (height + 1)
  tmp = height // 2
  return "\n".join([" /",(" \u00a6\n"*tmp)[:-1],"< ",(" \u00a6\n"*tmp)[:-1]," \\"])
t = tablelayout([["-x","if x < 0"],["x","if x \u2265 0"]])
h = dimension(t)["rows"]
right = hcombine(lfence(h),t)
res = hcombine("|x| = ",right)
print(res)
```
結果：
```
       /                 
       ¦   -x    if x < 0
|x| = <                  
       ¦   x     if x ≥ 0
       \                 
```
### 級數
---
```
series = frac(1,"k(k + 1)")
h = dimension(series)["rows"]
summa = vcombine('n',summaSign(h),'k = 1')
left = hcombine(summa,series)
right = frac('n','n + 1')
print(hcombine(left," = ",right))
```
結果：
```
  n                      
----                     
\        1           n   
 \   ---------- = -------
 /    k(k + 1)     n + 1 
/                        
----                     
k = 1                    
```
