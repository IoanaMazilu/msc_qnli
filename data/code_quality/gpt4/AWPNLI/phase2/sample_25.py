initial_cards_mike_premise = 87.0
bought_cards_sam_premise = 13.0
current_cards_mike_hypothesis = 72.0

# the hypothesis refers to the current number of cards Mike has, which is also mentioned in the premise
# compute the current number of cards Mike has in the premise
current_cards_mike_premise = initial_cards_mike_premise - bought_cards_sam_premise
if current_cards_mike_hypothesis != current_cards_mike_premise:
    # check if the number of cards in the hypothesis contradicts the number of cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
