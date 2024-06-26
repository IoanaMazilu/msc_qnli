average_speed_premise = 36
average_speed_hypothesis = 76

# the hypothesis refers to the average speed of the whole journey mentioned in the premise
if average_speed_premise >= average_speed_hypothesis:
    # check if the average speed in the premise contradicts the estimate of less than 'average_speed_hypothesis'
    label = "contradiction"
else:
    # if the average speed in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
