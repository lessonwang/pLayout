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
### 曲線積分
---
```
c = sub(cycleIntegralSign(3),"C")
res = hcombine("W = ",c,"F \u22c5 ds")
print(res)
```
結果：
```
       --       
      /         
      ¦         
W =  (¦)  F ⋅ ds
      ¦         
      /         
    --          
         C      
```
### 共軛複數
---
```
real = fence(frac(2,3))
imag = fence(frac(5,7))
comx = hcombine(real," + ",imag," j")
w = dimension(comx)["width"]
left = vcombine("_"*w,comx)
lw = dimension(left)["width"]
lh = dimension(left)["rows"]
right = hcombine(" = ",real," - ",imag," j")
right = expand(right,lw,lh,valign="bottom")
res = hcombine(left,right)
print(res)
```
結果：
```
_______________                  
/ 2 \   / 5 \     / 2 \   / 5 \  
¦---¦ + ¦---¦ j = ¦---¦ - ¦---¦ j
\ 3 /   \ 7 /     \ 3 /   \ 7 /  
```
