total_premise = 6600
total_hypothesis = 6600

# the hypothesis refers to the total amount mentioned in the premise
if total_hypothesis >= total_premise:
    # check if the estimate of 'total_hypothesis' contradicts the total amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
