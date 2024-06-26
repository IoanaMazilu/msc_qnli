average_speed_premise = 60
average_speed_hypothesis = 70

# the hypothesis talks about the average speed of Ganesh from X to Y, which is also referenced in the premise
if average_speed_premise >= average_speed_hypothesis:
    # check if 'average_speed_premise' contradicts the estimate of less than 'average_speed_hypothesis'
    label = "contradiction"
elif average_speed_premise < average_speed_hypothesis:
    # if the average speed in the premise is less than the average speed in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
