injured_people_premise = 20
injured_people_hypothesis = 20

# the hypothesis mentions the number of injured people, which is also referenced in the premise
if injured_people_hypothesis != injured_people_premise:
    # check if the number of injured people in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
