average_speed_premise = 46
average_speed_hypothesis = 36

# the hypothesis refers to the average speed of the journey mentioned in the premise
if average_speed_hypothesis >= average_speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_speed_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
