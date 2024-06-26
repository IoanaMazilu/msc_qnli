cards_given_premise = 5
cards_given_hypothesis = 5

# the hypothesis refers to the number of baseball cards given to John mentioned in the premise
if cards_given_hypothesis >= cards_given_premise:
    # check if the hypothesis value contradicts the exact number of cards given in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
