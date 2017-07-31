def cycleIntegralSign(height):
  try:
    height = int(height)
    if height == 1:
      return "\n".join(["   --","  /  "," (\u00a6) ","  /  ","--   "])
    elif height > 1:
      height = height if height % 2 else (height + 1)
      tmp = height // 2
      return "\n".join(["   --","  /  ",("  \u00a6  \n"*tmp)[:-1]," (\u00a6) ",("  \u00a6  \n"*tmp)[:-1],"  /  ","--   "])
    else:
      return "\n".join(["   --","  /  ",("  \u00a6  \n"*2)[:-1]," (\u00a6) ",("  \u00a6  \n"*2)[:-1],"  /  ","--   "])
  except:
    return "\n".join(["   --","  /  ",("  \u00a6  \n"*2)[:-1]," (\u00a6) ",("  \u00a6  \n"*2)[:-1],"  /  ","--   "])

def dimension(string):
	try:
		res = {}
		string=str(string)
		if not string:
		  return {"rows":0,"width":0}
		else:
		  res["rows"] = len(string.split("\n"))
		  res["width"] = max(map(len,string.split("\n")))
		  return res
	except:
		return {"width":None,"rows":None}
		
def expand(string,width,rows,align="center",valign="middle",chrs=" "):
	try:
		chrs = chrs if len(chrs) == 1 else chrs[0]
		lines = str(string).split("\n")
		diff = rows - len(lines)
		half_diff = diff // 2
		rest_diff = diff - half_diff
		width = width if width > dimension(str(string))["width"] else dimension(str(string))["width"]
		if align == "center":
			for i in range(len(lines)):
				lines[i] = insert_chrs(lines[i],width,chrs=chrs,ends="both")
		elif align == "left":
			for i in range(len(lines)):
				lines[i] = insert_chrs(lines[i],width,chrs=chrs,ends="right")
		elif align == "right":
			for i in range(len(lines)):
				lines[i] = insert_chrs(lines[i],width,chrs=chrs,ends="left")
		if valign == "middle":
			for _ in range(half_diff):
				lines.insert(0,chrs*width)
			for _ in range(rest_diff):
				lines.append(chrs*width)
		elif valign == "top":
			for _ in range(diff):
				lines.append(chrs*width)
		elif valign == "bottom":
			for _ in range(diff):
				lines.insert(0,chrs*width)
		return "\n".join(lines)
	except:
		print("Can't expand this string")

def fence(inner):
  try:
    inner = justify(inner)
    lines = inner.split("\n")
    if len(lines) == 1:
      return "("+inner+")"
    else:
      lines[0] = "/"+lines[0]+"\\"
      lines[-1] = "\\"+lines[-1]+"/"
      for i in range(1,len(lines)-1):
        lines[i] = "".join(["\u00a6",lines[i],"\u00a6"])
      return "\n".join(lines)
  except:
    return inner

def frac(num,den):
  try:
    expand_width = max(dimension(str(num))["width"],dimension(str(den))["width"])+2
    expand_rows = max(dimension(str(num))["rows"],dimension(str(den))["rows"])
    num = expand(str(num),expand_width,expand_rows)
    den = expand(str(den),expand_width,expand_rows)
    return vcombine(num,"-"*expand_width,den,eqh=False)
  except:
    print("Can't generate fraction.")

def hcombine(*elements,eqw=False):
  try:
    jus_elements = list(map(justify,elements))
    width_list = [dimension(x)["width"] for x in jus_elements]
    if not eqw:
      expand_rows = max(dimension(x)["rows"] for x in jus_elements)
      jus_elements = [expand(x,dimension(x)["width"],expand_rows) for x in jus_elements]
      res = []
      for i in range(expand_rows):
        tmp = []
        for j in range(len(jus_elements)):
          tmp.append(jus_elements[j].split("\n")[i])
        res.append("".join(tmp))
      return "\n".join(res)
    else:
      expand_rows = max(dimension(x)["rows"] for x in jus_elements)
      expand_width = max(dimension(x)["width"] for x in jus_elements)
      jus_elements = [expand(x,expand_width,expand_rows) for x in jus_elements]
      res = []
      for i in range(expand_rows):
        tmp = []
        for j in range(len(jus_elements)):
          tmp.append(jus_elements[j].split("\n")[i])
        res.append("".join(tmp))
      return "\n".join(res)      
  except:
    print("Can't combine horizontally.")

def insert_chrs(string,width,chrs=" ",ends="both"):
  try:
    string = str(string)
    diff = width - len(string)
    half_diff = diff // 2
    rest_diff = diff - half_diff
    chrs = chrs if len(chrs) == 1 else chrs[0]
    if ends == "both":
      return "".join([chrs*half_diff,string,chrs*rest_diff])
    elif ends == "right":
      return "".join([string,chrs*diff])
    elif ends == "left":
      return "".join([chrs*diff,string])
    else:
      return string
  except:
    return string

def integralSign(height):
  try:
    height = int(height)
    return "\n".join(["   --","  /  ",("  \u00a6  \n"*height)[:-1],"  /  ","--   "])
  except:
    return "\n".join(["   --","  /  ",("  \u00a6  \n"*5)[:-1],"  /  ","--   "])

def isFullString(string):
  w = dimension(str(string))["width"]
  r = dimension(str(string))["rows"]
  return w * r + (r - 1) == len(str(string))
		
def justify(string,align="center",chrs=" "):
	try:
		lines = str(string).split("\n")
		max_width = max(map(len,lines))
		chrs = chrs if len(chrs) == 1 else chrs[0]
		for i in range(len(lines)):
			if align == "center":
				lines[i] = insert_chrs(lines[i],max_width,chrs=chrs,ends="both")
			elif align == "left":
				lines[i] = insert_chrs(lines[i],max_width,chrs=chrs,ends="right")
			elif align == "right":
				lines[i] = insert_chrs(lines[i],max_width,chrs=chrs,ends="left")
		return "\n".join(lines)
	except:
		return string

def productSign(height):
  try:
    height = int(height)
    height = height if height >=5 else 5
    tmp = height if height % 2 else (height + 1)
    return "\n".join(["_"*tmp,((" \u00a6"+" "*(tmp-4)+"\u00a6 \n")*(tmp//2))[:-1]])
  except:
    return "\n".join(["_"*5,(" \u00a6 \u00a6 \n"*2)[:-1]])

def sqrt(inner):
  try:
    inner = justify(inner)
    right_part = vcombine("_"*dimension(inner)["width"],inner)
    left_part = hcombine(" \n"*dimension(inner)["rows"]+"\\"," \n"+("\u00a6\n"*dimension(inner)["rows"])[:-1])
    return hcombine(left_part,right_part)
  except:
    print("Can't generate square root")

def sub(base,subscript,shift=0):
  try:
    base = justify(base)
    subscript = justify(subscript)
    expand_width = dimension(base)["width"]+dimension(subscript)["width"]
    max_shift = min(dimension(base)["rows"],dimension(subscript)["rows"])
    if shift == 0:
      return vcombine(expand(base,expand_width,dimension(base)["rows"],align="left"),expand(subscript,expand_width,dimension(subscript)["rows"],align="right"))
    elif shift > 0 and shift < max_shift:
      top = "\n".join(base.split("\n")[:-shift])
      top = expand(top,expand_width,dimension(top)["rows"],align="left")
      middle = hcombine("\n".join(base.split("\n")[-shift:]),"\n".join(subscript.split("\n")[:shift]))
      bottom = "\n".join(subscript.split("\n")[shift:])
      bottom = expand(bottom,expand_width,dimension(bottom)["rows"],align="right")
      return vcombine(top,middle,bottom)
  except:
    print("Can't generate subscript")

def subsup(base,subscript,superscript,bshift=0,pshift=0):
  try:
    base = justify(base)
    subscript = justify(subscript)
    superscript = justify(superscript)
    expand_width = dimension(base)["width"]+max(dimension(subscript)["width"],dimension(superscript)["width"])
    tmp_width = max(dimension(subscript)["width"],dimension(superscript)["width"])
    max_bshift = min(dimension(base)["rows"],dimension(subscript)["rows"])
    max_pshift = min(dimension(base)["rows"],dimension(superscript)["rows"])
    if bshift == 0 and pshift == 0:
      subscript = expand(subscript,tmp_width,dimension(subscript)["rows"],align="left")
      superscript = expand(superscript,tmp_width,dimension(superscript)["rows"],align="left")
      return vcombine(expand(superscript,expand_width,dimension(superscript)["rows"],align="right"),expand(base,expand_width,dimension(base)["rows"],align="left"),expand(subscript,expand_width,dimension(subscript)["rows"],align="right"))
    elif (bshift > 0 and bshift < max_bshift) and (pshift > 0 and pshift < max_pshift) and ((bshift+pshift) < dimension(base)["rows"]):
      subscript = expand(subscript,tmp_width,dimension(subscript)["rows"],align="left")
      superscript = expand(superscript,tmp_width,dimension(superscript)["rows"],align="left")
      top_first = "\n".join(superscript.split("\n")[:-pshift])
      top_first = expand(top_first,expand_width,dimension(top_first)["rows"],align="right")
      top_second = hcombine("\n".join(base.split("\n")[:pshift]),"\n".join(superscript.split("\n")[-pshift:]))
      middle = "\n".join(base.split("\n")[pshift:-bshift])
      middle = expand(middle,expand_width,dimension(middle)["rows"],align="left")
      bottom_second = hcombine("\n".join(base.split("\n")[-bshift:]),"\n".join(subscript.split("\n")[:bshift]))
      bottom_first = "\n".join(subscript.split("\n")[bshift:])
      bottom_first = expand(bottom_first,expand_width,dimension(bottom_first)["rows"],align="right")
      return vcombine(top_first,top_second,middle,bottom_second,bottom_first)
    elif (bshift > 0 and bshift < max_bshift) and pshift == 0:
      subscript = expand(subscript,tmp_width,dimension(subscript)["rows"],align="left")
      superscript = expand(superscript,tmp_width,dimension(superscript)["rows"],align="left")
      top = sup("\n".join(base.split("\n")[:-bshift]),superscript)
      middle = hcombine("\n".join(base.split("\n")[-bshift:]),"\n".join(subscript.split("\n")[:bshift]))
      bottom = "\n".join(subscript.split("\n")[bshift:])
      bottom = expand(bottom,expand_width,dimension(bottom)["rows"],align="right")
      return vcombine(top,middle,bottom)
    elif (pshift > 0 and pshift < max_pshift) and bshift == 0:
      subscript = expand(subscript,tmp_width,dimension(subscript)["rows"],align="left")
      superscript = expand(superscript,tmp_width,dimension(superscript)["rows"],align="left")
      top = "\n".join(superscript.split("\n")[:-pshift])
      top = expand(top,expand_width,dimension(top)["rows"],align="right")
      middle = hcombine("\n".join(base.split("\n")[:pshift]),"\n".join(superscript.split("\n")[-pshift:]))
      bottom = sub("\n".join(base.split("\n")[pshift:]),subscript)
      return vcombine(top,middle,bottom)
    else:
      raise BaseException
  except:
    print("Can't generate subscript and superscript simultaneously.")

def summaSign(height):
  try:
    height = int(height)
    height = height if height >=6 else 6
    height = (height + 1) if height % 2 else height
    width = (height - 2) // 2 + 2
    res = []
    res.append("-"*width)
    res.append("\\"+" "*(width - 1))
    tmp = (height - 4) // 2
    for i in range(1,tmp + 1):
      res.append("".join([" "*i,"\\"," "*(width - i - 1)]))
    for i in range(tmp,0,-1):
      res.append("".join([" "*i,"/"," "*(width - i - 1)]))
    res.append("/"+" "*(width - 1))
    res.append("-"*width)
    return "\n".join(res)
  except:
    return "\n".join(["-"*4,"\\   "," \\  "," /  ","/   ","-"*4])

def sup(base,superscript,shift=0):
  try:
    base = justify(base)
    superscript = justify(superscript)
    expand_width = dimension(base)["width"]+dimension(superscript)["width"]
    max_shift = min(dimension(base)["rows"],dimension(superscript)["rows"])
    if shift == 0:
      return vcombine(expand(superscript,expand_width,dimension(superscript)["rows"],align="right"),expand(base,expand_width,dimension(base)["rows"],align="left"))
    elif shift > 0 and shift < max_shift:
      top = "\n".join(superscript.split("\n")[:-shift])
      top = expand(top,expand_width,dimension(top)["rows"],align="right")
      middle = hcombine("\n".join(base.split("\n")[:shift]),"\n".join(superscript.split("\n")[-shift:]))
      bottom = "\n".join(base.split("\n")[shift:])
      bottom = expand(bottom,expand_width,dimension(bottom)["rows"],align="left")
      return vcombine(top,middle,bottom)
  except:
    print("Can't generate superscript.")

def tablelayout(elementList,hsep=" ",vsep=" "):
  try:
    hsep,vsep = str(hsep),str(vsep)
    hsep = hsep if len(hsep) == 1 else hsep[0]
    vsep = vsep if len(vsep) == 1 else vsep[0]
    numberRows = len(elementList)
    numberColumns = len(elementList[0])
    flat_elem = [justify(x) for sublist in elementList for x in sublist]
    expand_width = max(dimension(x)["width"] for x in flat_elem)
    expand_rows = max(dimension(x)["rows"] for x in flat_elem)
    flat_elem = [expand(x,expand_width,expand_rows) for x in flat_elem]
    res = []
    for i in range(0,len(flat_elem),numberColumns):
      tmp = []
      tmp.append(flat_elem[i])
      for j in range(1,numberColumns):
        tmp.append(((hsep+"\n")*expand_rows)[:-1])
        tmp.append(flat_elem[i+j])
      res.append(hcombine(*tmp))
      res.append(vsep*(expand_width*numberColumns+(numberColumns-1)))
    return vcombine(*res[:-1])
  except:
    print("Can't generate table layout.")
		
def vcombine(*elements,eqh=False):
  try:
    if not eqh:
      expand_width = max(dimension(x)["width"] for x in elements)
      return "\n".join(expand(str(x),expand_width,dimension(x)["rows"]) for x in elements)
    else:
      expand_width = max(dimension(x)["width"] for x in elements)
      expand_rows = max(dimension(x)["rows"] for x in elements)
      return "\n".join(expand(x,expand_width,expand_rows) for x in elements)
  except:
    print("Can't combine vertically")
#
