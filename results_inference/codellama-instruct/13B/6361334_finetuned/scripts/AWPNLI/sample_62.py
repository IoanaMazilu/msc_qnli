baseball_cards_sally_premise = 39.0
baseball_cards_torn_premise = 9.0
baseball_cards_sara_bought_premise = 24.0
baseball_cards_sally_hypothesis = 15.0

# the hypothesis refers to the number of baseball cards, which are also mentioned in the premise
# compute the total number of baseball cards in the premise
total_baseball_cards_premise = baseball_cards_sally_premise - baseball_cards_torn_premise + baseball_cards_sara_bought_premise
if total_baseball_cards_hypothesis!= total_baseball_cards_premise:
    # check if the number of baseball cards in the hypothesis contradicts the number of baseball cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
