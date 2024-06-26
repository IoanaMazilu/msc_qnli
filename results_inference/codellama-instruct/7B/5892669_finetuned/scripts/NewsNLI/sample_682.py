ships_premise = 6
planes_premise = 3
ships_hypothesis = 6
planes_hypothesis = 3

# the hypothesis mentions the number of ships and planes involved in a search, which is also mentioned in the premise
if ships_hypothesis!= ships_premise:
    # check if the number of ships in the hypothesis contradicts the number of ships reported in the premise
    label = "contradiction"
elif planes_hypothesis!= planes_premise:
    # check if the number of planes from the hypothesis contradicts the number of planes in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
