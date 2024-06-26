stations_premise = 28
stations_hypothesis = 18

# the hypothesis refers to the number of stations between Hyderabad and Bangalore, referenced also in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the estimate of'stations_premise'
    label = "contradiction"
elif stations_premise!= stations_hypothesis:
    # check if the number of stations in the hypothesis contradicts the number of stations reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)