street_kids_premise = 12000
street_kids_hypothesis = 12000

# the hypothesis mentions the number of street kids in Jakarta, which is also referenced in the premise
if street_kids_hypothesis!= street_kids_premise:
    # check if the number of street kids in the hypothesis contradicts the number of street kids reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
