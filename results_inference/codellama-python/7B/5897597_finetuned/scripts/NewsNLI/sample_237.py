injured_people_premise = 50
injured_people_hypothesis = 50

# the hypothesis mentions the number of injured people, which is also referenced in the premise
if injured_people_hypothesis < injured_people_premise:
    # check if the number of injured people in the hypothesis is less than the number of injured people reported in the premise
    label = "contradiction"
else:
    # if the number of injured people in the hypothesis does not contradict the number of injured people in the premise, we can infer entailment
    label = "entailment"

print(label)
