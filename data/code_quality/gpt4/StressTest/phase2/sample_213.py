average_speed_premise = 36
average_speed_hypothesis = 76

# the hypothesis refers to the average speed of the journey mentioned in the premise
if average_speed_premise >= average_speed_hypothesis:
    # check if the estimate of 'average_speed_hypothesis' contradicts the average speed of the journey in the premise
    label = "contradiction"
else:
    # if the average speed of the journey in the premise is less than 'average_speed_hypothesis', we can infer entailment
    label = "entailment"

print(label)
