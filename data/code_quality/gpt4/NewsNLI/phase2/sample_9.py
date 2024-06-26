suspects_premise = 8
suspects_hypothesis = 8

# the hypothesis mentions the number of suspects arrested, which is also mentioned in the premise
if suspects_hypothesis != suspects_premise:
    # check if the number of suspects in the hypothesis contradicts the number of suspects in the premise
    label = "contradiction"
else:
    # if the number of suspects from the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
