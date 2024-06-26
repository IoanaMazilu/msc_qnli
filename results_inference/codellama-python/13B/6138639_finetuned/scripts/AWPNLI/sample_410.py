initial_cards_premise = 9.0
given_cards_premise = 4.0
current_cards_hypothesis = 5.0

# the hypothesis refers to the number of Pokemon cards, which are also mentioned in the premise
# compute the current number of cards in the premise
current_cards_premise = initial_cards_premise - given_cards_premise
if current_cards_hypothesis!= current_cards_premise:
    # check if the number of cards in the hypothesis contradicts the number of cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
