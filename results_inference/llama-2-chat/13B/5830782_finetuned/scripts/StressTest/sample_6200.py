stations_premise = 18
stations_hypothesis = 88

# the hypothesis refers to the number of stations between two cities mentioned in the premise
if stations_hypothesis!= stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
