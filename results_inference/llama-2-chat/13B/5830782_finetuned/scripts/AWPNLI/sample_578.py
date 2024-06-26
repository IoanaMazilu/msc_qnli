cards_initial_premise = 210.0
cards_received_premise = 58.0
cards_hypothesis = 268.0

# the hypothesis refers to the number of cards, which are also mentioned in the premise
# compute the total number of cards in the premise
total_cards_premise = cards_initial_premise + cards_received_premise
if cards_hypothesis!= total_cards_premise:
    # check if the number of cards in the hypothesis contradicts the number of cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
