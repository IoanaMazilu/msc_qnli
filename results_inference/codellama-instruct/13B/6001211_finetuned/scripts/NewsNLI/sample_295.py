average_rent_premise = 613
average_rent_hypothesis = 613

# the hypothesis mentions the average rent in Cincinnati, Ohio, which is also mentioned in the premise
if average_rent_hypothesis!= average_rent_premise:
    # check if the average rent in the hypothesis contradicts the average rent reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
