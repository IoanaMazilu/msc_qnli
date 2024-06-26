baseball_cards_premise = 6
baseball_cards_hypothesis = 5

# the hypothesis refers to the number of baseball cards you gave to John, mentioned in the premise
if baseball_cards_hypothesis == baseball_cards_premise:
    # check if the exact number of baseball cards in the hypothesis is the same as in the premise
    label = "entailment"
elif baseball_cards_hypothesis > baseball_cards_premise:
    # check if the number of baseball cards in the hypothesis contradicts the exact number mentioned in the premise
    label = "contradiction"
else:
    # if the number of baseball cards in the hypothesis is less than in the premise, it doesn't contradict nor can it be explicitly entailed from the premise
    label = "neutral"

print(label)
