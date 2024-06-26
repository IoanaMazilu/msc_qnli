jason_cards_premise = 676.0
alyssa_cards_premise = 224.0
jason_cards_hypothesis = 898.0

# the hypothesis refers to the total number of Pokemon cards that Jason has, which are also mentioned in the premise
# compute the total number of Pokemon cards in the premise
total_cards_premise = jason_cards_premise + alyssa_cards_premise
if jason_cards_hypothesis!= total_cards_premise:
    # check if the number of Pokemon cards in the hypothesis contradicts the number of Pokemon cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
