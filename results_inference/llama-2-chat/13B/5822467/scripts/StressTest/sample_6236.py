anne_speed_premise = 1
anne_speed_hypothesis = 2
house_cleaning_time_premise = 3

# the hypothesis refers to the speed of Anne and the time it takes to clean the house
if anne_speed_hypothesis <= anne_speed_premise:
    # check if the estimate of 'anne_speed_hypothesis' contradicts the speed of Anne in the premise
    label = "contradiction"
elif house_cleaning_time_premise!= house_cleaning_time_hypothesis:
    # check if the time it takes to clean the house in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
