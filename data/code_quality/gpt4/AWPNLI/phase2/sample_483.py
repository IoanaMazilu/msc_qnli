initial_cards_premise = 33.0
torn_cards_premise = 6.0
given_cards_premise = 23.0
remaining_cards_hypothesis = 5.0

# the hypothesis refers to the number of remaining Pokemon cards Mary has, which can be computed from the premise
# compute the remaining cards in the premise
remaining_cards_premise = initial_cards_premise - torn_cards_premise - given_cards_premise
if remaining_cards_hypothesis != remaining_cards_premise:
    # check if the number of remaining cards in the hypothesis contradicts the computed remaining cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
