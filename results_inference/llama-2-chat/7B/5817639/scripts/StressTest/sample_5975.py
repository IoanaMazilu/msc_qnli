miles_premise = 8
miles_hypothesis = 6
speed_premise = 40
speed_hypothesis = 60
stopped_premise = 11
stopped_hypothesis = 11

# the hypothesis talks about the distance and speed traveled by Jerry, referenced also in the premise
if miles_hypothesis <= miles_premise:
    # check if the hypothesis value contradicts the estimate of'miles_premise'
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the hypothesis speed contradicts the estimate of'speed_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
