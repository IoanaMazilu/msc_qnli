initial_cards_jason_premise = 676.0
bought_cards_alyssa_premise = 224.0
remaining_cards_jason_hypothesis = 452.0

# the hypothesis refers to the number of cards Jason has now, which is also mentioned in the premise
# compute the remaining number of cards Jason has in the premise
remaining_cards_jason_premise = initial_cards_jason_premise - bought_cards_alyssa_premise
if remaining_cards_jason_hypothesis!= remaining_cards_jason_premise:
    # check if the number of remaining cards in the hypothesis contradicts the number of remaining cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
