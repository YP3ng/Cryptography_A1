'''
Plaintext:  PMZRTZ YFQFTP IRBRXX KECAHR PMZRTZ YZHHKB JCJGHK VYNGQX
Ciphertext: XRDREZ LEBJCJ GXOHHK VUPYON XRDREZ HZHPRB JVGLHM SPNJBU
same char:     R Z                         R Z  ZH  B J   H    N
'''
import numpy as np

# Map characters to numbers
char_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_,."

char_map = {}
val = 0
for idx in range(len(char_string)):
    char_map[char_string[idx]] = val
    val += 1
#print(char_map)
# m = 6
# Y = AX

Plaintext = "PMZRTZYFQFTPIRBRXXKECAHRPMZRTZYZHHKBJCJGHKVYNGQX"
Ciphertext = "XRDREZLEBJCJGXOHHKVUPYONXRDREZHZHPRBJVGLHMSPNJBU"

same_char_idx = []
for i in range(len(Plaintext)):
    if Plaintext[i] == Ciphertext[i]:
        same_char_idx.append(i % 6)
#print(same_char_idx)
# Vigenere cipher
Vigenere_key = [5 ,21 ,16 ,13 ,21 ,4]

def calculator(Plaintext, Ciphertext, position):

    A = []
    B = []
    count = 0
    while (count < 6):

        cur_posit = position + count * 6

        # Find out all the Ys
        B_sub = []
        i = 0
        for ele in Ciphertext[cur_posit - position: cur_posit - position + 6]:
            B_sub.append((char_map.get(ele) - Vigenere_key[i]) % 29)
            i += 1
        

        B.append(B_sub)

        # Find out all the Xs
        A_sub = []
        for ele in Plaintext[cur_posit - position: cur_posit - position + 6]:
            A_sub.append(char_map.get(ele))
        A.append(A_sub)
        count += 1


    # Calculate K
    A = np.array(A)
    #print("original Plaintext \n",A)
    B = np.array(B)
    #print("\npre-Vigenere Ciphertext \n",B)

    inv_A = np.linalg.inv(A)
    #print("\n", inv_A)

    

    K_sub = np.matmul(inv_A, B)
    res = np.mod(K_sub, 29)
    return res

ciphertext = "SWNEJVTIOFTONPACOWIFPWARPMOVEISNTUNTRINRUTBHASHB" #fvqnve 5 21 16 13 21 4
K = calculator(Plaintext, Ciphertext, 0)
print(K)
print(np.linalg.inv(K))

def de_Vigenere(Plaintext, Ciphertext):
    res = []
    print("Plaintext: ", Plaintext)
    print("Ciphertext: ", Ciphertext)
    for idx in range(len(Ciphertext)):
       val = char_map.get(Ciphertext[idx]) - char_map.get(Plaintext[idx])
       res.append(val % 29)

    return res

#print(de_Vigenere(ciphertext, Ciphertext))
cipher_b = "VQWBUQIDKILMWT_WJBBUDVKJWTOUTFOMVZZ,OFJRDMNK,.TZBZWUXU"
de2_cipher_b = "QYGR3MDLXYTIR2_GZJ1PLF1RSOWEGNKHAJM,WBEZQ3VG,.OEOMBQS3" # change numbers