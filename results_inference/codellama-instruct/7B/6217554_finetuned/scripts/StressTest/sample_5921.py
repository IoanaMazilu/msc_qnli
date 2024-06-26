speed_premise_from_beach = 80
speed_premise_return_home = 70
speed_hypothesis_from_beach = 80
speed_hypothesis_return_home = 70

# the hypothesis refers to the average speed of Carl from the beach and home, mentioned in the premise
if speed_hypothesis_from_beach <= speed_premise_from_beach:
    # check if the estimate of'speed_hypothesis_from_beach' contradicts the average speed from the beach in the premise
    label = "contradiction"
elif speed_hypothesis_return_home!= speed_premise_return_home:
    # check if the average speed of Carl returning home from the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
