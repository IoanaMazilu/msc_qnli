apples_premise = 5
apples_hypothesis = 2

# the hypothesis refers to the number of apples Billy has, which is also mentioned in the premise
if apples_hypothesis != apples_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples reported in the premise
    label = "contradiction"
else:
    # if the number of apples in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
