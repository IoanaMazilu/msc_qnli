mary_cards_premise = 33.0
torn_cards_premise = 6.0
new_cards_given_premise = 23.0
mary_cards_hypothesis = 56.0

# the hypothesis refers to the number of Mary's Pokemon cards, which are also mentioned in the premise
# compute the total number of Mary's cards in the premise
mary_cards_total = mary_cards_premise + new_cards_given_premise

# check if the number of Mary's cards in the hypothesis contradicts the number of Mary's cards in the premise
if mary_cards_hypothesis!= mary_cards_total:
    label = "contradiction"
else:
    label = "entailment"

print(label)
