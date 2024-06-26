miles_per_hour_jog_premise = 3
miles_per_hour_walk_premise = 6
miles_per_hour_jog_hypothesis = 7
miles_per_hour_walk_hypothesis = 6

# the hypothesis refers to the speed at which Aaron will jog and walk back home
if miles_per_hour_jog_hypothesis <= miles_per_hour_jog_premise:
    # check if the estimate of'miles_per_hour_jog_hypothesis' contradicts the speed at which Aaron will jog in the premise
    label = "contradiction"
elif miles_per_hour_walk_hypothesis!= miles_per_hour_walk_premise:
    # check if the speed at which Aaron will walk back home in the hypothesis contradicts the speed at which Aaron will walk back home in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
