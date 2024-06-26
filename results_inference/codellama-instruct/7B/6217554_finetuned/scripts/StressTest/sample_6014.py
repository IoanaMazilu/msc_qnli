average_speed_karen_premise = 60
average_speed_karen_hypothesis = 20
average_speed_tom_premise = 45
average_speed_tom_hypothesis = 45

# the hypothesis talks about the average speed of Karen and Tom, referenced also in the premise
if average_speed_karen_hypothesis!= average_speed_karen_premise:
    # check if the average speed of Karen in the hypothesis contradicts the average speed of Karen reported in the premise
    label = "contradiction"
elif average_speed_tom_hypothesis!= average_speed_tom_premise:
    # check if the average speed of Tom in the hypothesis contradicts the average speed of Tom reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
