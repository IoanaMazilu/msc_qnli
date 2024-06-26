suspects_arrested_premise = 3
suspects_arrested_hypothesis = 3

# the hypothesis mentions the number of suspects arrested, which is also mentioned in the premise
if suspects_arrested_hypothesis != suspects_arrested_premise:
    # check if the number of suspects arrested in the hypothesis contradicts the number of suspects arrested in the premise
    label = "contradiction"
else:
    # if the number of suspects arrested in the hypothesis does not contradict the number of suspects arrested in the premise, we can infer entailment
    label = "entailment"

print(label)
