footballers_premise = 20
footballers_hypothesis = 20

# the hypothesis mentions the number of highest paid footballers according to Forbes, which is also mentioned in the premise
if footballers_hypothesis != footballers_premise:
    # check if the number of footballers in the hypothesis contradicts the number of footballers in the premise
    label = "contradiction"
else:
    # if the number of footballers in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
