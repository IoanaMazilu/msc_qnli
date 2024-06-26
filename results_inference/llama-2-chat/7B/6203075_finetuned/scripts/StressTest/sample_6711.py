balls_given_premise = 17
balls_given_hypothesis = 77

# the hypothesis refers to the number of balls given by Mike, which is also mentioned in the premise
if balls_given_hypothesis <= balls_given_premise:
    # check if the hypothesis value contradicts the number of balls given in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
