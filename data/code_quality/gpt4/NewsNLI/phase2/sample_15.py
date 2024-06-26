incidents_premise = 0.7
incidents_hypothesis = 0.7

# the hypothesis refers to the percentage of incidents that occurred in schools or businesses, which is also mentioned in the premise
if incidents_hypothesis != incidents_premise:
    # check if the percentage of incidents mentioned in the hypothesis contradicts the value reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)