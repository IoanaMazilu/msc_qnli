murders_premise = 19
murders_hypothesis = 19

# the hypothesis mentions the number of murders Bulger is accused of, which is also mentioned in the premise
if murders_hypothesis != murders_premise:
    # check if the number of murders in the hypothesis contradicts the number of murders reported in the premise
    label = "contradiction"
else:
    # if the number of murders in the hypothesis does not contradict the number of murders in the premise, we can infer entailment
    label = "entailment"

print(label)
