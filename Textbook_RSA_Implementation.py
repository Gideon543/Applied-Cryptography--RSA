# necessary imports 
from Crypto.Util import number  
from random import randint 

# function to check the validity of a provided bit size. 
def check_bit_size(bits): 
    if bits > 2048: 
        bits = 8 
    return bits 
 
bits = check_bit_size(12) 
print(f"RSA-{bits} IMPLEMENTATION") 
print("=" * 20) 
 
# generate random primes 
p = number.getPrime(bits)  
q = number.getPrime(bits)

 
# Computing Key- function to compute key 
def compute_key():  
    E = 65537 
    N = p*q  
    return (E,N) 


# Encryption- function to encrypt text, P 
def encrypt(P, key):  
    E = key[0]  
    N = key[1]  

    C = (P**E) % N  
    return C 

 
# Extended Euclidean Algorithm- function for extended Euclidean Algorithm 
def gcdExtended(a, b): 

    # Base Case 
    if a == 0 : 
        return b,0,1 
    gcd,x1,y1 = gcdExtended(b%a, a) 

    # Update x and y using results of recursive call 
    x = y1 - (b//a) * x1 
    y = x1 
    return gcd,x,y 


# Decryption - function to decrypt cipher text 
def decrypt(C, key):  
    F = (p - 1) * (q - 1)  
    E = key[0]  
    N = key[1]  
    D,x,y = gcdExtended(E,F) 

    if x < 0:  
        x = F + x 
        print(f'The decryption key computed with the Extend Euclidean algorithm = {x}')  

    P = (C**x) % N  
    return P  

 

# Displaying Results 
def compute(P): 
    print(f"Number of bits in primes is {bits}") 

    print(f'Plaintext provided for encryption is {P}') 

    key = compute_key() 

    print(f'The computed key for both RSA encryption and decryption is (E = {key[0]}, N = {key[1]})') 

    C = encrypt(P,key)  

    print(f'RSA encrytion (C = P^E mod N) of the plaintext produces {C}') 

    P = decrypt(C, key) 

    print(f'RSA decrytion (P = C^D mod N) of the ciphertext produces {P}') 

    print() 
