stations_premise = 18
stations_hypothesis = 18

# the hypothesis refers to the number of stations between Hyderabad and Bangalore mentioned in the premise
if stations_hypothesis <= stations_premise:
    # check if the estimate of'stations_hypothesis' contradicts the number of stations in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
