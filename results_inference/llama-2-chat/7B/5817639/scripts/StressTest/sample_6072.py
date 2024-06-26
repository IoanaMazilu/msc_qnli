travel_premise = 8
travel_hypothesis = 7
speed_premise = 40
speed_hypothesis = 60
stop_premise = 15
stop_hypothesis = 15

# the hypothesis talks about the distance traveled, speed, and stops, referenced also in the premise
if travel_hypothesis <= travel_premise:
    # check if the hypothesis value contradicts the estimate of more than 'travel_premise'
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the hypothesis speed value contradicts the estimate of'speed_premise'
    label = "contradiction"
elif stop_hypothesis!= stop_premise:
    # check if the hypothesis stop value contradicts the estimate of'stop_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
