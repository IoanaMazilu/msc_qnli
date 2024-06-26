interest_premise = 0.87
interest_hypothesis = 0.87

# the hypothesis mentions the percentage of Americans interested in their family background, which is also mentioned in the premise
if interest_hypothesis != interest_premise:
    # check if the percentage of interest in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the percentage of interest in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
