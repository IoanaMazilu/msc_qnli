rent_premise = 613
rent_hypothesis = 613

# the hypothesis mentions the average rent rate in Cincinnati, Ohio, which is also mentioned in the premise
if rent_hypothesis!= rent_premise:
    # check if the average rent rate in the hypothesis contradicts the average rent rate reported in the premise
    label = "contradiction"
else:
    # if the average rent rate in the hypothesis does not contradict the average rent rate in the premise, we can infer entailment
    label = "entailment"

print(label)
