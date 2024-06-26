baseball_cards_premise = 5
baseball_cards_hypothesis = 5

# the hypothesis refers to the number of baseball cards given to John mentioned in the premise
if baseball_cards_hypothesis >= baseball_cards_premise:
    # check if the estimate of 'baseball_cards_hypothesis' contradicts the number of baseball cards in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
