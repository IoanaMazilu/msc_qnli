cards_deck_premise = 52
cards_deck_hypothesis = 72

# the hypothesis refers to the number of cards in a deck, mentioned in the premise
if cards_deck_hypothesis != cards_deck_premise:
    # check if the number of cards in the hypothesis contradicts the number of cards mentioned in the premise
    label = "contradiction"
else:
    # if the number of cards in the hypothesis does not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
