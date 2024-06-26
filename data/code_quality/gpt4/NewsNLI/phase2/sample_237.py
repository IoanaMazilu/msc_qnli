people_injured_premise = 50
people_injured_hypothesis = 50

# the hypothesis mentions the number of injured people, which is also mentioned in the premise
if people_injured_hypothesis != people_injured_premise:
    # check if the number of injured people in the hypothesis contradicts the number of injured people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
