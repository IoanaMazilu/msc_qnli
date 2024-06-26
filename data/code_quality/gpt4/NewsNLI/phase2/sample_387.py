injured_people_premise = 30
injured_people_hypothesis = 30

# the hypothesis mentions the number of injured people, which is also referenced in the premise
if injured_people_hypothesis != injured_people_premise:
    # check if the number of injured people from the hypothesis contradicts the number of injured people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
