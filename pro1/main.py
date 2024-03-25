import numpy as np

states=["Paper", "Rock", "Scissors"]
transition_matrix_computer = {
    "Paper": {"Paper": 2/3, "Rock": 1/3, "Scissors": 0/3},
    "Rock": {"Paper": 0/3, "Rock": 2/3, "Scissors": 1/3},
    "Scissors": {"Paper": 2/3, "Rock": 0/3, "Scissors": 1/3}
}

def calc_stationary_vec():
    transition_matrix=transition_matrix_computer
    vector = [1 / 3, 1 / 3, 1 / 3]
    previous_meal = np.random.choice(states, p=vector)
    meal_counts = [0, 0, 0]
    for _ in range(10000):
        meal_counts = [0, 0, 0]
    for _ in range(10000):
        next_meal = np.random.choice(states, p=[transition_matrix[previous_meal][_] for _ in states])

        for __ in range(3):
            if next_meal == states[__]:
                meal_counts[__] += 1
                break
        previous_meal = next_meal
    probability_meal_counts = np.array(meal_counts) / sum(meal_counts)
    print("Prawdopodobieństwo wystąpienia poszczególnych posiłków =", probability_meal_counts)
    matrix_size = len(states)
    matrix = np.zeros((matrix_size, matrix_size))
    for i in range(matrix_size):
        for j in range(matrix_size):
            matrix[i, j] = transition_matrix[states[i]][states[j]]
    for _ in range(10):
        vector = np.dot(vector, matrix)
    print("Stacjonarny rozkład prawdopodobieństwa =", vector)
    eigenvalues, eigenvectors = np.linalg.eig(matrix.T)
    stationary_index = np.argmin(np.abs(eigenvalues - 1.0))
    stationary_vector = np.real(eigenvectors[:, stationary_index])
    stationary_vector /= stationary_vector.sum()
    print("stationary_vector (np.linalg.eig)=", stationary_vector)
    return stationary_vector

def comp_move(playerMove):
    odp = np.random.choice(states, p=list(transition_matrix_computer[playerMove].values()))
    return odp

def player_move(matrix):
    return np.random.choice(states, p=matrix)

def gameResults(player, computer):
    if (player == "Paper" and computer == "Rock") or \
       (player == "Scissors" and computer == "Paper") or \
       (player == "Rock" and computer == "Scissors"):
        print("Player wins")
    elif (player == "Paper" and computer == "Scissors") or \
         (player == "Scissors" and computer == "Rock") or \
         (player == "Rock" and computer == "Paper"):
        print("Player lose")
    else:
        print("Draw")

def PKNGame(num_rounds):
    compMove =  "Paper"
    oldplayermove = "Paper"
    for _ in range(num_rounds):
        playerMove = player_move(calc_stationary_vec())
        compMove = comp_move(oldplayermove)
        oldplayermove = playerMove
        gameResults(playerMove, compMove)

num_rounds = int(input("Podaj liczbę rund do zagrania: "))
PKNGame(num_rounds)
