stations_premise = 18
stations_hypothesis = 48

# the hypothesis refers to the number of stations between Hyderabad and Bangalore mentioned in the premise
if stations_premise >= stations_hypothesis:
    # check if the number of stations in the premise contradicts the estimate of less than'stations_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
