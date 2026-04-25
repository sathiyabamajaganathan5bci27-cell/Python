import cmath

if __name__ == '__main__':
    z = complex(input())
    
    # Calculate modulus (r) and phase (phi)
    print(abs(z))
    print(cmath.phase(z))
