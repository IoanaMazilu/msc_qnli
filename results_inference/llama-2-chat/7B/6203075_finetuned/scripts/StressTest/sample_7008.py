males_premise = 25
males_hypothesis = 45

# the hypothesis refers to the number of males mentioned in the premise
if males_hypothesis <= males_premise:
    # check if the hypothesis value contradicts the number of males in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
