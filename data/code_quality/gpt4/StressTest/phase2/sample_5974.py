first_leg_distance_premise = 4
first_leg_distance_hypothesis = 8
stop_time_premise = 11
stop_time_hypothesis = 11
second_leg_distance_premise = 20
second_leg_distance_hypothesis = 20

# the hypothesis talks about the distance and time Jerry travelled, similar to the premise
if first_leg_distance_hypothesis <= first_leg_distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'first_leg_distance_premise'
    label = "contradiction"
elif stop_time_hypothesis != stop_time_premise:
    # check if the stop time in the hypothesis contradicts the stop time mentioned in the premise
    label = "contradiction"
elif second_leg_distance_hypothesis != second_leg_distance_premise:
    # check if the second leg distance in the hypothesis contradicts the second leg distance mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the first leg distance
    # any first leg distance greater than 'first_leg_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
