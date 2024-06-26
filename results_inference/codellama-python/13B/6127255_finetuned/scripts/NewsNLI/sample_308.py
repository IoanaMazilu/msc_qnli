street_kids_premise = 12000
street_kids_hypothesis = 12000

# the hypothesis mentions the number of street kids in Jakarta, which is also mentioned in the premise
if street_kids_hypothesis!= street_kids_premise:
    # check if the number of street kids in the hypothesis contradicts the number of street kids reported in the premise
    label = "contradiction"
else:
    # if the number of street kids in the hypothesis does not contradict the number of street kids in the premise, we can infer entailment
    label = "entailment"

print(label)
