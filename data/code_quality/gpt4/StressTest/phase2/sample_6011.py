beat_distance_premise = 4
beat_distance_hypothesis = 6
start_late_premise = 4
start_late_hypothesis = 4

# the hypothesis refers to the beat distance and start late time mentioned in the premise
if beat_distance_premise >= beat_distance_hypothesis:
    # check if the 'beat_distance_hypothesis' contradicts the beat distance in the premise
    label = "contradiction"
elif start_late_hypothesis != start_late_premise:
    # check if the start late time in the hypothesis contradicts the start late time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the beat distance 
    # any beat distance greater than 'beat_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
