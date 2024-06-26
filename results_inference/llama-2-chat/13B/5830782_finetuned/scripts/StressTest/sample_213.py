average_speed_premise = 36
average_speed_hypothesis = 76

# the hypothesis refers to the average speed of the whole journey mentioned in the premise
if average_speed_premise >= average_speed_hypothesis:
    # check if the estimate of 'average_speed_premise' contradicts the estimate of average speed in the hypothesis
    label = "contradiction"
else:
    # if the premise's average speed does not contradict the hypothesis's estimate, we can infer entailment
    label = "entailment"

print(label)
