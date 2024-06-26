cards_premise = 5
cards_hypothesis = 4

# the hypothesis refers to the total number of cards mentioned in the premise
if cards_premise != cards_hypothesis:
    # check if the number of cards in the hypothesis contradicts the number of cards reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
