stations_premise = 18
stations_hypothesis = 58

# the hypothesis refers to the number of stations between Hyderabad and Bangalore mentioned in the premise
if stations_premise >= stations_hypothesis:
    # check if the estimate of'stations_premise' contradicts the number of stations in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
