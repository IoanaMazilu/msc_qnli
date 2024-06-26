average_speed_premise = 30
average_speed_hypothesis = 50

# the hypothesis refers to an average speed for Richard's trip, mentioned also in the premise
if average_speed_hypothesis <= average_speed_premise:
    # check if the estimate of 'average_speed_hypothesis' contradicts the average speed in the premise
    label = "contradiction"
elif average_speed_premise > average_speed_hypothesis:
    # check if the average speed in the premise contradicts the estimate of 'average_speed_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
