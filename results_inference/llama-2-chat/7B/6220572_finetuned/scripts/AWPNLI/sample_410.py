cards_premise = 9.0
cards_given_premise = 4.0
cards_hypothesis = 5.0

# the hypothesis refers to the number of Pokemon cards, which are also mentioned in the premise
# compute the number of Pokemon cards left with Jason from the premise
cards_left_premise = cards_premise - cards_given_premise
if cards_hypothesis!= cards_left_premise:
    # check if the number of Pokemon cards in the hypothesis contradicts the number of cards left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
