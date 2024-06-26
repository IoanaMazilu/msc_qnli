trapped_people_premise_min = 20
trapped_people_premise_max = 30
trapped_people_hypothesis = 30

# the hypothesis mentions the maximum number of people thought trapped in the casino, which is also mentioned in the premise
if trapped_people_hypothesis > trapped_people_premise_max:
    # check if the maximum number of people in the hypothesis contradicts the maximum number of people reported in the premise
    label = "contradiction"
elif trapped_people_hypothesis < trapped_people_premise_min:
    # check if the maximum number of people in the hypothesis contradicts the minimum number of people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
