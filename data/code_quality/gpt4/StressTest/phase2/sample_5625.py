cards_deck_premise = 52
cards_deck_hypothesis = 72
spade_cards_select = 13
heart_cards_select = 13

# the hypothesis refers to the number of cards in a deck and the number of ways to select certain cards, which are also mentioned in the premise
if cards_deck_hypothesis <= cards_deck_premise:
    # check if the hypothesis value contradicts the number of cards in the premise
    label = "contradiction"
elif spade_cards_select != 13 or heart_cards_select != 13:
    # checking if the number of selected cards in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
