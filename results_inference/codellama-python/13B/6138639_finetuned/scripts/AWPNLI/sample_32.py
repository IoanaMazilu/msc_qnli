jason_cards_premise = 676.0
alyssa_cards_premise = 224.0
jason_cards_hypothesis = 452.0

# the hypothesis refers to the number of Pokemon cards Jason has, which is also mentioned in the premise
# compute the number of Pokemon cards Jason has after Alyssa bought some of his cards
jason_cards_after_alyssa_premise = jason_cards_premise - alyssa_cards_premise
if jason_cards_hypothesis!= jason_cards_after_alyssa_premise:
    # check if the number of Pokemon cards in the hypothesis contradicts the number of Pokemon cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
