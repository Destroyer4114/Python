for i in range(int(input())):
    print("Case #"+str(i+1)+":",end=' ')
    s= list(str(input()))
    n=[0]*(26)
    for j in range(len(s)):
        n[ord(s[j])-65]+=1
    mv= max(n[0],n[4],n[8],n[14],n[20])
    sv=n[0]+n[4]+n[8]+n[14]+n[20]
    mc=max(n[1],n[2],n[3],n[5],n[6],n[7],n[9],n[10],n[11],n[12],n[13],n[15],n[16],n[17],n[18],n[19],n[21],n[22],n[23],n[25],n[24])
    sc=n[1]+n[2]+n[3]+n[5]+n[6]+n[7]+n[9]+n[10]+n[11]+n[12]+n[13]+n[15]+n[16]+n[17]+n[18]+n[19]+n[21]+n[22]+n[23]+n[25]+n[24]
    print(min((sc+ (sv-mv)*2),(sv+ (sc-mc)*2)))



#     dic={'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
#  'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 
# 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
