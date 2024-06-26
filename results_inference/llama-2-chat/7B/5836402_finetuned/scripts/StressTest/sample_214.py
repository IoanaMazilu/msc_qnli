average_speed_premise = 76
average_speed_hypothesis = 36

# the hypothesis refers to the average speed of the whole journey, which is also mentioned in the premise
if average_speed_hypothesis >= average_speed_premise:
    # check if the average speed in the hypothesis contradicts the estimate of less than 'average_speed_premise'
    label = "contradiction"
elif average_speed_hypothesis == average_speed_premise:
    # if the average speed in the hypothesis is equal to the premise, we can infer entailment
    label = "entailment"
else:
    # if the average speed in the hypothesis is less than the premise, it is a different value and cannot be entailed
    label = "neutral"

print(label)
