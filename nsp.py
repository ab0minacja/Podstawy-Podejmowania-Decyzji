import random
import math
import numpy as np
# Przykładowe dane wejściowe
nurses = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
preference_matrix = [[10, 5, 10, 7, 9, 11, 11, 11, 6, 8],[11, 12, 5, 10, 9, 12, 6, 8, 10],[9, 8, 8, 11, 5, 11, 12, 5, 11, 6],[7, 5, 8, 5, 11, 12, 5, 5, 11, 10],[10, 6, 6, 11, 7, 12, 10, 11, 5, 9],[7, 12, 10, 6, 10, 11, 7, 9, 10, 6],[5, 5, 6, 5, 9, 10, 6, 8, 8, 11]]
cost_matrix = [39,43,42,51,38, 50, 37, 40, 38,49]
temperature = 1000
cooling_rate = 1
iterations = 1000
#Losowanie pielegniarek które mają zmiane w danym dniu
elementy = []
selected_numbers =[]
def find_nurses(matrix):
    global elementy
    num_rows = 7
    num_cols = 9
    selected_numbers = []
    column_counts = [0] * num_cols

    for row in range(num_rows):
        found = False
        while not found:
            indices = list(np.random.choice(num_cols, 3, replace=False))
            if all(index < num_cols for index in indices):
                selected = matrix[row]
                selected = [selected[i] for i in indices]

                if np.sum(selected) == 24:
                    selected_numbers.append(indices)
                    found = True

    for row in range(num_rows):
        found = False
        while not found:
            hours_l = []
            for i in range(6):
                for j in range(2):
                    index = selected_numbers[i][j]
                    hours = preference_matrix[i][index]
                    hours_l.append(hours)

                if np.sum(hours_l) <= 40:
                    found = True
        print(selected_numbers)
        # Sprawdź liczbę wybranych wartości w każdej kolumnie
        for j in range(0,2):
            if column_counts[j] >= 5:
                continue
            index = selected_numbers[row][j]
            column_counts[j] += 1

    print(selected_numbers)
    return selected_numbers
# Funkcja obliczająca koszt zmiany dla danego harmonogramu
def calculate_cost(schedule):
    schedule = schedule
    cost = 0
    for schedule in schedule:
        list = schedule
        for p,j in zip(range(6),range(len(list))):
                index = schedule[j]
                print(preference_matrix[p][index]*cost_matrix[index])
                cost += preference_matrix[p][index]*cost_matrix[index]
    return cost
# Implementacja metody wyżarzania
def simulated_annealing(matrix):
    current_schedule = find_nurses(matrix)
    current_cost = calculate_cost(current_schedule)
    best_schedule = current_schedule.copy()
    best_cost = current_cost
    global temperature
    while temperature > 0:
        for _ in range(iterations):
            # Generowanie nowego losowego harmonogramu
            new_schedule = find_nurses(matrix)
            new_cost = calculate_cost(new_schedule)

            # Obliczanie różnicy kosztu między obecnym a nowym harmonogramem
            cost_diff = new_cost - current_cost

            # Akceptowanie nowego harmonogramu z pewnym prawdopodobieństwem
            if cost_diff < 0 or random.random() < math.exp(-cost_diff / temperature):
                current_schedule = new_schedule
                current_cost = new_cost

            # Aktualizacja najlepszego harmonogramu
            if current_cost < best_cost:
                best_schedule = current_schedule.copy()
                best_cost = current_cost

        # Obniżanie temperatury
        temperature *= 1 - cooling_rate

    return best_schedule, best_cost

# Wywołanie funkcji rozwiązującej problem harmonogramowania
min_cost = []
for i in range(25):
    best_schedule, best_cost = simulated_annealing(preference_matrix)
    min_cost.append(best_cost)
    print("Najlepszy harmonogram:", best_schedule)
    print("Najniższy koszt:", best_cost)
print("Najniższy koszt po 25 iteracjach  " + str(np.mean(min_cost)))
