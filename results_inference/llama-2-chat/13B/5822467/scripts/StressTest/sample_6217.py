stations_premise = 85
stations_hypothesis = 25

# the hypothesis refers to the number of stations between Delhi and Chennai mentioned in the premise
if stations_premise > stations_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'less than 85 stations' in the premise
    label = "contradiction"
elif stations_hypothesis!= stations_premise:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
