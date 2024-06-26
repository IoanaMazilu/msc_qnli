value_premise = 1000000
value_hypothesis = 1000000

# the hypothesis mentions the value of the stolen vehicles, which is also referenced in the premise
if value_hypothesis!= value_premise:
    # check if the value in the hypothesis contradicts the value reported in the premise
    label = "contradiction"
else:
    # if the value in the hypothesis does not contradict the value in the premise, we can infer entailment
    label = "entailment"

print(label)
