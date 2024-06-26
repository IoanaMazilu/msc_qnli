stations_premise = 25
stations_hypothesis = 55

# the hypothesis refers to the number of stations between Delhi and Chennai mentioned in the premise
if stations_hypothesis!= stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
