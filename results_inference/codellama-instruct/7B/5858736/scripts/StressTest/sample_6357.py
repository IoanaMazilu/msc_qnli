baseball_cards_premise = 5
baseball_cards_hypothesis = 2

if baseball_cards_hypothesis <= baseball_cards_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
