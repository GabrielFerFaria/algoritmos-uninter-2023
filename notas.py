notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
notas_ordenadas = sorted(notas)
print(notas.count(7))
notas[-1] = 4
print(notas)

print(max(notas))

print(notas_ordenadas)

media_notas = sum(notas)/len(notas)
print(f'Média das notas é {media_notas:.2f}')