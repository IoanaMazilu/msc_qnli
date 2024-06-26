dollars_premise = 1803
dollars_hypothesis = 1803

# the hypothesis refers to the amount of money Mary has, which is also mentioned in the premise
if dollars_hypothesis >= dollars_premise:
    # check if the statement in the hypothesis contradicts the amount of money reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
