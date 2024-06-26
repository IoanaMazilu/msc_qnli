miles_per_hour_premise = 3
miles_per_hour_hypothesis = 7

# the hypothesis refers to the speed at which Aaron will jog and walk back home, as estimated in the premise
if miles_per_hour_premise <= miles_per_hour_hypothesis:
    # check if the estimate of'miles_per_hour_hypothesis' contradicts the speed reported in the premise
    label = "contradiction"
elif miles_per_hour_hypothesis!= miles_per_hour_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
