race_distance_premise = 100
race_distance_hypothesis = 300

# the hypothesis refers to the distance of the race, mentioned in the premise
if race_distance_hypothesis <= race_distance_premise:
    # check if the estimate of 'race_distance_hypothesis' contradicts the distance of the race in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance of the race
    # any distance greater than 'race_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
