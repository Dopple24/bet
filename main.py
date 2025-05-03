import math
import random

startingRate = 1.6
currentRate = [1.6, 1.6]
bets = [[[300, 1.6]], [[300, 1.6]]]
options = [["option0", 0], ["option1", 0]]

def getData(betID):
    losses = 0
    winnings = 0
    for los in bets[betID]:
        losses += los[0] * (los[1] - 1)
    for i in range(len(bets)):
        if i is not betID:
            for bet in bets[i]:
                winnings += bet[0]
    #print(round(winnings - losses, 2))
    #print(bets[betID])
    return [winnings, losses]

def newBet(volume, betID):
    global currentRate
    bets[betID].append([volume, round(currentRate[betID],2)])
    newRates = []
    for i in range(len(bets)):
        data = getData(i)
        newRate = math.sqrt(max(((data[0] - data[1])),0)/300) + 1
        newRates.append(newRate)
        #print(newRate)
    currentRate = newRates


for j in range(100):
    totalBet = 0
    for i in range(20):
        #print(f"{i}:")
        rand = random.randint(0, 1)
        #print(rand)
        rand2 = random.randint(10, 100)
        newBet(rand2, rand)

        totalBet += rand2

    print("\n--- Final Profit Analysis ---")
    print("Total Bet: ", totalBet)
    for win_option in range(2):
        winnings = 0
        losses = 0
        # Skip the first placeholder bet
        for i in range(len(bets)):
            for idx, bet in enumerate(bets[i]):
                if idx == 0:
                    continue  # skip initial placeholder
                amount, rate = bet
                if i == win_option:
                    winnings += amount
                else:
                    losses += amount * (rate-1)
        net_profit = round(winnings - losses, 2)
        print(f"If Option {win_option} wins: Profit = {net_profit}")
    startingRate = 1.6
    currentRate = [1.6, 1.6]
    bets = [[[300, 1.6]], [[300, 1.6]]]
    options = [["option0", 0], ["option1", 0]]