initial_cards_mary = 33.0
torn_cards = 6.0
new_cards_mary = 23.0
total_cards_mary = initial_cards_mary + new_cards_mary

# the hypothesis refers to the total number of Mary's Pokemon cards, which is also mentioned in the premise
# compute the total number of Mary's Pokemon cards according to the premise
total_cards_mary_premise = initial_cards_mary + new_cards_mary
if total_cards_mary!= total_cards_mary_premise:
    # check if the total number of Mary's Pokemon cards in the hypothesis contradicts the total number of cards in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are the same, we can infer entailment
    label = "entailment"

print(label)
