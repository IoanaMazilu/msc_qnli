avg_speed_premise = 14
avg_speed_hypothesis = 44

# the hypothesis also talks about the average speed of Ganesh from X to Y mentioned in the premise
if avg_speed_hypothesis <= avg_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'avg_speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed
    # any speed greater than 'avg_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
