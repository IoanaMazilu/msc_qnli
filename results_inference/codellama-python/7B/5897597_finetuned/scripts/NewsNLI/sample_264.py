people_in_peril_premise = 1000000
people_in_peril_hypothesis = 1000000

# the hypothesis mentions the number of people in peril, which is also referenced in the premise
if people_in_peril_hypothesis!= people_in_peril_premise:
    # check if the number of people in peril in the hypothesis contradicts the number of people in peril reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
