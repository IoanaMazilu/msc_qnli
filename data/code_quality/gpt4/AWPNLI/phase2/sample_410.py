initial_cards_premise = 9.0
given_cards_premise = 4.0
total_cards_hypothesis = 5.0

# the hypothesis refers to the number of Pokemon cards, which is also mentioned in the premise
# compute the remaining number of Pokemon cards in the premise
remaining_cards_premise = initial_cards_premise - given_cards_premise
if total_cards_hypothesis != remaining_cards_premise:
    # check if the number of Pokemon cards in the hypothesis contradicts the number of Pokemon cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
