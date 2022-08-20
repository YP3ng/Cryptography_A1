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
        B.append(char_map.get(Ciphertext[cur_posit]))

        # Find out all the Xs
        A_sub = []
        for ele in Plaintext[cur_posit - position: cur_posit - position + 6]:
            A_sub.append(char_map.get(ele))
        A.append(A_sub)
        count += 1
    # Calculate K
    A = np.array(A)
    print(A)


    B = np.array(B)
    print(B)

    K_sub = np.linalg.lstsq(A, B, rcond=None)

    return np.array(K_sub)
K = []

for idx in range(1):
    K.append(calculator(Plaintext, Ciphertext, idx))
res = np.mod(K, 29)
print(res.shape)