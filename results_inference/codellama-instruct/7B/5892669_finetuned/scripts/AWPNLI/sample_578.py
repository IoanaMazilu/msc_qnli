initial_cards_premise = 210.0
received_cards_premise = 58.0
total_cards_hypothesis = 268.0

# the hypothesis refers to the total number of baseball cards, which are also mentioned in the premise
# compute the total number of baseball cards in the premise
total_cards_premise = initial_cards_premise + received_cards_premise
if total_cards_hypothesis!= total_cards_premise:
    # check if the total number of baseball cards in the hypothesis contradicts the total number of baseball cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
