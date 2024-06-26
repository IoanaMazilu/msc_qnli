baseball_cards_premise = 3
baseball_cards_hypothesis = 3

# the hypothesis refers to the number of baseball cards given to John, as mentioned in the premise
if baseball_cards_hypothesis != baseball_cards_premise:
    # check if the number of baseball cards in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the number of baseball cards in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
