def AdaptiveThershold(imgIn, imgOut, w, h):
    i=0
    j=0
    for i in range(w):
        sum =0
        for j in range(h):
            sum += imgIn[i,j]
            if i==0:
                imgIn[i,j]=sum
            else:
                imgIn[i,j]= imgIn[i-1, j] + sum
    
    i=0
    j=0
    for i in range(w):
        for j in range(h):
            x1=i-

