average_speed_premise = 36
average_speed_hypothesis = 36

# the hypothesis refers to the average speed of the whole journey, which is also mentioned in the premise
if average_speed_hypothesis >= average_speed_premise:
    # check if the hypothesis value contradicts the premise value of 'average_speed_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it is not contradictory
    # but we cannot infer entailment since we don't know the exact value of Tom's speed
    label = "neutral"

print(label)
