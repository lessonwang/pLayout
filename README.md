### pLayout 簡介
---
`pLayout`是一個簡單的排版模組，目前只支援ASCII和單字節的unicode字元在終端機或主控台視窗上的排版；嘗試非單字節字元的排版會使得排版跑位，造成非預期的效果。<br/>
可以使用`pLayout`做一些簡單地數學排版或一些ASCII art。<br/>
### 字串的寬度和列數
---
在`pLayout`中的所有字串，都視為一個矩形的方塊，並且擁有寬度和列數。<br/>
一個字串的寬度`width`定義為：字串列印在終端機或主控台上的每一列當中，找尋哪一列具有最多的字元數，這個數字就是此字串的寬度。<br/>
一個字串的列數`rows`定義為：字串列印在終端機或主控台上所顯示的列數即為此字串的列數。<br/>
### dimension函數
---
在`pLayout`中可以使用`dimension`函數來確認一個字串的列數和寬度，只要把此字串傳入`dimension`的引數中即可。<br/>
此函數的結果會傳回一個dictionary，其中包含兩個key，分別是`rows`和`width`。<br/>
例如：
```
s = "st\n2nd line\n3rd"
print(s)
print(dimension(s))
```
列印出來的結果如下：
```
st
2nd line
3rd
{'rows': 3, 'width': 8}
```
可以看出，字串`s`列印出來有3列，因此字串`s`的列數`rows`為3，而其中第2列的字元數是這3列當中最多的，因此字串`s`的寬度`width`為8。<br/>
對於一個空字串而言：
```
s = ""
print(s)
print(dimension(s))
```
列印出來的結果顯示如下：
```

{'rows': 0, 'width': 0}
```
顯然地，空字串的列數和寬度皆為零。
### 完滿字串 v.s. 非完滿字串
---
若一個字串的每一列字元數都相同，則稱為**完滿字串**；反之，則稱為**非完滿字串**。<br/>
換句話說，一個字串的矩形區域內，任何一個位置都有字元的狀態，就是**完滿字串**，也就是所有字元都填滿了這個字串的矩形區域。<br/>
### isFullString函數
---
在`pLayout`中可以使用`isFullString`函數來確認一個字串是否為完滿字串，只要把此字串傳入`isFullString`的引數中即可。<br/>
此函數的結果會傳回一個邏輯值，如果是**完滿字串**，則會傳回True；否則，傳回False。<br/>
例如：
```
s1 = "123\n12345\n1"
print(s1)
print(isFullString(s1))
```
列印出來的結果顯示如下：
```
123
12345
1
False
```
若把字串`s1`稍作修改如下：
```
s1 = "12345\n12345\n12345"
print(s1)
print(isFullString(s1))
```
列印出來的結果顯示如下：
```
12345
12345
12345
True
```
顯然地，對於單列的字串(字串中沒有換行字元)，一定是**完滿字串**；空字串，一定是**非完滿字串**。
### justify函數
---
在`pLayout`中可以使用`justify`函數將一個字串利用填補字元的方式來形成**完滿字串**。<br/>
第一個引數：要形成**完滿字串**的原字串。<br/>
第二個為關鍵字引數`align`：指定形成**完滿字串**時，字串中每一列的對齊方式，值有三種可選擇，分別是`left`靠左對齊、`center`置中對齊、`right`靠右對齊；若沒有指定此引數，預設值為`center`。<br/>
第三個為關鍵字引數`chrs`：指定形成**完滿字串**時，要使用哪個字元來填滿；若沒有指定此引數，預設值為一個半形空白；此外，若`chrs`的長度大於1，那麼只會取第一個字元當作填滿的字元。<br/>
此函數的結果會傳回一個經過格式化的**完滿字串**。<br/>
例如：
```
s = "st\n2nd line\n3rd"
print(s)
print(isFullString(s))
s = justify(s)
print(s)
print(isFullString(s))
```
列印出來的結果顯示如下：
```
st
2nd line
3rd
False
   st   
2nd line
  3rd   
True
```
字串`s`原本3列的字元數都不相同，使用`justify`函數後，並使用`justify`函數預設的引數，使字串`s`變成完滿字串。<br/>
由於使用`justify`函數中`chrs`引數的預設值(半形空白)，看不出差異，上面的結果可以使用**反白**來觀看每一列的字元數是否相同。<br/>
因此，使用下面的例子使用不同的`chrs`及`align`值來展示：
```
s = "st\n2nd line\n3rd"
s1 = justify(s,align="right",chrs="-+")
print(s1)
print(isFullString(s1))
s2 = justify(s,align="left",chrs="+-")
print(s2)
print(isFullString(s2))
```
列印出來的結果顯示如下：
```
------st
2nd line
-----3rd
True
st++++++
2nd line
3rd+++++
True
```
上面的結果也顯示`chrs`引數的值之長度大於1，會以第一個字元當作填滿的字元。
### expand函數
---
在`pLayout`中可以使用`expand`函數將一個字串利用填補字元的方式來擴大此字串的寬度和列數。<br/>
第一個引數：要被擴大寬度或列數的原字串。<br/>
第二個引數：指定擴大之後的寬度。<br/>
第三個引數：指定擴大之後的列數。<br/>
第四個為關鍵字引數`align`：指定字串中每一列的對齊方式，值有三種可選擇，分別是`left`靠左對齊、`center`置中對齊、`right`靠右對齊；若沒有指定此引數，預設值為`center`。<br/>
第五個為關鍵字引數`valign`：指定字串在矩形區域內垂直方向上的對齊方式，值有三種可選擇，分別是`top`靠上對齊、`middle`置中對齊、`bottom`靠下對齊；若沒有指定此引數，預設值為`middle`。<br/>
第六個為關鍵字引數`chrs`：指定要使用哪個字元來填滿，若沒有指定此引數，預設值為一個半形空白；此外，若`chrs`的長度大於1，那麼只會取第一個字元當作填滿的字元。<br/>
此函數的結果會傳回一個經過擴大寬度或擴大列數的**完滿字串**。<br/>
以下舉一些例子：
```
s = "abcde\ndefgh\nploki"
s = expand(s,9,7,align="left",valign="top",chrs=".")
print(s)
print(isFullString(s))
```
列印出來的結果顯示如下：
```
abcde....
defgh....
ploki....
.........
.........
.........
.........
True
```
上面的例子，是將原字串靠左上對齊後的結果。
```
s = "abcde\ndefgh\nploki"
s = expand(s,9,7,align="right",valign="bottom",chrs="-")
print(s)
print(isFullString(s))
```
列印出來的結果顯示如下：
```
---------
---------
---------
---------
----abcde
----defgh
----ploki
True
```
上面的例子，是將原字串靠右下對齊後的結果。
### fence函數
---
在`pLayout`中可以使用`fence`函數來將一個字串括住，只要把此字串傳入`fence`的引數中即可。<br/>
此函數的結果會傳回一個被括住的**完滿字串**；須注意的是，若傳入的字串是單列字串，那麼預設會以一對小括號括住字串，兩列以上的字串就會使用排版來括住字串。<br/>
以下是單列字串的效果：
```
s = "3+4*5/6%7**8"
s = fence(s)
print(s)
print(isFullString(s))
```
列印出來的結果顯示如下：
```
(3+4*5/6%7**8)
True
```
以下是兩列字串的效果：
```
s = "first line\nsecond line"
s = fence(s)
print(s)
print(isFullString(s))
```
列印出來的結果顯示如下：
```
/first line \
\second line/
True
```
以下是多列字串的效果：
```
s = "1st line...\n2nd line......\n3rd line\n4th line\n5th line"
s = fence(s)
print(s)
print(isFullString(s))
```
列印出來的結果顯示如下：
```
/ 1st line...  \
¦2nd line......¦
¦   3rd line   ¦
¦   4th line   ¦
\   5th line   /
True
```
可以看出來，對於一個沒有經過`justify`函數的字串，傳入`fence`函數之後會格式化括號內部，因此從這裡可以看出來，`fence`函數預設會套用`justify`函數，並使用置中對齊和半形空白補足剩下的區域。<br/>
當然，對於嵌套的`fence`函數也可以接受：
```
s = "1st line\n2nd line\n3rd line"
s = fence(fence(s))
print(s)
print(isFullString(s))
```
列印出來的結果顯示如下：
```
//1st line\\
¦¦2nd line¦¦
\\3rd line//
True
```
和`expand`函數搭配：
```
s = "1st line\n2nd line\n3rd line"
s = fence(expand(s,12,5,chrs="="))
print(s)
print(isFullString(s))
```
列印出來的結果顯示如下：
```
/============\
¦==1st line==¦
¦==2nd line==¦
¦==3rd line==¦
\============/
True
```
### frac函數
---
在`pLayout`中可以使用`frac`函數做一個類似分數或分式的排版，或者用「-」符號來隔開上下兩部分。<br/>
第一個引數：分數或分式的分子部分。<br/>
第二個引數：分數或分式的分母部分。<br/>
此函數的結果也會是一個**完滿字串**。<br/>
最簡單的就是用於排版分數：
```
s = frac(100,30117)
print(s)
```
列印出來的結果顯示如下：
```
  100  
-------
 30117 
```
當然也可以接受具有未知數的分子或分母：
```
s = frac(100,'xyz')
print(s)
```
列印出來的結果顯示如下：
```
 100 
-----
 xyz 
```
分子或分母帶有分數也可以：
```
num = frac(1,'x')
s = frac(fence(num),10000)
print(s)
```
列印出來的結果顯示如下：
```
 / 1 \ 
 ¦---¦ 
 \ x / 
-------
       
 10000 
       
```
### hcombine函數
---
在`pLayout`中可以使用`hcombine`函數做水平方向上由左至右依序地字串結合，此函數接受許多個引數。<br/>
第一個引數至倒數第二個引數：要被結合的字串。<br/>
最後一個為關鍵字引數`eqw`：此引數是個邏輯值，指定各字串是否要以「等寬」的方式做結合，預設值是False，底下會以一些例子來展示有「等寬」與否的影響。<br/>
此函數的結果也會是一個**完滿字串**。<br/>
以下先示範沒有用`hcombine`函數對於結果的差別，使用`print`函數做串接：
```
left = frac(200,400)
right = frac(1,2)
print(left," = ",right)
```
列印出來的結果顯示如下：
```
 200 
-----
 400   =   1 
---
 2
```
可以明顯地看到排版跑位，原因是因為`right`字串的第一列緊接著等號後面，而`right`字串第二列之後會換行，因此會導致上面的結果。<br/>
而`hcombine`函數做的工作是把字串拆開至每一列做串接後再於每一列最後補上換行字元。<br/>
```
left = frac(200,400)
right = frac(1,2)
res = hcombine(left," = ",right)
print(res)
```
列印出來的結果顯示如下：
```
 200     1 
----- = ---
 400     2 
```
接下來，看看引數`eqw`值不同的差別：
```
left = frac(20000,40000)
right = frac(1,2)
res = hcombine(left,"=",right,eqw=False)
print(res)
res = hcombine(left,"=",right,eqw=True)
print(res)
```
列印出來的結果顯示如下：
```
 20000   1 
-------=---
 40000   2 
 20000           1   
-------   =     ---  
 40000           2   
```
可以看到`eqw`值為`True`時，會讓每一個要結合的字串調整至一樣的寬度。<br/>
`hcombine`函數應用在帶分數上：
```
f = frac(1,2)
print(hcombine(100,f))
```
列印出來的結果顯示如下：
```
    1 
100---
    2 
```
使用`hcombine`函數和`python`內建模組`fractions`的搭配應用：
```
from fractions import Fraction as F
num = 1044654
den = 25472
left = frac(num,den)
fr = F(num,den).limit_denominator()
inte = num // den
num = fr.numerator
den = fr.denominator
right = hcombine(inte,frac(num,den))
print(hcombine(left," = ",right))
```
列印出來的結果顯示如下：
```
 1044654       522327 
--------- = 41--------
  25472        12736  
```
圓周率`pi`的連分數展開：
```
res = hcombine(15," + ","...")
res = frac(1,res)
res = hcombine(7," + ",res)
res = frac(1,res)
res = hcombine(3," + ",res)
res = hcombine('pi'," = ",res)
print(res)
```
列印出來的結果顯示如下：
```
                         
                1        
                         
pi = 3 + ----------------
                  1      
          7 + ---------- 
               15 + ...  
```
### sqrt函數
---
在`pLayout`中可以使用`sqrt`函數來做一個根式的排版。<br/>
此函數的結果也會是一個**完滿字串**。<br/>
例如：
```
sq = sqrt(300)
print(sq)
sq = sqrt(frac(1,300))
print(sq)
```
列印出來的結果顯示如下：
```
  ___
\¦300
  _____
 ¦  1  
 ¦-----
\¦ 300 
```
當然可以搭配`expand`函數和`sqrt`函數來完成N次方根式的排版：
```
sq = sqrt(frac(1,300))
r = dimension(sq)["rows"]
n = expand('n',1,r,valign="top")
print(hcombine(n,sq))
```
列印出來的結果顯示如下：
```
n  _____
  ¦  1  
  ¦-----
 \¦ 300 
```
### sub函數
---
在`pLayout`中可以使用`sub`函數做一個類似下標的排版。<br/>
第一個引數：底數的部分。<br/>
第二個引數：下標的部分。<br/>
第三個為關鍵字引數`shift`：指定下標往上偏移的列數，此數字不可以超過底數部分的列數和下標部分的列數，若沒有指定，預設值是0。<br/>
此函數的結果也會是一個**完滿字串**。<br/>
以下示範不同的shift值對結果的影響：
```
f1 = frac(1,'x')
f2 = frac(2,'y')
f = fence(frac(f1,f2))
print(sub(f,f1,shift=0))
print(sub(f,f1,shift=1))
print(sub(f,f1,shift=2))
```
列印出來的結果顯示如下，往上偏移0列：
```
/  1  \   
¦ --- ¦   
¦  x  ¦   
¦-----¦   
¦  2  ¦   
¦ --- ¦   
\  y  /   
        1 
       ---
        x 
```
往上偏移1列：
```
/  1  \   
¦ --- ¦   
¦  x  ¦   
¦-----¦   
¦  2  ¦   
¦ --- ¦   
\  y  / 1 
       ---
        x 
```
往上偏移2列：
```
/  1  \   
¦ --- ¦   
¦  x  ¦   
¦-----¦   
¦  2  ¦   
¦ --- ¦ 1 
\  y  /---
        x 
```
對於上面的例子，最多就往上偏移2列，因為對於下標部分，其列數為3，所以偏移值不可以超過3。<br/>
當然，對於此函數，`hcombine`和`expand`函數搭配的效果也可以完成此函數的排版，使用上當然比`sub`函數更加地彈性，只是`sub`函數讓你有一個更快速、簡單的選擇。<br/>
```
f1 = frac(1,'x')
f2 = frac(2,'y')
f = fence(frac(f1,f2))
h_of_f1 = dimension(f1)["rows"]
w_of_f1 = dimension(f1)["width"]
h_of_f = dimension(f)["rows"]
w_of_f = dimension(f)["width"]
f1 = expand(f1,w_of_f1,h_of_f1+h_of_f,valign="bottom")
f = expand(f,w_of_f,h_of_f1+h_of_f,valign="top")
print(hcombine(f,f1))
```
列印出來的結果顯示如下：
```
/  1  \   
¦ --- ¦   
¦  x  ¦   
¦-----¦   
¦  2  ¦   
¦ --- ¦   
\  y  /   
        1 
       ---
        x 
```
可以看得出來程式碼多了很多行，非常地不簡便，但是使用上絕對是比`sub`函數更彈性，就端看自己的需求。
### sup函數
---
在`pLayout`中可以使用`sup`函數做一個類似上標的排版。<br/>
第一個引數：底數的部分。<br/>
第二個引數：上標的部分。<br/>
第三個為關鍵字引數`shift`：指定上標往下偏移的列數，此數字不可以超過底數部分的列數和上標部分的列數，若沒有指定，預設值是0。<br/>
此函數的行為就類似`sub`函數的行為，對於`shift`關鍵字引數的效果只是和`sub`函數相反，一樣地，此函數的結果也會是一個**完滿字串**。<br/>
例如：
```
f = fence(frac(1,300))
sp = fence(sup(f,frac(1,300),shift=1))
sp = sup(sp,frac(1,300),shift=1)
print(sp)
```
列印出來的結果顯示如下：
```
                1  
              -----
/         1  \ 300 
¦       -----¦     
¦/  1  \ 300 ¦     
¦¦-----¦     ¦     
\\ 300 /     /      
```
當然地，也可以使用`hcombine`和`expand`函數模擬`sup`函數的排版。
### subsup函數
---
在`pLayout`中可以使用`subsup`函數做一個類似上下標的排版。<br/>
第一個引數：底數的部分。<br/>
第二個引數：下標的部分。<br/>
第三個引數：上標的部分。<br/>
第四個為關鍵字引數`bshift`：指定下標往上偏移的列數，此數字不可以超過底數部分的列數和下標部分的列數，若沒有指定，預設值是0。<br/>
第四個為關鍵字引數`pshift`：指定上標往下偏移的列數，此數字不可以超過底數部分的列數和上標部分的列數，若沒有指定，預設值是0。<br/>
此函數的結果也會是一個**完滿字串**。<br/>
行為就類似`sub`和`sup`函數，因此以下舉一些應用的例子當作展示：
```
sbp = subsup('a'," n",'  2')
res = hcombine(sbp," + ",sbp)
print(res)
```
列印出來的結果顯示如下：
```
   2      2
a    + a   
  n      n  
```
### tablelayout函數
---
在`pLayout`中可以使用`tablelayout`函數做一個類似表格的排版。<br/>
第一個引數：一個二維的`list`，對於每一個元素，其內部元素個數要一致，否則無法排版。<br/>
第二個為關鍵字引數`hsep`：指定左右兩欄之間的分隔符號，預設值為半形空白。<br/>
第三個為關鍵字引數`vsep`：指定上下兩列之間的分隔符號，預設值為半形空白。<br/>
對於第一個引數，若有某個元素有缺少，可以使用一個空字串代替。<br/>
例如：
```
t = [[1,2,3],[89,74,20],[105,1,30541]]
table = fence(tablelayout(t,hsep="\u00a6",vsep="-"))
print(table)
```
列印出來的結果顯示如下：
```
/  1  ¦  2  ¦  3  \
¦-----------------¦
¦ 89  ¦ 74  ¦ 20  ¦
¦-----------------¦
\ 105 ¦  1  ¦30541/
```
使用空字串代替缺少的部分：
```
t = [[1,2,""],[89,"",20]]
table = fence(tablelayout(t))
print(table)
```
列印出來的結果顯示如下：
```
/1  2    \
¦        ¦
\89    20/
```
當然，表格排版不一定要應用於矩陣或向量：
```
a = "3x + 2y + 8z = 3"
b = "4x + 6y + 9z = 147"
c = "7x + 13y = 50"
t = [[a,"---(1)"],[b,"---(2)"],[c,"---(3)"]]
print(tablelayout(t))
```
列印出來的結果顯示如下：
```
 3x + 2y + 8z = 3        ---(1)      
                                     
4x + 6y + 9z = 147       ---(2)      
                                     
  7x + 13y = 50          ---(3)       
```
### vcombine函數
---
在`pLayout`中可以使用`vcombine`函數做垂直方向上由上至下依序地字串結合，此函數接受許多個引數。<br/>
第一個引數至倒數第二個引數：要被結合的字串。<br/>
最後一個為關鍵字引數`eqh`：此引數是個邏輯值，指定各字串是否要以「等高」的方式做結合，預設值是False，底下會以一些例子來展示有「等高」與否的影響。<br/>
此函數的結果也會是一個**完滿字串**。<br/>
先看`eqh`值為`False`的效果：
```
f = frac(1,'x')
print(vcombine(1,f,eqh=False))
```
列印出來的結果顯示如下：
```
 1 
 1 
---
 x 
```
再看`eqh`值為`True`的效果：
```
f = frac(1,'x')
print(vcombine(1,f,eqh=True))
```
列印出來的結果顯示如下：
```
   
 1 
   
 1 
---
 x 
```
### integralSign函數
---
在`pLayout`中可以使用`integralSign`函數做指定高度的積分符號。<br/>
第一個引數：指定積分符號的高度(列數)，若沒有指定或引數形態錯誤，預設高度為5列。<br/>
例如：
```
function = hcombine("f ",fence(frac(1,'x'))," dx")
h = dimension(function)["rows"]
it = subsup(integralSign(h),'a','b')
res = hcombine(it," ",function)
print(res)
```
列印出來的結果顯示如下：
```
     b           
   --            
  /              
  ¦      / 1 \   
  ¦    f ¦---¦ dx
  ¦      \ x /   
  /              
--               
     a           
```
### cycleIntegralSign函數
---
在`pLayout`中可以使用`cycleIntegralSign`函數做指定高度的環積分符號。<br/>
第一個引數：指定環積分符號的高度(列數)，若沒有指定或引數形態錯誤，預設高度為5列。<br/>
例如：
```
c = cycleIntegralSign(5)
c = sub(c,'C')
print(c)
```
列印出來的結果顯示如下：
```
   -- 
  /   
  ¦   
  ¦   
 (¦)  
  ¦   
  ¦   
  /   
--    
     C
```
### productSign函數
---
在`pLayout`中可以使用`productSign`函數做指定高度的連乘積符號。<br/>
第一個引數：指定連乘積符號的高度(列數)，若沒有指定或引數形態錯誤，預設高度為3列。<br/>
例如：
```
p = productSign(6)
print(p)
```
列印出來的結果顯示如下：
```
_______
 ¦   ¦ 
 ¦   ¦ 
 ¦   ¦ 
```
### summaSign函數
---
在`pLayout`中可以使用`summaSign`函數做指定高度的連加符號。<br/>
第一個引數：指定連加符號的高度(列數)，若沒有指定或引數形態錯誤，預設高度為6列。<br/>
例如：
```
s = summaSign(8)
print(s)
```
列印出來的結果顯示如下：
```
-----
\    
 \   
  \  
  /  
 /   
/    
-----
```
