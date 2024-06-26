start_time_premise = 0
end_time_premise = 44
average_speed_premise = 50

start_time_hypothesis = 0
end_time_hypothesis = 24
average_speed_hypothesis = 50

# the hypothesis refers to the time taken for the bus to reach Pune and the average speed
if end_time_hypothesis <= end_time_premise:
    # check if the estimate of 'end_time_hypothesis' contradicts the time taken in the premise
    label = "contradiction"
elif average_speed_hypothesis!= average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
