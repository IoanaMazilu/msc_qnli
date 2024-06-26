premise_distance = 80
hypothesis_distance = 20
maxwell_walking_speed = 4
brad_running_speed = 6

# the hypothesis refers to the distance between their homes and the walking speed of Maxwell
if hypothesis_distance < premise_distance:
    # check if the hypothesis value contradicts the estimate of less than 'premise_distance'
    label = "contradiction"
elif maxwell_walking_speed!= 4:
    # check if the walking speed of Maxwell contradicts the hypothesis
    label = "contradiction"
elif brad_running_speed!= 6:
    # check if the running speed of Brad contradicts the hypothesis
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between their homes and the walking speed of Maxwell
    # any distance between their homes and any walking speed of Maxwell is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
