average_speed_premise_from = 40
average_speed_premise_to = 70
average_speed_hypothesis_from = 80
average_speed_hypothesis_to = 70

# the hypothesis talks about the average speed from Carl's home to the beach and back, referenced also in the premise
if average_speed_hypothesis_from <= average_speed_premise_from:
    # check if the speed from the beach in the hypothesis contradicts the estimate of more than 'average_speed_premise_from'
    label = "contradiction"
elif average_speed_hypothesis_to!= average_speed_premise_to:
    # check if the speed back from the beach in the hypothesis contradicts the speed back from the beach in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
