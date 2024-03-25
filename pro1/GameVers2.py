import random
import numpy as np
import matplotlib.pyplot as plt

class GameVers2:
    def __init__(self):
        self.learningRate = 0.01
        self.states = [0, 1, 2]
        self.computerMatrix = np.array([[2 / 3, 1 / 3, 0],  # papier
                                        [0, 2 / 3, 1 / 3],  # kamień
                                        [2 / 3, 0, 1 / 3]])  # nożyce

        self.playerMatrix = np.array([[1 / 3, 1 / 3, 1 / 3],
                                      [1 / 3, 1 / 3, 1 / 3],
                                      [1 / 3, 1 / 3, 1 / 3]])
        self.cash = 0
        self.cash_history = [self.cash]  # Inicjalizacja historii stanu gotówki

    def comp_move(self, previousPlayerMove):
        return np.random.choice(self.states, p=self.computerMatrix[previousPlayerMove])

    def first_move(self):
        return random.randint(0, 2)

    def player_move(self, previousComputerMove):
        return np.random.choice(self.states, p=self.playerMatrix[previousComputerMove])

    def update_weights(self, gameRes, playerMove, compPrevMove):
        if gameRes == 1:
            self.cash += 1
            self.playerMatrix[playerMove][compPrevMove] += self.playerMatrix[playerMove][compPrevMove] * self.learningRate
        elif gameRes == -1:
            self.cash -= 1
            self.playerMatrix[playerMove][compPrevMove] -= self.playerMatrix[playerMove][compPrevMove] * self.learningRate

        sum_vector = sum(self.playerMatrix[playerMove])
        self.playerMatrix[playerMove] = [element / sum_vector for element in self.playerMatrix[playerMove]]

    def compare_moves(self, playerMove, computerMove):
        if playerMove == 0 and computerMove == 1 or \
                playerMove == 1 and computerMove == 2 or \
                playerMove == 2 and computerMove == 0:
            print("WYGRANA")
            return 1
        elif playerMove == 0 and computerMove == 2 or \
                playerMove == 1 and computerMove == 0 or \
                playerMove == 2 and computerMove == 1:
            print("Przegrana")
            return -1
        else:
            print("remis")
            return 0

    def PKN_game(self, iteration):
        playerMove = self.first_move()
        computerMove = self.first_move()

        for _ in range(iteration):
            oldComputerMove = computerMove
            computerMove = self.comp_move(playerMove)
            playerMove = self.player_move(oldComputerMove)
            gameRes = self.compare_moves(playerMove, computerMove)
            self.update_weights(gameRes, playerMove, oldComputerMove)
            self.cash_history.append(self.cash)  # Dodaj stan gotówki do historii


if __name__ == '__main__':
    pkn = GameVers2()
    pkn.PKN_game(100000)
    print(pkn.playerMatrix)
    plt.plot(range(100001), pkn.cash_history)
    plt.xlabel('Numer Gry')
    plt.ylabel('Stan Gotówki')
    plt.title('Zmiana Stanu Gotówki w Grze "Kamień, Papier, Nożyce"')
    plt.show()
