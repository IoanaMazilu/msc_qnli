cards_premise = 9.0
gave_cards_premise = 4.0
cards_hypothesis = 5.0

# the hypothesis refers to the number of Pokemon cards, which are also mentioned in the premise
# compute the total number of cards in the premise
total_cards_premise = cards_premise - gave_cards_premise
if total_cards_hypothesis!= total_cards_premise:
    # check if the number of cards in the hypothesis contradicts the number of cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
