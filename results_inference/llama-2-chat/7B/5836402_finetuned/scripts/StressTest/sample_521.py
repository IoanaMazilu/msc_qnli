stations_premise = 18
stations_hypothesis = 18

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, which is also mentioned in the premise
if stations_hypothesis <= stations_premise:
    # check if the hypothesis value contradicts the estimate of more than'stations_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)