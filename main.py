from fonctions import *

a = conv(8,8)
a = onNdigit(a,3)
print(a)

f0 = open('f0.txt', 'w')
f1 = open('f1.txt', 'w')
f2 = open('f2.txt', 'w')
f3 = open('f3.txt', 'w')

f0.write("Fichier table de vérité"+"\n")
f0.write("7"+"\n")
f0.write("Nom,c,a2,a1,a0,b2,b1,b0"+"\n")
f0.write("f0"+"\n")

f1.write("Fichier table de vérité"+"\n")
f1.write("7"+"\n")
f1.write("Nom,c,a2,a1,a0,b2,b1,b0"+"\n")
f1.write("f1"+"\n")

f2.write("Fichier table de vérité"+"\n")
f2.write("7"+"\n")
f2.write("Nom,c,a2,a1,a0,b2,b1,b0"+"\n")
f2.write("f2"+"\n")

f3.write("Fichier table de vérité"+"\n")
f3.write("7"+"\n")
f3.write("Nom,c,a2,a1,a0,b2,b1,b0"+"\n")
f3.write("f3"+"\n")

for c in range(2):
    for a in range(8):
        for b in range(8):

            A = conv(a,2)
            A = onNdigit(A,3)

            B = conv(b,2)
            B = onNdigit(B,3)

            s = conv(a+b+c, 8)
            S = onNdigit(s,2)

            s0 = conv(S[1],2)
            S0 = onNdigit(s0,3)

            S1 = S[0]

            print(c, A[0], A[1], A[2], B[0], B[1], B[2], S1, S0[0], S0[1], S0[2])

            f0.write(str(c)+","+str(A[0])+","+str(A[1])+","+str(A[2])+","+str(B[0])+","+str(B[1])+","+str(B[2])+","+str(S0[2])+"\n")
            f1.write(str(c)+","+str(A[0])+","+str(A[1])+","+str(A[2])+","+str(B[0])+","+str(B[1])+","+str(B[2])+","+str(S0[1])+"\n")
            f2.write(str(c)+","+str(A[0])+","+str(A[1])+","+str(A[2])+","+str(B[0])+","+str(B[1])+","+str(B[2])+","+str(S0[0])+"\n")
            f3.write(str(c)+","+str(A[0])+","+str(A[1])+","+str(A[2])+","+str(B[0])+","+str(B[1])+","+str(B[2])+","+str(S1)+"\n")

f0.close()
f1.close()
f2.close()
f3.close()

