money_given_premise = 95
money_given_hypothesis = 55

# the hypothesis refers to the amount of money given to John mentioned in the premise
if money_given_hypothesis!= money_given_premise:
    # check if the amount of money given in the hypothesis contradicts the amount of money given in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
