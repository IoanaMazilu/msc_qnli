stations_premise = 8
stations_hypothesis = 2

# the hypothesis refers to the number of stations between Vijayawada and Chennai mentioned in the premise
if stations_hypothesis!= stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # if the number of stations in the hypothesis does not contradict the number of stations in the premise, we can infer entailment
    label = "entailment"

print(label)
