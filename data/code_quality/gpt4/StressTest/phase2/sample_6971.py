stations_premise = 8
stations_hypothesis = 2

# the hypothesis refers to the number of stations between Vijayawada and Chennai mentioned in the premise
if stations_premise != stations_hypothesis:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
