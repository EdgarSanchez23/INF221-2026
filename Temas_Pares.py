import json

with open("uefa_champions_league_2011_2020.json", "r", encoding="utf-8") as archivo:
    datos_a = json.load(archivo)
    
with open("premier_league_2011_2020.json", "r", encoding="utf-8") as archivo:
    datos_b = json.load(archivo)
    
#print(datos_a)
#print(datos_b)

A = {registro["campeon"] for registro in datos_a} #CHAMPIONS
B = {registro["campeon"] for registro in datos_b} #PREMIER

U = A | B

print(A) #CHAMPIONS
print(B) #PREMIER
print(U) #TODOS

#2. Notación y Pertenencia
print('Chelsea' in A)
print('Barcelona' not in B)

#4. Conjunto vacio y universo
vacio = set()
print(len(vacio))
print(type(set()))
print(type({}))

#6. Subconjuntos y subconjuntos propios
C = {x for x in A if x == 'FC Barcelona' or x == 'Bayern Munich' or x == 'Real Madrid'} #Equipos no ingleses
print(C <= A)
print(C < A)
print(A < A)

#8. Cardinalidad de conjuntos finitos
print(len(A))
print(len(B))
print(len(A & B))

'''#10. Elementos hashables y conjuntos inmutables
D = frozenset(A)
B.add(D)
print(B)'''

#12. Itersección
print(A & B)
print(A.intersection(B))

#14. Diferencia simétrica
print(A ^ B)
#print(A.symmetric_difference(B))
print((A - B) | (B - A))

#16. Propiedades de las operaciones
C = {x for x in B if x == 'Manchester United' or x == 'Manchester City'} #Equipos de la ciudad de Manchester
print(C)

#Conmutatividad
assert (A | B) == (B | A)
#Asociatividad
assert ((A | B) | C) == (A | (B | C))
# Idempotencia
assert (A & A) == A
# Distributividad
assert (A & (B | C)) == ((A & B) | (A & C))