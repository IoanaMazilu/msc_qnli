ratio_premise = 8/9
ratio_hypothesis = 7/9

# the hypothesis refers to the ratio of ages mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the 'ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
