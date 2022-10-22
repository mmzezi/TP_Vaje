'''
for _ in range(51):
    for i in range(2,x):
        if x % i == 0:
            print(f'{x} ni praštevilo.')
            break
        else:
            print(f'{x} je praštevilo.')
            break
'''
z = 51
s = 0

print("Praštevila med", s, "in", z, "so:")

for x in range (s, z):
    if x > 1:
        for i in range(2,x): #več od 2, 1 ne more bit praštevilo, 2 je vedno praštevilo
            if (x % i) == 0: #preverimo ostanek pri deljenju z števili pod sabo, če ima pod sabo delitelja ne more biti praštevilo
                break
        else:
            print(x)
