# import base64

def ksa(K):
    S = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + S[i] + K[i % len(K)]) % 256
        S[i], S[j] = S[j], S[i]
    return(S)

def prga(S, P):
    i = 0
    j = 0
    hasil = ""
    for idx in range(len(P)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        u = S[t] # Keystream
        c = u ^ ord(P[idx])
        hasil += (chr(c))
    return(hasil)
    # print(hasil.encode("utf-8"))
    # print(base64.b64encode(bytes(hasil,"utf8")))
    # print(hasil)
    # for character in hasil :
    #     print(hex(character))

def keyMakers(K):
    key_tmp = [ord(x) for x in K]
    return key_tmp

# plain = input()
# key = input()
# prga(ksa(keyMakers(key)), plain)
