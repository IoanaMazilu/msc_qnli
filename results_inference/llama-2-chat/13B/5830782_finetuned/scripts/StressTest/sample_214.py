average_speed_premise = 76
average_speed_hypothesis = 36

# the hypothesis refers to the average speed of the journey mentioned in the premise
if average_speed_hypothesis >= average_speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_speed_premise'
    label = "contradiction"
elif average_speed_hypothesis < average_speed_premise:
    # the premise gives only an estimate for the average speed
    # any speed less than 'average_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
