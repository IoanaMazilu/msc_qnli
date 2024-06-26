driving_time_premise = 4
driving_time_hypothesis = 8

if driving_time_hypothesis <= driving_time_premise:
    # check if the driving time in the hypothesis contradicts the driving time reported in the premise
    label = "contradiction"
else:
    # the premise gives the exact driving time
    # any driving time greater than 'driving_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
