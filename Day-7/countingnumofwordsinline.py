n=input("enter ur text:-")
l=[]
for i in range(len(n)):
    l.append(i)
print("wordlength",len(l))    
v="aeiouAEIOU"
c="A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z: a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
for j in n:
    if j in v:
        print("vowels:-",j)
for k in n:        
    if j in c:
        print("consonants",k)    

