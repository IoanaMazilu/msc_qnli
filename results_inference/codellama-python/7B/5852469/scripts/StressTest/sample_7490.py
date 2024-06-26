apples_premise = 360
apples_hypothesis = 360

# the hypothesis refers to the number of apples in the premise
if apples_hypothesis <= apples_premise:
    # check if the estimate of 'apples_hypothesis' contradicts the number of apples in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
