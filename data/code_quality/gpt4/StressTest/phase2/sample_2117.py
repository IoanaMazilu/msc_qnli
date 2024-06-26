cards_given_premise = 4
cards_given_hypothesis = 4

# the hypothesis refers to the number of cards given to John mentioned in the premise
if cards_given_hypothesis >= cards_given_premise:
    # check if the estimate of 'cards_given_hypothesis' contradicts the number of cards given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
