joining_time_premise = 2
joining_time_hypothesis = 8

# the hypothesis refers to the time when Jose joined, which is also mentioned in the premise
if joining_time_hypothesis < joining_time_premise:
    # check if the 'joining_time_hypothesis' contradicts the joining time in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
