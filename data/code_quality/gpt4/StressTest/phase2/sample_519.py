stations_premise = 18
stations_hypothesis = 58

# the hypothesis refers to the number of stations between Hyderabad and Bangalore mentioned in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the exact number of stations in the premise
    label = "contradiction"
elif stations_premise >= stations_hypothesis:
    # check if the exact number of stations in the premise contradicts the estimate of less than 'stations_hypothesis' in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
