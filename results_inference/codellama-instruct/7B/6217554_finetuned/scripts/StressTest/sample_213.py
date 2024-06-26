average_speed_premise = 36
average_speed_hypothesis = 76

# the hypothesis gives an estimate for the average speed of the whole journey
# any average speed greater than 'average_speed_hypothesis' contradicts the premise
if average_speed_hypothesis <= average_speed_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed
    # any average speed greater than 'average_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
