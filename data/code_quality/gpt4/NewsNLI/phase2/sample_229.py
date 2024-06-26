people_wounded_premise = 1000
people_wounded_hypothesis = 1000
people_killed_premise = 1 + 5
people_killed_hypothesis = 6

# the hypothesis mentions the number of people wounded and killed in the demonstrations, which are also mentioned in the premise
if people_wounded_hypothesis != people_wounded_premise:
    # check if the number of wounded people in the hypothesis contradicts the number of wounded people reported in the premise
    label = "contradiction"
elif people_killed_hypothesis != people_killed_premise:
    # check if the number of killed people from the hypothesis contradicts the number of killed people in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
