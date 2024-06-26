baseball_cards_premise = 87.0
baseball_cards_hypothesis = 96.0

# the hypothesis refers to the number of baseball cards, which is also mentioned in the premise
# compute the total number of baseball cards in the premise
total_baseball_cards_premise = baseball_cards_premise + 13.0

# check if the number of baseball cards in the hypothesis contradicts the number of baseball cards from the premise
if baseball_cards_hypothesis!= total_baseball_cards_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
