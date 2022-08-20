'''
Plaintext:  PMZRTZ YFQFTP IRBRXX KECAHR PMZRTZ YZHHKB JCJGHK VYNGQX
Ciphertext: XRDREZ LEBJCJ GXOHHK VUPYON XRDREZ HZHPRB JVGLHM SPNJBU
'''
import numpy as np

# Map characters to numbers
char_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_,."

char_map = {}
val = 0
for idx in range(len(char_string)):
    char_map[char_string[idx]] = val
    val += 1

# m = 6
# Y = AX

Plaintext = "PMZRTZYFQFTPIRBRXXKECAHRPMZRTZYZHHKBJCJGHKVYNGQX"
Ciphertext = "XRDREZLEBJCJGXOHHKVUPYONXRDREZHZHPRBJVGLHMSPNJBU"

def calculator(Plaintext, Ciphertext, position):

    A = []
    B = []
    count = 0
    while (count < 6):

        cur_posit = position + count * 6

        # Find out all the Ys
        B_sub = []
        for ele in Ciphertext[cur_posit - position: cur_posit - position + 6]:
            B_sub.append(char_map.get(ele))
        dummy = sum(B_sub) % 29
        B_sub.append(dummy)
        B.append(B_sub)

        # Find out all the Xs
        A_sub = []
        for ele in Plaintext[cur_posit - position: cur_posit - position + 6]:
            A_sub.append(char_map.get(ele))
        A_sub.append(1)
        A.append(A_sub)
        count += 1
    
    A.append([1,1,1,1,1,1,0])
    B.append([0,0,0,0,0,0,0])

    # Calculate K
    A = np.array(A)
    print("original Plaintext \n",A.shape)
    B = np.array(B)
    print("\noriginal Ciphertext \n",B)

    inv_A = np.linalg.inv(A)
    print("\n", inv_A.shape)

    

    K_sub = np.matmul(inv_A, B)
    res = np.mod(K_sub, 29)
    return res

K = calculator(Plaintext, Ciphertext, 0)
print(K)