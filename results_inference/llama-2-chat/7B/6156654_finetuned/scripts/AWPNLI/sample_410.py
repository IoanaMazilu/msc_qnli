jason_cards_premise = 9.0
given_cards_premise = 4.0
jason_cards_hypothesis = 5.0

# the hypothesis refers to the number of cards Jason has, which is also mentioned in the premise
if jason_cards_hypothesis!= jason_cards_premise:
    # check if the number of cards in the hypothesis contradicts the number of cards in the premise
    label = "contradiction"
elif given_cards_premise!= jason_cards_hypothesis:
    # check if the number of cards given to friends in the hypothesis contradicts the number of cards given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
