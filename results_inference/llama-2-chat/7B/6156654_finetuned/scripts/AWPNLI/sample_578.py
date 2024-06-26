cards_marcus_premise = 210.0
cards_given_premise = 58.0
new_cards_hypothesis = 268.0

# the hypothesis refers to the number of baseball cards Marcus has now, which is also mentioned in the premise
# compute the total number of cards Marcus has now, according to the premise
total_cards_marcus = cards_marcus_premise + cards_given_premise
if total_cards_marcus == new_cards_hypothesis:
    # if the total number of cards Marcus has now is equal to the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the total number of cards Marcus has now is not equal to the hypothesis, we can infer contradiction
    label = "contradiction"

print(label)
