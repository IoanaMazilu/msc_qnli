average_rent_premise = 613
average_rent_hypothesis = 613

# the hypothesis mentions the average rent rate in Cincinnati, Ohio, which is also mentioned in the premise
if average_rent_hypothesis!= average_rent_premise:
    # check if the average rent rate in the hypothesis contradicts the average rent rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
