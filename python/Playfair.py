print("\n- - - Playfair Cipher Code - - -\n")
alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
s = input("Enter Your Message : ").upper()

if len(s)%2 != 0 :
    s+='X'
# print(s)
key = list(input("\nEnter Key : ").upper())
newkey=[]

for i in key:
    if i not in newkey:
        newkey.append(i)
# Removing Duplicates in key

for ch in newkey:
    alpha.remove(ch)
# Removing characters from alpha
# which are present in newkey

newkey.extend(alpha)

M = []

for i in range(6):
    l=[]
    for j in range(6):
        l.append(newkey.pop(0))
    M.append(l)

print("\n-----------------\nMatrix : \n")

for i in range(6):
    print(*M[i])
print("-----------------\n")

print(f"Message Before Encryption : {s}")
ans=""

for i in range(0,len(s),2):
    ch1 = s[i]
    ch2 = s[i+1]

    for j in range(6):
        for k in range(6):
            if M[j][k] == ch1:
                r1 = j
                c1 = k
            if M[j][k] == ch2:
                r2 = j
                c2 = k

    if r1 == r2:
        if c1 == 5:
            ans+=M[r1][0]
        else :
            ans+=M[r1][c1+1]

        if c2 == 5:
            ans+=M[r1][0]
        else :
            ans+=M[r1][c2+1]

    elif c1 == c2:
        if r1 == 5:
            ans+=M[0][c1]
        else :
            ans+=M[r1+1][c1]

        if r2 == 5:
            ans+=M[0][c1]
        else:
            ans+=M[r2+1][c1]

    else:
        ans+=M[r1][c2]
        ans+=M[r2][c1]

print(f"Message After Encryption : {ans}")

ans2=""

for i in range(0,len(ans),2):
    ch1 = ans[i]
    ch2 = ans[i+1]

    for j in range(6):
        for k in range(6):
            if M[j][k] == ch1:
                r1 = j
                c1 = k
            if M[j][k] == ch2:
                r2 = j
                c2 = k

    if r1 == r2:
        if c1 == 0:
            ans2+=M[r1][5]
        else :
            ans2+=M[r1][c1-1]

        if c2 == 0:
            ans2+=M[r1][5]
        else :
            ans2+=M[r1][c2-1]

    elif c1 == c2:
        if r1 == 0:
            ans2+=M[5][c1]
        else :
            ans2+=M[r1-1][c1]

        if r2 == 0:
            ans2+=M[5][c1]
        else:
            ans2+=M[r2-1][c1]

    else:
        ans2+=M[r1][c2]
        ans2+=M[r2][c1]

print(f"Message After Decryption : {ans2}")
