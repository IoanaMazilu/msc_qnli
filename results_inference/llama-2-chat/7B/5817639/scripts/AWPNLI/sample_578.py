baseball_cards_premise = 210.0
baseball_cards_hypothesis = 268.0

# check if the number of baseball cards in the hypothesis contradicts the number of cards from the premise
if baseball_cards_hypothesis > baseball_cards_premise:
    label = "contradiction"
elif baseball_cards_hypothesis - baseball_cards_premise == 58.0:
    # check if the number of cards given by Carter contradicts the estimate of more than 58 cards
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
