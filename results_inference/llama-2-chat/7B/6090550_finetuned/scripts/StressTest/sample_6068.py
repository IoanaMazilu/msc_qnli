ys_premise = 4
ys_hypothesis = 4

# the hypothesis refers to the number of shops in the town mentioned in the premise
if ys_hypothesis >= ys_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ys_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
