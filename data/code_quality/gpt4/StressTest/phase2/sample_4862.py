albert_mary_ratio_premise = 2
albert_mary_ratio_hypothesis = 2
albert_betty_ratio_premise = 4
albert_betty_ratio_hypothesis = 4

# the hypothesis refers to the age ratios between Albert, Mary and Betty, mentioned in the premise
if albert_mary_ratio_hypothesis >= albert_mary_ratio_premise:
    # check if the hypothesis ratio contradicts the Albert-Mary age ratio in the premise
    label = "contradiction"
elif albert_betty_ratio_hypothesis != albert_betty_ratio_premise:
    # check if the Albert-Betty age ratio in the hypothesis contradicts the same ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
