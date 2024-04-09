suspects_premise = 3
suspects_hypothesis = 3

# the hypothesis mentions the number of suspects, which is also mentioned in the premise
if suspects_hypothesis!= suspects_premise:
    # check if the number of suspects in the hypothesis contradicts the number of suspects reported in the premise
    label = "contradiction"
else:
    # if the number of suspects in the hypothesis does not contradict the number of suspects in the premise, we can infer entailment
    label = "entailment"

print(label)
