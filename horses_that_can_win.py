import csv
from random import choice
from string import ascii_letters

from functools import reduce

def points_analise(points):
    for point in points:
        if int(point) < 4 or int(point) > 10:
            return False
    return True

def probability_analysis():
    with open('horses.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(['cavalo', 'provavel'])
        horses = {}

        racing = int(input('Corridas: '))
        for i in range(7):
            while True:
                horse = str(input(f'Insira o cavalo {i + 1} e seus pontos: '))
                horse = horse.split(' ')
                name = horse[0]
                points = horse[1:]
                if len(points) > racing or len(points) < racing:
                    print('Erro: O número inserido de corridas está diferente do especificado anteriormente.')
                else:
                    if points_analise(points):
                        sum_points = reduce(lambda x, y: int(x) + int(y), points)
                        horses[f'{choice(ascii_letters)}{choice(ascii_letters)}{choice(ascii_letters)}{name}'] = int(sum_points), int(points[-1])
                        break
                    else:
                        print('Erro: O valor de pontos incorretos.')
        value_max = max(horses.values())
        print(value_max)

        for horse in horses:
            if horses[horse][0] + 10 > value_max[0] + 4:
                writer.writerow([horse[3:], 'sim'])
            elif horses[horse][0] + 10 == value_max[0] + 4:
                if horses[horse][1] > value_max[1]:
                    writer.writerow([horse[3:], 'sim'])
                else:
                    writer.writerow([horse[3:], 'não'])
            else:
                writer.writerow([horse[3:], 'não'])


probability_analysis()