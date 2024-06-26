avg_speed_premise = 70
avg_speed_hypothesis = 60

# the hypothesis refers to the average speed of Ganesh mentioned in the premise
if avg_speed_hypothesis >= avg_speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'avg_speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed
    # any speed less than 'avg_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
