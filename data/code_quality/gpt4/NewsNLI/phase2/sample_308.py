street_kids_premise = 12000
street_kids_hypothesis = 12000

# the hypothesis mentions the estimate of street kids living in Jakarta, which is also mentioned in the premise
if street_kids_hypothesis != street_kids_premise:
    # check if the number of street kids in the hypothesis contradicts the number of street kids reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
