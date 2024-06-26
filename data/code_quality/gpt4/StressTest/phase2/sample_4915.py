average_speed_premise = 56
average_speed_hypothesis = 36

# the hypothesis talks about the average speed of the whole journey, referenced also in the premise
if average_speed_hypothesis >= average_speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_speed_premise'
    label = "contradiction"
elif average_speed_hypothesis < average_speed_premise:
    # if the hypothesis value is less than 'average_speed_premise', it is consistent with the premise
    # however, the exact speed of Tom's driving from B to C cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
