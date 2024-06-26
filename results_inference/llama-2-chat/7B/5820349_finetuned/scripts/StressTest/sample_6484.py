distance_homes_premise = 80
distance_homes_hypothesis = 20
maxwell_speed = 4
brad_speed = 6

# the hypothesis talks about the distance between homes and the walking/running speeds of Maxwell and Brad, all referenced in the premise
if distance_homes_hypothesis >= distance_homes_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_homes_premise'
    label = "contradiction"
elif maxwell_speed!= 4 or brad_speed!= 6:
    # check if the speeds in the hypothesis contradict the speeds reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between homes
    # any distance less than 'distance_homes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
