import math
import random

startingRate = 1.6
currentRate = [1.6, 1.6, 1.6]
bets = [[[0, 1.6]], [[0, 1.6]]]
options = [["option0", 0], ["option1", 0]]

startingValue = 30
if len(bets) == 2:
    startingValue = 250
elif len(bets) == 3:
    startingValue = 150
elif len(bets) == 4:
    startingValue = 80
elif len(bets) == 5:
    startingValue = 50
else:
    startingValue = 30
for bet in bets:
    bet[0][0] = startingValue

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
        newRate = min(
            math.sqrt(max((data[0] - data[1]), 0) / 300) * len(bets) / 2 + 1,
            math.sqrt(max((data[0] - data[1]), 0) ** 3) / 2000 * len(bets) / 2 + 1
        )
        newRates.append(newRate)
        print(f"rate for option {i}: {newRate}")
        truePL = data[0] - data[1] + bets[i][0][0] * (bets[i][0][1] - 1)
        for bet in bets:
            if bet is not bets[i]:
                truePL -= bet[0][0]
        print(f"p&l for option {i}: {truePL}")
    currentRate = newRates
    for bet in bets:
        bet[0][0] = max(bet[0][0] - volume/3, 0)


for j in range(1):
    totalBet = 0
    for i in range(20):
        print(f"{i}:")

        rand = random.randint(0, len(bets) - 1)

        print(rand)
        rand2 = random.randint(0, 10) * random.randint(0, 10) + 10
        print(rand2)
        newBet(rand2, rand)

        totalBet += rand2

    print("\n--- Final Profit Analysis ---")
    print("Total Bet: ", totalBet)
    for win_option in range(len(options)):
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
        print(bets)
    startingRate = 1.6
    currentRate = [1.6, 1.6, 1.6]
    bets = [[[80, 1.6]], [[80, 1.6]], [[80, 1.6]], [[80, 1.6]]]
    options = [["option0", 0], ["option1", 0]]